import requests
import allure
from config.headers import Headers
from services.user.payloads import Payloads
from services.user.endpoints import Endpoints
from utils.helper import Helper
from services.user.models.user_model import UserModel


class UserAPI(Helper):

    def __init__(self):
        self._headers = Headers()
        self._endpoints = Endpoints()
        self._payloads = Payloads()

    @allure.step("Поиск питомца по имени")
    def get_user(self, username, expected_result):
        response = requests.post(
            url=self._endpoints.get_user_by_username(username),
            headers=self._headers.basic,
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, (response.json())
            model = UserModel(**response.json())
            return model
        else:
            assert response.status_code != 200
            return response.json()