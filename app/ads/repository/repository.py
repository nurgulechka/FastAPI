from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


class AdsRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_ad(self, user_id: str, ads: dict):
        payload = {
            "user_id": ObjectId(user_id),
            "type_": ads["type_"],
            "price": ads["price"],
            "address": ads["address"],
            "area": ads["area"],
            "rooms_count": ads["rooms_count"],
            "description": ads["description"],
            "created_at": datetime.utcnow(),
        }
        self.database["ads"].insert_one(payload)

    def get_ads_by_user_id(self, user_id: str) -> List[dict]:
        # return self.database["ads"].find_many({"user_id": ObjectId(user_id)})

        ads_ = self.database["ads"].find(
            {
                "user_id": ObjectId(user_id),
            }
        )
        result = []
        for ad in ads_:
            result.append(ad)
        return result
        # return self.database["ads"].find_many({"user_id": ObjectId(user_id)})

    def delete_ad(self, ad_id: str, user_id: str) -> DeleteResult:
        return self.database["ads"].delete_one(
            {"_id": ObjectId(ad_id), "user_id": ObjectId(user_id)}
        )

    def update_ad(self, ad_id: str, user_id: str, updated_data: dict) -> UpdateResult:
        # usr_id = ObjectId(user_id)
        self.database["ads"].update_one(
            filter={"_id": ObjectId(ad_id), "user_id": ObjectId(user_id)},
            update={"$set": updated_data},
        )

    # def update_ad_by_user(self, user_id: str, ads: dict):
