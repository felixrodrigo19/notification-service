from celery import Celery

from config import settings


class TaskManager:
    def __init__(self):
        self._redis_url = f"redis://{settings.get('REDIS_HOST')}:{settings.get('REDIS_PORT')}"
        self.task_manager = None

    @property
    def redis_url(self) -> str:
        return self._redis_url

    @redis_url.setter
    def redis_url(self, new_url: str):
        self._redis_url = new_url

    def setup_task_manager(self):
        self.task_manager = Celery(
            main=settings.get('APP_NAME'),
            broker=self._redis_url,
            include=[]  # todo: replace list to include project tasks modules
        )

        self.task_manager.conf.update(
            result_backend=f'{self._redis_url}/0',
        )
