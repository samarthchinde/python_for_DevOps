
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="devops utilities api")

@app.get("/hello")
def hello():
    return {"message": "hi this is my api for devops utilities"}

if __name__ == "__main__":
    uvicorn.run(
        "build_api:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )
