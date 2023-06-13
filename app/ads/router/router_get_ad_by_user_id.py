from typing import Any, List

from app.utils import AppModel
from fastapi import Depends
from pydantic import Field

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetAdsByUserId(AppModel):
    id: Any = Field(alias="_id")
    # user_id: str
    type_: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class GetAdsResponse(AppModel):
    ads: List[GetAdsByUserId]


@router.get("/{user_id}")
def get_ads_by_user_id(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, Any]:
    user_id = jwt_data.user_id
    ads = svc.repository.get_ad_by_user_id(user_id)
    response = {"ads": ads}
    return response
