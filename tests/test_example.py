import allure


from config.base_test import BaseTest

@allure.epic("Coздание нового питомца")
class TestExample(BaseTest):
    @allure.title("Создание нового питомца")
    def test_create_new_pet(self):
        user = self.api_pet.create_pet()
        self.user_api.get_user(user.name)