import datetime

class Booking:
    def __init__(self, user, hour) -> None:
        parts = hour.split(":")
        hour = int(parts[0])
        minutes = int(parts[1])

        reservation_time = datetime.time(hour,minutes)

        self.user = user
        self.hour = reservation_time

    @staticmethod
    def show_reservation(user,hour):
        if not isinstance(user, str):
            raise ValueError
        
        if not user.strip():
            raise ValueError

        user = user.strip()

        if len(user) < 3:
            raise ValueError
        
        print(f'Hello {user}, your reservation {hour} has been successfully scheduled.')


user_reservation = Booking(
    user="Maria",
    hour="00:00"
)
user_reservation.show_reservation(
    user=user_reservation.user,
    hour=user_reservation.hour 
)