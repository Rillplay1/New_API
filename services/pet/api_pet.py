import requests
import allure
from config.headers import Headers
from services.pet.payloads import Payloads
from services.pet.endpoints import Endpoints
from utils.helper import Helper
from services.pet.models.pet_model import PetModel

class PetAPI(Helper):

    def __init__(self):
        self._headers = Headers()
        self._endpoints = Endpoints()
        self._payloads = Payloads()

    @allure.step("Создание нового питомца")
    def create_pet(self, expected_result):
        response = requests.post(
            url=self._endpoints.create_user,
            headers=self._headers.basic,
            json=self._payloads.create_pet()
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, (response.json())
            model = PetModel(**response.json())
            return model
        else:
            assert response.status_code != 200
            return response.json()
