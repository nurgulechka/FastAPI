from typing import Any, Optional

from app.utils import AppModel
from fastapi import Depends, Response

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateAdRequest(AppModel):
    type_: Optional[str] = None
    price: Optional[int] = None
    address: Optional[str] = None
    area: Optional[float] = None
    rooms_count: Optional[int] = None
    description: Optional[str] = None


@router.patch("/{ad_id: str}")
def update_ad(
    ad_id: str,
    input: UpdateAdRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, Any]:
    # ads = svc.repository.get_ads_by_user_id(ads_id)
    user_id = jwt_data.user_id
    updated_ads = svc.repository.update_ad(
        ad_id, user_id, input.dict(exclude_unset=True)
    )
    if updated_ads.modified_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)
