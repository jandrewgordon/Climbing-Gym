from flask import Flask, render_template, redirect, request, Blueprint
from models.upcoming_session import UpcomingSession
import repositories.upcoming_sessions_repository as upcoming_session_repository

upcoming_sessions_blueprint = Blueprint("upcoming_sessions", __name__)

@upcoming_sessions_blueprint.route("/upcoming_sessions/<id>")
def show_upcoming_session(id):
    selected_upcoming_session = upcoming_session_repository.select(id)
    return render_template("upcoming_sessions/show.html", upcoming_session = selected_upcoming_session)