#Query Parameters:
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/search")
async def search(q: str, limit: int = 10):
    return {"query":q, "limit":limit}

@app.get("/products")
async def get_products(
    category: OPtional[str] = None,
    min_price: float = 0,
    max_price: float = 1000,
    in_stock: bool = True,
    sort_by: str = "name",
    order: str = "asc"
):
    return{
        "Category":category,
        "min_price":min_price ,
        "max_price":max_price ,
        "in_stock":in_stock,
        "sort_by":sort_by ,
        "order":order ,
    }

#http://127.0.0.1:8000/products?category=Electronics&min_price=100&sort_by=price

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "P1:app",
        host= "127.0.0.1",
        port=8000,
        reload=True
    )

#http://127.0.0.1:8000/search?q=python&limit=5