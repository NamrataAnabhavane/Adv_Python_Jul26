from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="My First API",
    description="This is my first FastAPI app",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name:str):
    return {"message": "Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run(
        "P2:app",
        host= "127.0.0.1",
        port=8000,
        reload=True
    )