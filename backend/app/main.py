from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import books, members, borrow, dashboard
from app.database import Base, engine
from app import models

app = FastAPI(
    title="Library Management System API",
    description="API for managing books, members, and borrowing records",
    version="1.0.0"
)

# ========== CORS CONFIGURATION ==========
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== CREATE TABLES ==========
Base.metadata.create_all(bind=engine)

# ========== INCLUDE ROUTERS ==========
app.include_router(books.router)
app.include_router(members.router)
app.include_router(borrow.router)
app.include_router(dashboard.router)

# ========== BASIC ROUTES ==========
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Library Management System API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/test")
def test_endpoint():
    return {"message": "API test endpoint is working!"}

# ========== ERROR HANDLING ==========
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal server error: {str(exc)}"}
    )