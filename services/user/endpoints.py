from config.stages import get_stage

class Endpoints:
    get_user_by_username = lambda self, username: f"{get_stage()}/user/{username}"


