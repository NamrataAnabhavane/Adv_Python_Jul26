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
    return {"message": f"Hello, {name}!"}

@app.get("/users/{user_id}/orders/{order_id}")
async def get_order(user_id:int,order_id:int):
    return {
        "user_id":user_id,
        "order_id":order_id,
        "order":f"Order {order_id} for user {user_id}"
    }

if __name__ == "__main__":
    uvicorn.run(
        "P2:app",
        host= "127.0.0.1",
        port=8000,
        reload=True
    )