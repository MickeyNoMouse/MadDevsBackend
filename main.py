from fastapi import FastAPI
from user_routes import router as user_router
import uvicorn
from shop_routes import router as shop_router
from product_routes import router as product_router
from brand_routes import router as brand_router
from payment_routes import router as payment_router
from statistics_routes import router as statistics_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(shop_router, prefix="/shops", tags=["shops"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(brand_router, prefix="/brands", tags=["brands"])
app.include_router(payment_router, prefix="/payments", tags=["payments"])
app.include_router(statistics_router, prefix="/statistics", tags=["statistics"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)