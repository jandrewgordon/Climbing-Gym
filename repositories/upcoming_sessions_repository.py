# from db.run_sql import run_sql
# from models.member import Member
# from models.session import Session
# from models.booking import Booking
# from models.upcoming_session import UpcomingSession

# import repositories.member_repository as member_repository
# import repositories.session_repository as session_repository
# import repositories.booking_repository as booking_repository

# def save(upcoming_session):
#     sql = "INSERT INTO upcoming_sessions (session_name, session_date) VALUES (%s, %s) RETURNING *"
#     values = [upcoming_session.session_name, upcoming_session.session_date]
#     existing_upcoming_sessions = run_sql("SELECT * FROM upcoming_sessions")

#     if existing_upcoming_sessions !=[]:

#         upcoming_session_exists = False

#         for row in existing_upcoming_sessions:

#             if row['session_date'] == upcoming_session.session_date and row['session_name'] == upcoming_session.session_name:
#                 upcoming_session_exists = True
#             else:
#                 upcoming_session_exists = False

#         if upcoming_session_exists == False:
#             results = run_sql(sql, values)
#             id = results[0]['id']
#             upcoming_session.id = id
#         else:
#             print("Upcoming Session already exists")

#     else:
#         results = run_sql(sql, values)
#         id = results[0]['id']
#         upcoming_session.id = id
#         ("I added it OVER HERE anyway")
        

# def select_all():
#     upcoming_sessions = []
#     results = run_sql("SELECT * FROM upcoming_sessions")
#     for row in results:
#         upcoming_session = UpcomingSession(row['session_name'], row['session_date'], row['id'])
#         upcoming_sessions.append(upcoming_session)
#     return upcoming_sessions  

# NOT USING

# def select(id):
#     sql = "SELECT * FROM bookings WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     member = member_repository.select(result['member_id'])
#     session = session_repository.select(result['session_id'])
#     booking_date = result['booking_date']
#     capacity = session.capacity
#     booking = Booking(member, session, booking_date, capacity, id)
#     return booking

# def delete_all():
#     run_sql("DELETE FROM bookings")

# def update_capacity(booking):
#     sql = "UPDATE bookings SET (member_id, session_id, booking_date, capacity) = (%s, %s, %s, %s) WHERE id = %s"
#     booking.capacity -= 1
#     values = [booking.member.id, booking.session.id, booking.booking_date, booking.capacity]
#     run_sql(sql, values)

# def booked_member_list():
#     pass
    
    
    