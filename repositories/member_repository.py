from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members(last_name, first_name, premium, bookings) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.last_name, member.first_name, member.premium, member.bookings]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    run_sql("DELETE FROM members")