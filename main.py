from fastapi import FastAPI
from core.database import Base, engine
from apps.api.urls import router as api_router  # Import from urls.py
from apps.cron.tasks import setup_cron_jobs
from insert_100_test_data import insert_test_data

app = FastAPI(title="Ad Metrics API")

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Create database tables
Base.metadata.create_all(bind=engine)

# Setup cron jobs
@app.on_event("startup")
async def startup_event():
    setup_cron_jobs()

if __name__ == "__main__":
    import uvicorn
    insert_test_data()
    uvicorn.run(app, host="0.0.0.0", port=8000)