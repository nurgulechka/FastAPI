from typing import Any

from app.utils import AppModel
from fastapi import Depends
from pydantic import Field

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateAdRequest(AppModel):
    # "user_id": ObjectId(input["user_id"]),
    #         "type_": ads["type"],
    #         "price": ads["price"],
    #         "address": ads["address"],
    #         "area": ads["area"],
    #         "rooms_count": ads["rooms_count"],
    #         "description": ads["description"],
    type_: str
    price: int
    address: str
    area: float
    rooms_count: int
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
    svc.repository.create_ad({"user_id": user_id, "ads": input.dict()})

    return Response(status_code=200)
