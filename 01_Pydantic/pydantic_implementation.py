from pydantic import BaseModel, Field
from typing import Optional

# class Person(BaseModel):
#     name: str = Field(default="John Doe", min_length=3, max_length=10, description="The name of the person")
#     age: int = Field(default=20, gt=0, lt=100, description="The age of the person")
#     email: str = Field(default="user@gmail.com", description="The email of the person")
#     Hobbies: list[str] = Field(default=["reading", "writing", "coding"], description="The hobbies of the person")

# # Create an instance of the Person class
# person = Person(name="John", age='25', email="john@example.com")
# print(person)

# Model with nested Model
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Person(BaseModel):
    name: str
    age: int
    address: Address

person=Person(name="John", age=20, address=Address(street="123 Main St", city="Anytown", state="CA", zip_code="12345"))
print(person)




