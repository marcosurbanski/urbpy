import os
from decouple import config
from distutils.util import strtobool

print("=== OS ENV ===")
print("os.environ.get('COLLECTFAST_ENABLED') =", os.environ.get('COLLECTFAST_ENABLED'))

print("=== decouple ===")
print("config raw =", config("COLLECTFAST_ENABLED", default="not found"))
print("config parsed =", config("COLLECTFAST_ENABLED", cast=lambda v: bool(strtobool(v)), default=False))
