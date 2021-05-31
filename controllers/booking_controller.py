from flask import Flask, render_template, redirect, request, Blueprint
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", all_bookings = bookings)

# NEW
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def get_new_booking():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", members=members, sessions=sessions)

# CREATE
@bookings_blueprint.route("/bookings", methods=['POST'])
def create_new_booking():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    new_booking = Booking(member, session)
    booking_repository.save(new_booking)
    return redirect("/bookings")

#EDIT
#UPDATE

@bookings_blueprint.route("/bookings/<id>")
def show_booking():
    pass

# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")




    
