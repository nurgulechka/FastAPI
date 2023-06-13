from fastapi import Depends, Response

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


@router.delete("/{ad_id: str}")
def delete_ad(
    ad_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    # ads = svc.repository.get_ads_by_user_id(ads_id)
    user_id = jwt_data.user_id
    delete_ad = svc.repository.delete_ad(ad_id, user_id)
    if delete_ad.deleted_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)
