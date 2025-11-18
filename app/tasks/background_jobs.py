from celery import shared_task
from app.db.session import get_db
from app.db.models.inventory import Inventory
from app.db.models.order import Order

@shared_task
def sync_inventory(product_id, quantity):
    db = get_db()
    inventory_item = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if inventory_item:
        inventory_item.quantity += quantity
        db.commit()

@shared_task
def process_order(order_id):
    db = get_db()
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        # Logic to process the order
        order.status = 'processed'
        db.commit()