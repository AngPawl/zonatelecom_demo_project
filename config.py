import os
from typing import Literal
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(__file__)


class Config(BaseSettings):
    login: str
    password: str
    browser_url: str
    context: Literal['local', 'remote'] = 'local'
    browser_name: Literal['chrome', 'firefox'] = 'chrome'
    base_url: str = "https://www.zonatelecom.ru/"
    window_width: int = 1366
    window_height: int = 768


config = Config(_env_file=os.path.join(BASE_DIR, '.env'))
