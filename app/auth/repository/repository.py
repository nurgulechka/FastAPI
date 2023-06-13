from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    # added city, phone, name params
    def create_user(self, user: dict):
        payload = {
            "name": user["name"],
            "email": user["email"],
            "password": hash_password(user["password"]),
            "phone": user["phone"],
            "city": user["city"],
            "created_at": datetime.utcnow(),
        }

        self.database["users"].insert_one(payload)

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    # user_id
    def update_param(self, user: dict):
        update_user = {
            "name": user["name"],
            "phone": user["phone"],
            "city": user["city"],
        }

        self.database["users"] = update_user

    # def update_user(self, user_id: str, data: dict):
    #     self.database["users"].update_one(
    #         filter={"_id": ObjectId(user_id)},
    #         update={
    #             "$set": {
    #                 "phone": data["phone"],
    #                 "name": data["name"],
    #                 "city": data["city"],
    #             }
    #         },
    #     )
    def get_user_by_email(self, email: str) -> Optional[dict]:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user

    # def get_user_info(self):
    #     user = self.database["users"]
