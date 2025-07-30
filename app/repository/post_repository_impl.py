from __future__ import annotations

from dto.delete_post import DeletePost
from sqlmodel import Session, asc, desc, select

from app.dto.create_post import CreatePost
from app.dto.update_post import UpdatePost
from app.entity.post import Post
from app.repository.post_repository import PostRepository


class PostRepositoryImpl(PostRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, sort: str | None = "desc") -> list[Post]:
        statement = select(Post).where(not Post.deleted)
        if sort == "desc":
            statement = statement.order_by(desc(Post.post_number))
        else:
            statement = statement.order_by(asc(Post.post_number))
        return self.session.exec(statement).all()

    def get(self, post_number: int) -> Post | None:
        statement = select(Post).where(
            Post.post_number == post_number, not Post.deleted
        )
        return self.session.exec(statement).first()

    def save(self, create_post: CreatePost) -> int:
        post = Post.model_validate(create_post)
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post.post_number

    def update(self, update_post: UpdatePost) -> int | None:
        post = self.get(post_number=update_post.post_number)
        if not post:
            return None

        update_data = update_post.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(post, key, value)

        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post.post_number

    def delete(self, delete_post: DeletePost) -> int | None:
        post = self.get(post_number=delete_post.post_number)
        if not post:
            return None

        post.deleted = True
        self.session.add(post)
        self.session.commit()
        return post.post_number
