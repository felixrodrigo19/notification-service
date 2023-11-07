import os

from config import settings

if __name__ == "__main__":
    os.environ['ENV'] = "default"
    settings.setenv(os.getenv('ENV'))
