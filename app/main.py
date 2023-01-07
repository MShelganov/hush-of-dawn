import uvicorn

# Импортируем роутер.
from app.api.meeting_room import router
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.app_title)

# Подключаем роутер.
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
