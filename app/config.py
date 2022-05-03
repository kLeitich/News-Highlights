from flask import Flask
from .config import DevConfig

class Config:
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True