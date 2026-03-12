from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Vacation Assistant",
    description="AI-powered travel planning assistant for budget-based trip recommendations.",
    version="1.0",
)
app.include_router(router=router)


@app.get("/")
async def root():
    return {"message": "AI Vacation Assistant API is running"}


@app.get("/health")
async def health():
    return {"status": "OK"}
