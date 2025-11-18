from sqlalchemy.orm import Session
from app.db.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate
from app.utils.exceptions import NotFoundException

class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, order_data: OrderCreate) -> Order:
        order = Order(**order_data.dict())
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_order(self, order_id: int) -> Order:
        order = self.db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise NotFoundException(f"Order with id {order_id} not found")
        return order

    def update_order(self, order_id: int, order_data: OrderUpdate) -> Order:
        order = self.get_order(order_id)
        for key, value in order_data.dict(exclude_unset=True).items():
            setattr(order, key, value)
        self.db.commit()
        self.db.refresh(order)
        return order

    def delete_order(self, order_id: int) -> None:
        order = self.get_order(order_id)
        self.db.delete(order)
        self.db.commit()