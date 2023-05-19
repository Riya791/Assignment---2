"""Here is the creation of main file which includes fastapi,dotenv,uvicorn,item_router"""

# importing uvicorn
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from scripts.core.services.billing_services import item_router
from scripts.constants.app_constants import *
from scripts.constants.app_configurations import *

# Calling FastAPI
app = FastAPI()

app.include_router(item_router)

if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(host = SERVICE_HOST,app=CommonConstants.APP_KEY, port=int(SERVICE_PORT),reload=True)
