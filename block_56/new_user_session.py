class NewUser:
    server = "LATAM"

    def __init__(self,user, password, ip,session_id) -> None:
        self.user = user
        self.password = password
        self.ip = ip
        self.sessions_id = session_id 
        self.state_session = False
        self.create_session = False

    def __enter__(self):
        self.state_session = True
        self.create_session = True
        return self

    def __exit__(self, exc_type, exc, tb):
        self.state_session = False
        self.create_session = True
        return None

    def __eq__(self, other) :
        if not isinstance(other, NewUser):
            return NotImplemented
        
        return (self.sessions_id == other.sessions_id)

    def __str__(self)  -> str:
        if self.create_session:
            if self.state_session:
                return f"welcome {self.user}"
            else:
                return f"The session is not started"
        else:
            return f"The session has not been created."

    def __repr__(self) -> str:
        return f"NewUser=(user={self.user!r}, session_id={self.sessions_id!r}, state={self.state_session!r}, create={self.create_session!r}, ip={self.ip!r}, server={self.server!r})"


new_user = NewUser("Tataduty", 52789, "100.10.95", "S001")

print(new_user)
with new_user as file:
    if not new_user.create_session:
        if not new_user.state_session:
            raise ValueError
    print(file)
print(file)