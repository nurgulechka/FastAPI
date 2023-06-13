from datetime import datetime
from typing import List, Optional

from bson.objectid import ObjectId
from pymongo.database import Database


class AdsRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_ad(self, ads: dict):
        payload = {
            "user_id": ObjectId(input["user_id"]),
            "type_": ads["type_"],
            "price": ads["price"],
            "address": ads["address"],
            "area": ads["area"],
            "rooms_count": ads["rooms_count"],
            "description": ads["description"],
            "created_at": datetime.utcnow(),
        }
        self.database["ads"].insert_one(payload)

    def get_ads_by_user_id(self, user_id: str) -> Optional[List[dict]]:
        ads = self.database["ads"].find({"user_id": ObjectId(user_id)})
        result = []
        for ad in ads:
            result.append(ad)
        return result
