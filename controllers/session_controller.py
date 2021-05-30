from flask import Flask, render_template, redirect, request, Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", all_sessions = sessions)

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


    
