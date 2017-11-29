"""Contains classes to generate session id and to create a session user"""

import os
from flask import session
class Base:
    "Used to generate session_id"

    def generate_session_id(self, session_key):
        """returns a randomly generated session_id if not in session already
        Random no one guesses it :-)"""
        session_id = str(os.urandom(10))
        while session_id in session[session_key]:
            session_id = str(os.urandom(10))

        return session_id

class SessionUser(Base):
    "Stores the user object during a session"
   
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.id = self.generate_session_id("users")