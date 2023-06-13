from typing import Optional

from app.utils import AppModel
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from ..utils.security import check_password
from . import router
from .dependencies import parse_jwt_user_data
from .errors import InvalidCredentialsException


class GetMyAccountRequest:
    phone: Optional[str]
    city: Optional[str]
    email: Optional[str]


class GetMyAccountResponse(AppModel):
    access_token: str
    token_type: str = "Bearer"


@router.patch("/users/me", response_model=GetMyAccountResponse)
def patch_my_data(
    input: GetMyAccountRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyAccountResponse:
    user = svc.repository.get_user_by_id(jwt_data.user_id)
    # if input.name:
    # if input.city:
    # if input.email:
    # if input.phone:
    svc.repository.update_param(user, input.dict())
    return Response(status_code=200)
