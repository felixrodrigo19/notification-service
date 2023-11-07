import os

from dynaconf import settings

if __name__ == "__main__":
    os.environ['ENV'] = "development"

    settings.setenv(os.getenv('ENV'))
