import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key"
    GITHUB_API_KEY = os.environ.get("GITHUB_API_KEY")
    RESEND_API_KEY = os.environ.get("RESEND_API_KEY")

    MAIL_RECIPIENT = "name@example.com"
