
import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:

    # ==========================================================
    # FLASK
    # ==========================================================

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "book_store_secret_key"
    )

    # ==========================================================
    # DATABASE
    # ==========================================================

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///"
        + os.path.join(BASE_DIR, "bookstore.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================================================
    # GMAIL
    # ==========================================================

    MAIL_SERVER = os.getenv(
        "MAIL_SERVER",
        "smtp.gmail.com"
    )

    MAIL_PORT = int(
        os.getenv("MAIL_PORT", "587")
    )

    MAIL_USE_TLS = (
        os.getenv("MAIL_USE_TLS", "True").lower()
        == "true"
    )

    MAIL_USERNAME = os.getenv(
        "MAIL_USERNAME"
    )

    MAIL_PASSWORD = os.getenv(
        "MAIL_PASSWORD"
    )


