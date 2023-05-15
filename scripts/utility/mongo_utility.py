from pymongo import MongoClient  # import mongo client to connect
# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23
inventory_item = {"id": "2210",
                  "name": "Chikni",
                  "quantity": "50",
                  "cost": "8000"
                  }
# # Creating document
inventory = db.riya_inventory
# # Inserting data
inventory.insert_one(inventory_item)
# # Fetching data
print(inventory.find_one({"id": "2209"}))