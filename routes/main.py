from flask import Blueprint, render_template, url_for, send_from_directory, abort
import os 

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/services")
def services():
    return render_template("services.html")


@main.route("/solutions")
def solutions():
    return render_template("solutions.html")


@main.route("/how")
def how():
    return render_template("how.html")


@main.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Us",
        description="Learn about the mission, vision, and leadership of Prosperity System Hub.",
        og_image=url_for("static", filename="img/logo.png", _external=True),
    )


@main.route("/team_leadership")
def team_leadership():
    return render_template("team_leadership.html")


@main.route("/privacy")
def privacy():
    return render_template("privacy.html")


@main.route("/security")
def security():
    return render_template("security.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/teams")
def teams():
    return render_template("teams.html")


@main.route("/mission_vision")
def mission_vision():
    return render_template("mission_vision.html")


@main.route("/briefing")
def briefing():
    return render_template("briefing.html")


@main.route("/careers")
def careers():
    return render_template("careers.html")


@main.route("/overview")
def overview():
    return render_template("overview.html")


@main.route("/platform")
def platform():
    return render_template("platform.html")

@main.route('/robots.txt')
def serve_robots():
    """Serve robots.txt from root directory"""
    try:
        return send_from_directory(os.getcwd(), 'robots.txt')
    except FileNotFoundError:
        abort(404)

@main.route('/sitemap.xml')
def serve_sitemap():
    """Serve sitemap.xml from root directory"""
    try:
        return send_from_directory(os.getcwd(), 'sitemap.xml')
    except FileNotFoundError:
        abort(404)

# Error handlers
@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500