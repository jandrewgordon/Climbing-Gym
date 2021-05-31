from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id, booking_date) VALUES (%s, %s, %s) RETURNING *"
    values = [booking.member.id, booking.session.id, booking.booking_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select_all():
    bookings = []
    results = run_sql("SELECT * FROM bookings")
    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking_date = row['booking_date']
        booking = Booking(member, session, booking_date, row['id'])
        bookings.append(booking)
    return bookings   

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result['member_id'])
    session = session_repository.select(result['session_id'])
    booking_date = result['booking_date']
    booking = Booking(member, session, booking_date, id)
    return booking

def delete_all():
    run_sql("DELETE FROM bookings")