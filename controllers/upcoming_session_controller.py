from flask import Flask, render_template, redirect, request, Blueprint
from models.upcoming_session import UpcomingSession
import repositories.upcoming_sessions_repository as upcoming_session_repository
import repositories.upcoming_sessions_members_repository as upcoming_sessions_member_repository

upcoming_sessions_blueprint = Blueprint("upcoming_sessions", __name__)

@upcoming_sessions_blueprint.route("/upcoming_sessions/<id>")
def show_upcoming_session(id):
    selected_upcoming_session = upcoming_session_repository.select(id)
    all_booked_members = upcoming_sessions_member_repository.select_all_booked_members(id)
    for member in all_booked_members:
        print(member.last_name)
    return render_template("upcoming_sessions/show.html", upcoming_session = selected_upcoming_session, all_booked_members = all_booked_members)