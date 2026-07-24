from flask import render_template, jsonify, flash, redirect, url_for, current_app
from app.main.forms import ContactForm
from app.main import bp
from app.services.github_api import get_repos
from app.email import send_email


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/about_me", methods=["GET"])
def about_me():
    return render_template("about_me.html", title="Über mich")


@bp.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html", title="Projekte")


@bp.route("/api/github")
def github_api():

    repos = get_repos()

    return jsonify(repos)


@bp.route("/contact", methods=["GET", "POST"])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        try:
            send_email(
                name=form.name.data,
                email=form.email.data,
                subject=form.subject.data,
                message=form.message.data,
            )

        except Exception as err:
            current_app.logger.exception(f"Contact Form Error: {err}")

            flash(
                "Beim Versenden Ihrer Nachricht ist ein Fehler aufgetreten. Bitte versuchen Sie es später nochmal.",
                "danger",
            )

        else:

            flash("Ihre Nachricht wurde versendet.", "success")

        return redirect(url_for("main.contact"))

    return render_template("contact.html", title="Kontakt", form=form)


@bp.route("/data_privacy", methods=["GET"])
def data_privacy():
    return render_template("data_privacy.html", title="Datenschutzerklärung")


@bp.route("/legal", methods=["GET"])
def legal():
    return render_template("legal.html", title="Impressum")
