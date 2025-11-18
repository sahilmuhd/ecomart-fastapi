from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate
from app.services.inventory_service import InventoryService

router = APIRouter()
inventory_service = InventoryService()

@router.post("/", response_model=Inventory)
def create_inventory(item: InventoryCreate, db: Session = Depends(get_db)):
    return inventory_service.create_inventory(db=db, item=item)

@router.get("/{inventory_id}", response_model=Inventory)
def read_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory_item = inventory_service.get_inventory(db=db, inventory_id=inventory_id)
    if inventory_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return inventory_item

@router.put("/{inventory_id}", response_model=Inventory)
def update_inventory(inventory_id: int, item: InventoryUpdate, db: Session = Depends(get_db)):
    updated_item = inventory_service.update_inventory(db=db, inventory_id=inventory_id, item=item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return updated_item

@router.delete("/{inventory_id}", response_model=dict)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    success = inventory_service.delete_inventory(db=db, inventory_id=inventory_id)
    if not success:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return {"detail": "Inventory item deleted successfully"}