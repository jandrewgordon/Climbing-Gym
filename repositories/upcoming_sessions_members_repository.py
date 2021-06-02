from db.run_sql import run_sql
from models.member import Member
from models.upcoming_session import UpcomingSession

import repositories.member_repository as member_repository
import repositories.upcoming_sessions_repository as upcoming_sessions_repository

def save(upcoming_sessions_member):
    sql = "INSERT INTO upcoming_sessions_members(upcoming_session_id, member_id) VALUES (%s, %s) RETURNING *"
    values = [upcoming_sessions_member.upcoming_session.id, upcoming_sessions_member.member.id]
    
    # Check is there is space in the upcoming session
    upcoming_session = upcoming_sessions_member.upcoming_session
    print(upcoming_session.remaining_capacity)
    if upcoming_session.remaining_capacity > 0:
        results = run_sql(sql, values)
        upcoming_sessions_member.id = results[0]['id']
        upcoming_sessions_repository.update_capacity(upcoming_session)
    else:
        print("Upcoming Session Full")  
    
    

def select_all_booked_members(id):
    all_booked_member_ids = []
    results = run_sql("SELECT * FROM upcoming_sessions_members")
    for row in results:
        if int(row['upcoming_session_id']) == int(id):
            all_booked_member_ids.append(row['member_id'])
    all_booked_members = []
    for member_id in all_booked_member_ids:
        found_member = member_repository.select(member_id)
        all_booked_members.append(found_member)
    return all_booked_members

    
