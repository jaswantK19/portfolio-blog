from sqlalchemy.orm import Session
from models import BlogPost, PortfolioItem
from schemas import BlogPostBase, PortfolioItemBase

# --- BlogPost CRUD ---


def create_blog_post(db: Session, post: BlogPostBase) -> BlogPost:
    db_post = BlogPost(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_blog_posts(db: Session, post_id: int) -> BlogPost | None:
    return db.query(BlogPost).filter(BlogPost.id == post_id).first()


def list_blog_posts(db: Session) -> list[BlogPost]:
    return db.query(BlogPost).order_by(BlogPost.created_at.desc()).all()


def update_blog_post(db: Session, post_id: int, post_update: BlogPostBase) -> BlogPost | None:
    post = get_blog_posts(db, post_id)
    if not post:
        return None
    for key, value in post_update.model_dump(exclude_unset=True).items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post


def delete_blog_post(db: Session, post_id: int) -> bool:
    post = get_blog_posts(db, post_id)
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True

# --- PortfolioItem CRUD ---


def create_portfolio_item(db: Session, item: PortfolioItemBase) -> PortfolioItem:
    item_data = item.model_dump()
    # Convert tags list to comma-separated string
    if item_data.get('tags'):
        item_data['tags'] = ','.join(item_data['tags'])
    
    db_item = PortfolioItem(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_portfolio_items(db: Session, item_id: int) -> PortfolioItem | None:
    return db.query(PortfolioItem).filter(PortfolioItem.id == item_id).first()


def list_portfolio_items(db: Session) -> list[PortfolioItem]:
    return db.query(PortfolioItem).order_by(PortfolioItem.created_at.desc()).all()


def update_portfolio_item(db: Session, item_id: int, item_update: PortfolioItemBase) -> PortfolioItem | None:
    item = get_portfolio_items(db, item_id)
    if not item:
        return None
    
    update_data = item_update.model_dump(exclude_unset=True)
    # Convert tags list to comma-separated string
    if 'tags' in update_data and update_data['tags']:
        update_data['tags'] = ','.join(update_data['tags'])
    
    for key, value in update_data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_portfolio_item(db: Session, item_id: int) -> bool:
    item = get_portfolio_items(db, item_id)
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True

