import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()


member1 = Member("Bloggs", "Joe", True, 0)
member_repository.save(member1)

session1 = Session("Beginner Lesson", 15, False)
session_repository.save(session1)

booking1 = Booking(member1, session1, "hhhahs")
booking_repository.save(booking1)

pdb.set_trace()