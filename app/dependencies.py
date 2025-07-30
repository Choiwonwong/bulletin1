from config.database import get_session
from fastapi import Depends
from repository.post_repository_impl import PostRepositoryImpl
from service.post_service_impl import PostServiceImpl
from sqlmodel import Session


def get_post_repository(session: Session = Depends(get_session)) -> PostRepositoryImpl:
    """PostRepository 의존성 생성"""
    return PostRepositoryImpl(session)


def get_post_service(
    post_repository: PostRepositoryImpl = Depends(get_post_repository),
) -> PostServiceImpl:
    """PostService 의존성 생성"""
    return PostServiceImpl(post_repository)
