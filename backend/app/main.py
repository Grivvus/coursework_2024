from fastapi import FastAPI
import uvicorn

from app.api.main import api_router


app = FastAPI(
    title="my_own_tech_market_api", version="0.2.0",
)
app.include_router(api_router, prefix="api_v1/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
