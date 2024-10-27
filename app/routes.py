from flask import render_template, request, redirect, url_for, flash
from . import app
from .models import URL
from .utils import generate_short_code

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["original_url"]
        short_code = generate_short_code()
        URL.create(original_url, short_code)
        return render_template("index.html", short_url=request.host_url + short_code)
    return render_template("index.html")

@app.route("/<short_code>")
def redirect_to_url(short_code):
    url_entry = URL.find_by_code(short_code)
    if url_entry:
        return redirect(url_entry["original_url"])
    flash("Invalid URL")
    return redirect(url_for("index"))
