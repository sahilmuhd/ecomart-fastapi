from sqlalchemy.orm import Session
from app.db.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_create: ProductCreate, tenant_id: int) -> Product:
        product = Product(**product_create.dict(), tenant_id=tenant_id)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_product(self, product_id: int, tenant_id: int) -> Product:
        return self.db.query(Product).filter(Product.id == product_id, Product.tenant_id == tenant_id).first()

    def update_product(self, product_id: int, product_update: ProductUpdate, tenant_id: int) -> Product:
        product = self.get_product(product_id, tenant_id)
        if product:
            for key, value in product_update.dict(exclude_unset=True).items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product

    def delete_product(self, product_id: int, tenant_id: int) -> bool:
        product = self.get_product(product_id, tenant_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False

    def list_products(self, tenant_id: int, skip: int = 0, limit: int = 10):
        return self.db.query(Product).filter(Product.tenant_id == tenant_id).offset(skip).limit(limit).all()