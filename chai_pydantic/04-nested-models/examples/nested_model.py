from typing import List, Optional 
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
    
class User(BaseModel):
    id:int
    name:str
    address:Address
    
    
class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']] = None  # Recursive type for nested comments
    
Comment.model_rebuild()


address= Address(
    street="123 Main St",
    city="Jaipur",
    postal_code="12345"
)

user= User(
    id=1,
    name="John Doe",
    address=address
)

comment= Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a nested comment",
            replies=[
                Comment(
                    id=3,
                    content="This is a reply to the nested comment"
                )
            ]
        )
    ]
)

print(user)
print(comment)