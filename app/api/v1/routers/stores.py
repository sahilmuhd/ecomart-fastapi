from fastapi import APIRouter, Depends, HTTPException
from app.schemas.store import StoreCreate, StoreUpdate, Store
from app.services.store_service import StoreService
from app.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=Store)
async def create_store(store: StoreCreate, current_user: str = Depends(get_current_user)):
    return await StoreService.create_store(store, current_user)

@router.get("/{store_id}", response_model=Store)
async def read_store(store_id: int, current_user: str = Depends(get_current_user)):
    store = await StoreService.get_store(store_id, current_user)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.put("/{store_id}", response_model=Store)
async def update_store(store_id: int, store: StoreUpdate, current_user: str = Depends(get_current_user)):
    updated_store = await StoreService.update_store(store_id, store, current_user)
    if not updated_store:
        raise HTTPException(status_code=404, detail="Store not found")
    return updated_store

@router.delete("/{store_id}", response_model=dict)
async def delete_store(store_id: int, current_user: str = Depends(get_current_user)):
    success = await StoreService.delete_store(store_id, current_user)
    if not success:
        raise HTTPException(status_code=404, detail="Store not found")
    return {"detail": "Store deleted successfully"}