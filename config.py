from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    load_dotenv=True,
    settings_files=['settings.toml', '.secrets.toml'],
)
