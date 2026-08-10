from fastapi import FastAPI
from typing import Optional 

app = FastAPI()

# Simple query parameters
@app.get("/search")
async def search(q: str,limit: int = 10):
    return {"query":q,"limit":limit}

# Multiple query parameters
@app.get("/products")
async def get_products(
    category: Optional[str] = None,
    min_price: float = 0,
    max_price: float = 1000,
    in_stock: bool = True,
    sort_by: str = "name",
    order: str = "asc"
):
    return{
        "category":category,
        "min_price":min_price ,
        "max_price":max_price ,
        "in_stock":in_stock ,
        "sort_by":sort_by,
        "order":order 
    }

# Run our application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "P1:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
