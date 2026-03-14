from flask import Blueprint, render_template

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
    return render_template("about.html")

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
