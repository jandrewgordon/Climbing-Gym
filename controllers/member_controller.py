from flask import Flask, render_template, redirect, request, Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", all_members = members)

@members_blueprint.route("/members/new", methods=['GET'])
def get_new_member():
    return render_template("members/new.html")


@members_blueprint.route("/members", methods=['POST'])
def create_new_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    premium = request.form.get("premium")
    if premium:
        print("We laughing")
        premium = True
    else:
        print("gubbed")
        premium = False
    bookings = 0
    new_member = Member(last_name, first_name, premium, bookings)
    member_repository.save(new_member)
    return redirect("/members")


    
