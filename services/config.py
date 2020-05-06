class Config:
    DEBUG = True
    SECRET_KEY = 'secret-key'

class Development(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False
