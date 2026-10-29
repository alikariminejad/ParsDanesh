from .base import *
import environ

DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS')