import os
from dotenv import load_dotenv

load_dotenv()

class Headers:


    # def basic(self, typecontent='application/json'):
    #     return {
    #     'Content-Type': typecontent
    # }


    basic = {
        'Content-Type': 'application/json'
    }

# class Headers:
#
#     basic = {
#         'Content-Type': 'application/json',
#         'Authorization': f"Bearer {os.getenv('TOKEN')}"
#     }
