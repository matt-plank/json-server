from json_server.api import Api
from routes import prediction

api = Api()
api.add_router("/prediction", prediction.router)

if __name__ == "__main__":
    api.run("0.0.0.0", 8000)
