from fastapi import FastAPI



app = FastAPI(title="devops utilites api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("build_api:app", host="127.0.0.1", port=8000, reload=False)

@app.get("/hello")
def hello():
    return {"message" : "hi this is my api for devops utilites"}




