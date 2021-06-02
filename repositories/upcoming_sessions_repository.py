from db.run_sql import run_sql
from models.member import Member
from models.session import Session
from models.booking import Booking
from models.upcoming_session import UpcomingSession

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

def save(upcoming_session):
    sql = "INSERT INTO upcoming_sessions(session_name, session_date, remaining_capacity, member_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [upcoming_session.session_name, upcoming_session.session_date, upcoming_session.remaining_capacity, upcoming_session.member.id]
    existing_upcoming_sessions = run_sql("SELECT * FROM upcoming_sessions")

    if existing_upcoming_sessions != []:
        upcoming_session_exists = False

        for row in existing_upcoming_sessions:
            
            if row['session_name'] == upcoming_session.session_name and row['session_date'] == upcoming_session.session_date:
                upcoming_session_exists = True
                break
            else:
                upcoming_session_exists = False

        if upcoming_session_exists == False:
            results = run_sql(sql, values)
            id = results[0]['id']
            upcoming_session.id = id
        else:
            pass
    else:
        results = run_sql(sql, values)
        id = results[0]['id']
        upcoming_session.id = id
            


def select_all():
    upcoming_sessions = []
    results = run_sql("SELECT * FROM upcoming_sessions")
    for row in results:
        member = member_repository.select(row['member_id'])
        upcoming_session = UpcomingSession(row['session_name'], row['session_date'], row['remaining_capacity'], member, row['id'])
        upcoming_sessions.append(upcoming_session)
    return upcoming_sessions  

def select(id):
    sql = "SELECT * FROM upcoming_sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    session_name = result['session_name']
    session_date = result['session_date']
    remaining_capacity = result['remaining_capacity']
    member = member_repository.select(result['member_id'])
    upcoming_session = UpcomingSession(session_name, session_date, remaining_capacity, member, id)
    return upcoming_session
    
# def get_length():
#     database_as_list = select_all()
#     database_length = len(database_as_list)
#     return database_length

def get_id(session_name, session_date):
    all_entries = run_sql("SELECT * FROM upcoming_sessions")
    for row in all_entries:
        if row['session_name'] == session_name and row['session_date'] == session_date:
            return row['id']



# def delete_all():
#     run_sql("DELETE FROM bookings")

# def update_capacity(booking):
#     sql = "UPDATE bookings SET (member_id, session_id, booking_date, capacity) = (%s, %s, %s, %s) WHERE id = %s"
#     booking.capacity -= 1
#     values = [booking.member.id, booking.session.id, booking.booking_date, booking.capacity]
#     run_sql(sql, values)

# def booked_member_list():
#     pass
    
    
    