from fastapi import FastAPI
from app.endpoints.user_endpoint import router as demo_router

app = FastAPI(
    title="CRUD",
    description="In this api, we are performing user creation, updation, deletion features"
)

app.include_router(demo_router)
