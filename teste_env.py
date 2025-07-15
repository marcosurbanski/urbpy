from decouple import config
from distutils.util import strtobool

print("Raw value from .env:", config("COLLECTFAST_ENABLED", default="not found"))
print("Parsed bool value   :", config("COLLECTFAST_ENABLED", cast=lambda v: bool(strtobool(v)), default=False))
