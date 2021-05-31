class Booking:

    def __init__(self, member, session, booking_date, id=None):
        self.member = member
        self.session = session
        self.booking_date = booking_date
        self.id = id
