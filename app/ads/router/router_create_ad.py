from typing import Any

from app.utils import AppModel
from fastapi import Depends
from pydantic import Field

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateAdRequest(AppModel):
    type_: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateAdResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post("/", response_model=CreateAdResponse)
def create_ad(
    input: CreateAdRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, Any]:
    user_id = jwt_data.user_id
    ad_id = svc.repository.create_ad(user_id, input.dict())

    return CreateAdResponse(id=ad_id)
