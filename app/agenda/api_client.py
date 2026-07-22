import requests
from flask import current_app


class ScheduleApiClient:
    @classmethod
    def get_schedules(cls) -> list[dict]:
        base_url = current_app.config.get("API_BASE_URL", "http://127.0.0.1:5000/api")

        try:
            response = requests.get(f"{base_url}/schedules", timeout=5)
            response.raise_for_status()

            data = response.json()
            if not isinstance(data, list):
                current_app.logger.warning("API retornou formato inválido")
                return []

            return data
        except requests.Timeout:
            current_app.logger.exception("Timeout ao consultar agendamentos")
            return []
        except requests.RequestException:
            current_app.logger.exception("Falha ao consultar agendamentos")
            return []
        except ValueError:
            current_app.logger.exception("JSON inválido na resposta de agendamentos")
            return []
