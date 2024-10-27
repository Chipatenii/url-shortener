from . import mongo

class URL:
    @staticmethod
    def create(original_url, short_code):
        mongo.db.urls.insert_one({"original_url": original_url, "short_code": short_code})

    @staticmethod
    def find_by_code(short_code):
        return mongo.db.urls.find_one({"short_code": short_code})
