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
    price: str
    address: str
    area: str
    rooms_count: str
    description: str


# class AuthorizeUserResponse(AppModel):
#     access_token: str
#     token_type: str = "Bearer"


@router.post("/")  # , response_model=AuthorizeUserResponse)
def create_ad(
    input: CreateAdRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id
    svc.repository.create_ad(
        {
            "user_id": user_id,
            "type_": input.type_,
            "price": input.price,
            "address": input.address,
            "area": input.area,
            "rooms_count": input.rooms_count,
            "description": input.description,
        }
    )

    return Response(status_code=200)
