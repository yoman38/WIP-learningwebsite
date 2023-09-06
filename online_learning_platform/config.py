"""config.py"""

from typing import Tuple

class Config:
    """Configuration settings for the Online Learning Platform application."""

    def __init__(self,
                 SECRET_KEY: str = 'secret_key',
                 SQLALCHEMY_DATABASE_URI: str = 'sqlite:///site.db',
                 SQLALCHEMY_TRACK_MODIFICATIONS: bool = False,
                 CKEDITOR_PKG_TYPE: str = 'standard',
                 CKEDITOR_LANGUAGE: str = 'en',
                 CKEDITOR_HEIGHT: int = 400,
                 CKEDITOR_WIDTH: int = 600,
                 CKEDITOR_FILE_UPLOADER: str = 'upload',
                 CKEDITOR_FILE_BROWSER: str = 'browse',
                 BOOTSTRAP_SERVE_LOCAL: bool = True,
                 BOOTSTRAP_USE_MINIFIED: bool = True,
                 BOOTSTRAP_JQUERY_VERSION: Tuple[int, int, int] = (3, 4, 1)):

        self.SECRET_KEY = SECRET_KEY
        self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
        self.SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
        self.CKEDITOR_PKG_TYPE = CKEDITOR_PKG_TYPE
        self.CKEDITOR_LANGUAGE = CKEDITOR_LANGUAGE
        self.CKEDITOR_HEIGHT = CKEDITOR_HEIGHT
        self.CKEDITOR_WIDTH = CKEDITOR_WIDTH
        self.CKEDITOR_FILE_UPLOADER = CKEDITOR_FILE_UPLOADER
        self.CKEDITOR_FILE_BROWSER = CKEDITOR_FILE_BROWSER
        self.BOOTSTRAP_SERVE_LOCAL = BOOTSTRAP_SERVE_LOCAL
        self.BOOTSTRAP_USE_MINIFIED = BOOTSTRAP_USE_MINIFIED
        self.BOOTSTRAP_JQUERY_VERSION = BOOTSTRAP_JQUERY_VERSION
