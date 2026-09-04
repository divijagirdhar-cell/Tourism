from fastapi import FastAPI

app = FastAPI(title="Tourism Boost API")


@app.get("/")
def home():
    return {
        "message": "Tourism Backend is Working!"
    }