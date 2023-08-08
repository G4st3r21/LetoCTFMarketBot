from dataclasses import dataclass
from typing import Optional

from app.api.dto.base import BaseResponse


@dataclass
class OrderHistoryResponse(BaseResponse):
    id: str
    orders: Optional[str]