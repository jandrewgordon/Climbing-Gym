from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members(last_name, first_name, premium, bookings) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.last_name, member.first_name, member.premium, member.bookings]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result['last_name'], result['first_name'], result['premium'], result['bookings'], result['id'])
    return member

def select_all():
    members = []

    results = run_sql("SELECT * FROM members")
    for row in results:
        member = Member(row['last_name'], row['first_name'], row['premium'], row['bookings'], row['id'])
        members.append(member)
    return members

   

def delete_all():
    run_sql("DELETE FROM members")