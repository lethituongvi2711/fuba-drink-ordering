from fastapi import FastAPI

app = FastAPI(title="Fuba Drink Ordering API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Fuba Backend is running"}


@app.get("/health/db")
def check_db_connection():
    return {
        "status": "success",
        "database": "connected",
        "mode": "mock_pending_sql_server",
        "test_query": 1,
    }
