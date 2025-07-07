from config.stages import get_stage

class Endpoints:
    create_user = f"{get_stage()}/pet"

