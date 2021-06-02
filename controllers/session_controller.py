from flask import Flask, render_template, redirect, request, Blueprint
from models.session import Session
import repositories.session_repository as session_repository
import repositories.upcoming_sessions_repository as upcoming_sessions_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", all_sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show_session(id):
    session = session_repository.select(id)
    return render_template("sessions/show.html", session = session)

@sessions_blueprint.route("/sessions/new", methods=['GET'])
def get_new_session():
    return render_template("sessions/new.html")


@sessions_blueprint.route("/sessions", methods=['POST'])
def create_new_session():
    name = request.form['name']
    capacity = int(request.form['capacity'])
    premium = request.form.get("premium")
    if premium:
        print("We laughing")
        premium = True
    else:
        print("gubbed")
        premium = False
    new_session = Session(name, capacity, premium)
    session_repository.save(new_session)
    return redirect("/sessions")

# Edit
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template("sessions/edit.html", session=session)

# Update
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    capacity = request.form["capacity"]
    premium = request.form.get("premium")
    if premium:
        premium = True
    else:
        premium = False
    print(name)
    print(premium)
    session = Session(name, capacity, premium, id)  
    session_repository.update(session)
    # upcoming_sessions_repository.update_upcoming_session_name(session)
    return redirect("/sessions")
    
