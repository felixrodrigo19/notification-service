import os

from config import settings
from tasks.task_manager import TaskManager

if __name__ == "__main__":
    os.environ['ENV'] = "default"
    settings.setenv(os.getenv('ENV'))

    task_manager = TaskManager()
    task_manager.setup_task_manager()
