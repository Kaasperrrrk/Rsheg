import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6954456583:AAE5bftP766kUNu-Uwj_bWvlyuNgrW6VGpA")

    APP_ID = int(os.environ.get("APP_ID", 24540294))

    API_HASH = os.environ.get("API_HASH", "bf5c97a35179d634949ceda43533bd89")
