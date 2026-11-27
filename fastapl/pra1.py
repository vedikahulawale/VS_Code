
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock: bool



product = Product(
    product_id="50",
    name="Laptop",
    price="199.99",
    in_stock="1"
)

print("Valid Product:")
print(product)
print("Product ID:", product.product_id)
print("Price:", product.price)
print("In Stock:", product.in_stock)



try:
    broken_product = Product(
        product_id="abc",
        name="Mobile",
        price="invalid",
        in_stock="1"

    )

except ValidationError as e:
    print("\nValidation Error:")
    print(e)
    print("Total Errors:", e.error_count())

