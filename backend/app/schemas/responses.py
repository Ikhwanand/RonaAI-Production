from typing import Generic, TypeVar, Optional, Any 
from pydantic import BaseModel

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool 
    message: str 
    data: Optional[T] = None 
    errors: Optional[list] = None 

