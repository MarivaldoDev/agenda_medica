from app.agenda.api_client import ScheduleApiClient


class ScheduleService:

    @staticmethod
    def list_schedules():
        return ScheduleApiClient.get_schedules()