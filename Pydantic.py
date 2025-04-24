from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core.core_schema import FieldValidationInfo

class User(BaseModel):
    name: str
    email: EmailStr     # Validates that the email has a correct format
    account_id: int

    # Validator to ensure that account_id is strictly positive
    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value: int, info: FieldValidationInfo) -> int:
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

# This line will raise a validation error due to the invalid email
try:
    user = User(name='Ali', email='ali', account_id=1234)
except Exception as e:
    print("Validation Error:", e)

# Creating a valid user
user = User(name='Ali', email='ali@gmail.com', account_id=1234)

# Display the Python model
print(user)

# Convert the model to JSON (string)
user_json_str = user.model_dump_json()
print(user_json_str)

# Convert to a Python dictionary
user_json_obj = user.model_dump()
print(user_json_obj)

# Example of creating an instance from a raw JSON string
import json

json_str = '{"name": "Ali", "email": "ali@gmail.com", "account_id": 1234}'
user = User.model_validate_json(json_str)
print(user)