from app.agenda.api_client import ScheduleApiClient


class ScheduleService:
    @staticmethod
    def list_schedules():
        try:
            schedules = ScheduleApiClient.get_schedules()
            return {
                "schedules": schedules,
                "has_schedules": bool(schedules),
                "error": None,
            }
        except Exception:
            return {
                "schedules": [],
                "has_schedules": False,
                "error": "Não foi possível carregar os agendamentos no momento.",
            }