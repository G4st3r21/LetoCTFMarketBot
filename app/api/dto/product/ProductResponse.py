from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseResponse


@dataclass
class ProductResponse(BaseResponse):
    id: str
    name: str
    description: Optional[str]
    price: float
    hidden: bool
    sizes: Optional[str]
