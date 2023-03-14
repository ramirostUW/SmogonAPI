# pylint:disable=unused-argument
"""
This is the root module of our Smogon API. It is a barebones file that
mostly just grabs the endpoints from the appropriate submodules.
"""

import uvicorn
from fastapi import FastAPI
from .submodules import smogon_endpoints, http_endpoints, kaggle_data_endpoints

myApp = FastAPI()
myApp.include_router(smogon_endpoints.router)
myApp.include_router(http_endpoints.router)
myApp.include_router(kaggle_data_endpoints.router)


def main():
    """Starts up a server locally when called"""
    uvicorn.run(myApp)


if __name__ == "__main__":
    main()
