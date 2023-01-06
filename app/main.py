import uvicorn

from fastapi import FastAPI
from app.api.endpoints import router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
