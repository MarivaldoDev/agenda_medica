import requests


class ScheduleApiClient:
    BASE_URL = "http://localhost:5000/api"

    @classmethod
    def get_schedules(cls) -> list[dict]:
        response = requests.get(
            f"{cls.BASE_URL}/schedules",
            timeout=5,
        )

        response.raise_for_status()

        return response.json()