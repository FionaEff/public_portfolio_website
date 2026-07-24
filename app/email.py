from flask import render_template, current_app
from config import Config
import resend


def send_email(name, email, subject, message):

    resend.api_key = Config.RESEND_API_KEY

    html = render_template(
        "email/email.html", name=name, email=email, subject=subject, message=message
    )

    text = render_template(
        "email/email.txt", name=name, email=email, subject=subject, message=message
    )

    try:
        resend.Emails.send(
            {
                "from": "Kontaktformular <kontakt@fiona-eff.dev>",
                "to": Config.MAIL_RECIPIENT,
                "subject": subject,
                "reply_to": email,
                "html": html,
                "text": text,
            }
        )

    except Exception as err:
        current_app.logger.exception(err)
        print(type(err))
