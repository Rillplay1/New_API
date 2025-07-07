from faker import Faker

faker = Faker()

class Payloads:

    def create_pet(self):
        return {
  "id": faker.random_int(),
  "category": {
    "id": faker.random_int(),
    "name": "loli",
  },
  "name": faker.name(),
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": faker.random_int(),
      "name": faker.name(),
    }
  ],
  "status": "available"
}
