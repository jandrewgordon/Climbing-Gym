from db.run_sql import run_sql
from models.session import Session

def save(session):
    sql = "INSERT INTO sessions(name, capacity, premium) VALUES (%s, %s, %s) RETURNING *"
    values = [session.name, session.capacity, session.premium]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    results = run_sql("SELECT * FROM sessions")
    for row in results:
        session = Session(row['name'], row['capacity'], row['premium'], row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    run_sql("DELETE FROM sessions")

    