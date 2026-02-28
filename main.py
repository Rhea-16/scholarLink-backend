from fastapi import FastAPI
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models.user import Base
from app.routes import auth
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.profile import router as profile_router
from app.routes.scholarships_routes import router as scholarship_router
from app.routes.saved_scholarship_routes import router as saved_scholarship_router
from app.routes.get_user_profile import router as get_profile_router
from app import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",  # Vite frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(profile_router)
app.include_router(scholarship_router)
app.include_router(saved_scholarship_router)
app.include_router(get_profile_router)

@app.get("/")
def health_check():
    return {"status": "Backend running"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Scholarship Portal API",
        version="1.0.0",
        description="Backend API for Scholarship Portal",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

