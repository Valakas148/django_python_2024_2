import os
import uuid


class FileService:
    @staticmethod
    def upload_car_photo(instance, filename: str)-> str:
        ex = filename.split('.')[-1]
        return os.path.join('cars_photo', f"{uuid.uuid1()}.{ex}")