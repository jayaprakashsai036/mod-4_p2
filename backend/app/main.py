from fastapi import FastAPI
from .api.routes import router
from .core.config import APP_NAME

app = FastAPI(title=APP_NAME, version="1.0.0")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
