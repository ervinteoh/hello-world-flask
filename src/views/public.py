from flask import Blueprint, render_template

blueprint = Blueprint("public", __name__)


@blueprint.route("/home")
@blueprint.route("/")
def home():
    return render_template("pages/home.jinja")


@blueprint.route("/about")
def about():
    return render_template("pages/about.jinja")
