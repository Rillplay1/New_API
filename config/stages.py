import os

stages = {
    "prod": "https://petstore.swagger.io/v2/prod",
    "test": "https://petstore.swagger.io/v2"
}

def get_stage():
    stage_key = os.getenv("STAGE")
    if stage_key not in stages:
        raise ValueError(f"Invalid or missing STAGE env variable: got '{stage_key}'")
    return stages[stage_key]
