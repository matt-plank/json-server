from routes import prediction

from json_server.api import Api

api = Api()
api.add_router("/prediction", prediction.router)

if __name__ == "__main__":
    api.run("0.0.0.0", 8000)
