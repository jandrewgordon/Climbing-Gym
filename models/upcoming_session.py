class UpcomingSession:

    def __init__(self, session_name, session_date, remaining_capacity, member, id=None):
        self.session_name = session_name
        self.session_date = session_date
        self.remaining_capacity = remaining_capacity
        self.member = member
        self.id = id