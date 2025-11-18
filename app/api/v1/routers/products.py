from fastapi import APIRouter, HTTPException, Depends
from app.schemas.product import ProductCreate, ProductUpdate, Product
from app.services.product_service import ProductService
from app.api.v1.deps import get_current_tenant

router = APIRouter()

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate, tenant=Depends(get_current_tenant)):
    return await ProductService.create_product(product, tenant)

@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int, tenant=Depends(get_current_tenant)):
    product = await ProductService.get_product(product_id, tenant)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate, tenant=Depends(get_current_tenant)):
    updated_product = await ProductService.update_product(product_id, product, tenant)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", response_model=dict)
async def delete_product(product_id: int, tenant=Depends(get_current_tenant)):
    success = await ProductService.delete_product(product_id, tenant)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}