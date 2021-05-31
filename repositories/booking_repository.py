from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']

def select_all():
    bookings = []

    results = run_sql("SELECT * FROM bookings")
    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(member, session, row['id'])
        bookings.append(booking)
    return bookings   

def delete_all():
    run_sql("DELETE FROM bookings")