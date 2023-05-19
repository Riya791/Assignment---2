from scripts.constants.app_constants import DBConstants, Aggregation
from scripts.core.db.mongo.interns_b2_23.Riya.mongo_query import read_item, create_item, update_item, delete_item, Item, \
    pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass, MongoConnect


class ItemHandler:

    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConstants.DB_DATABASE,
                                                       mongo_client=MongoConnect(DBConstants.DB_URI).client,
                                                       collection=DBConstants.DB_COLLECTION)

    def read_data(self):
        res = self.user_mongo_obj.find({})
        # res= 'success'
        if res:
            return {"status": "success", "message": "Records Displayed "}
        else:
            return {"status": "failed", "message": "Error in displaying", "error": ""}

    def create_data(self, item: Item):
        res = self.user_mongo_obj.insert_one(data=item.dict())
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Inserted"}
        else:
            return {"status": "failed", "message": "Error inserting", "error": ""}

    def update_data(self, item_id: int, item: Item):
        res = self.user_mongo_obj.update_one({"id": item_id}, item.dict())
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Updated"}
        else:
            return {"status": "failed", "message": "Error", "error": ""}

    def delete_data(self, item_id: int):
        res = self.user_mongo_obj.delete_one({'id': item_id})
        # res= 'success'
        if res:
            return {"status": "success", "message": "Record Deleted"}
        else:
            return {"status": "failed", "message": "Error", "error": ""}

    def pipeline_aggregation(self):
        data = pipeline_aggregation(Aggregation.Agr)
        print(data)
        return list(data)[0]['total']
