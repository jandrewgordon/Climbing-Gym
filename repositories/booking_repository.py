from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id, booking_date, capacity) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [booking.member.id, booking.session.id, booking.booking_date, booking.session.capacity]
    existing_bookings = run_sql("SELECT * FROM bookings")
    
    if existing_bookings != []:
        
        booking_exists = False

        for row in existing_bookings:
            
            if row['booking_date'] == booking.booking_date and row['member_id'] == booking.member.id:
                booking_exists = True
                break
            else:
                booking_exists = False
                

        if booking_exists == False:
            results = run_sql(sql, values)
            id = results[0]['id']
            booking.id = id
            
        else:
            pass     
    
    else:
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
        capacity = session.capacity
        booking = Booking(member, session, booking_date, capacity, row['id'])
        bookings.append(booking)
    return bookings   

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result['member_id'])
    session = session_repository.select(result['session_id'])
    booking_date = result['booking_date']
    capacity = session.capacity
    booking = Booking(member, session, booking_date, capacity, id)
    return booking

def delete_all():
    run_sql("DELETE FROM bookings")

# def update_capacity(booking):
#     sql = "UPDATE upcoming_sessions SET (member_id, session_id, booking_date, capacity) = (%s, %s, %s, %s) WHERE id = %s"
#     booking.capacity -= 1
#     values = [booking.member.id, booking.session.id, booking.booking_date, booking.capacity]
#     run_sql(sql, values)

def booked_member_list():
    pass
    
    
    