from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from schemas import BlogPostBase, PortfolioItemBase, BlogPostOut, PortfolioItemOut, LoginRequest, TokenResponse
from sqlalchemy.orm import Session
import boto3
import uuid
from datetime import timedelta

from database import get_db, create_db_and_tables
from crud import (create_blog_post, update_blog_post, get_blog_posts, list_blog_posts, delete_blog_post,
                  create_portfolio_item, update_portfolio_item, get_portfolio_items, list_portfolio_items, delete_portfolio_item)
from auth import authenticate_user, create_access_token, verify_token
from config import settings


app = FastAPI()

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    create_db_and_tables()

origins = [
    "http://localhost:3000",
    "http://localhost:5173", # Vite dev server
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Authentication endpoint
@app.post("/admin/login", response_model=TokenResponse)
def login(login_request: LoginRequest):
    if not authenticate_user(login_request.username, login_request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": login_request.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Public endpoints (no authentication required)
@app.get("/posts", response_model=list[BlogPostOut])
def list_posts_api(db: Session = Depends(get_db)):
    return list_blog_posts(db)


@app.get("/posts/{post_id}")
def get_post_api(post_id: int, db: Session = Depends(get_db)):
    post = get_blog_posts(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
    return post


@app.get("/portfolio", response_model=list[PortfolioItemOut])
def list_portfolio_api(db: Session = Depends(get_db)):
    return list_portfolio_items(db)


@app.get("/portfolio/{item_id}")
def get_portfolio_item_api(item_id: int, db: Session = Depends(get_db)):
    item = get_portfolio_items(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Portfolio item not found.")
    return item


# Protected admin endpoints (authentication required)
@app.post("/admin/posts")
def create_post_api(post: BlogPostBase, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    if not post.title or not post.content:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title and content are required.")
    return create_blog_post(db, post)


@app.patch("/admin/posts/{post_id}")
def update_post_api(post_id: int, post_update: BlogPostBase, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    post = update_blog_post(db, post_id, post_update)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
    return post


@app.delete("/admin/posts/{post_id}")
def delete_post_api(post_id: int, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    success = delete_blog_post(db, post_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
    return {"detail": "Post deleted successfully."}


@app.post("/admin/portfolio")
def create_portfolio_item_api(item: PortfolioItemBase, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    if not item.name or not item.description:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name and description are required.")
    return create_portfolio_item(db, item)


@app.patch("/admin/portfolio/{item_id}")
def update_portfolio_item_api(item_id: int, item_update: PortfolioItemBase, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    item = update_portfolio_item(db, item_id, item_update)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Portfolio item not found.")
    return item


@app.delete("/admin/portfolio/{item_id}")
def delete_portfolio_item_api(item_id: int, db: Session = Depends(get_db), _: str = Depends(verify_token)):
    success = delete_portfolio_item(db, item_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Portfolio item not found.")
    return {"detail": "Portfolio item deleted successfully."}


@app.post("/admin/upload-image/")
def upload_image(
    file: UploadFile = File(...),
    bucket: str = Form(...),
    region: str = Form(...),
    access_key: str = Form(...),
    secret_key: str = Form(...),
    _: str = Depends(verify_token)
):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    ext = file.filename.split('.')[-1]
    key = f"portfolio/{uuid.uuid4()}.{ext}"
    s3.upload_fileobj(file.file, bucket, key, ExtraArgs={"ACL": "public-read"})
    url = f"https://{bucket}.s3.{region}.amazonaws.com/{key}"
    return {"image_url": url}