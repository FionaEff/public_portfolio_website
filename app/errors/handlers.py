from flask import render_template, flash, redirect, url_for
from flask_limiter import RateLimitExceeded
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(RateLimitExceeded)
def rate_limit_error(error):

    flash(
        "Sie haben zu viele Nachrichten gesendet. Bitte versuchen Sie es später noch einmal.",
        "error",
    )

    return redirect(url_for("main.contact"))
