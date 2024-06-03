from fastapi import FastAPI
import uvicorn

from api.main import api_router


app = FastAPI(
    title="myapiv1", version="0.0.1",
)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
