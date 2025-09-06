from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BlogPostBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    content: str
    published: bool = True


class BlogPostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool

    model_config = {"from_attributes": True}


class PortfolioItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    link: Optional[str] = None
    image_url: Optional[str] = None
    tags: Optional[list[str]] = None


class PortfolioItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    image_url: Optional[str] = None
    tags: Optional[list[str]] = None

    model_config = {"from_attributes": True}
    
    @field_validator('tags', mode='before')
    @classmethod
    def validate_tags(cls, v):
        # Convert comma-separated tags string back to list
        if isinstance(v, str) and v:
            return [tag.strip() for tag in v.split(',')]
        elif v is None:
            return []
        return v


# Authentication schemas
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
