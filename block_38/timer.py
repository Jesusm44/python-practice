import datetime

class Timer:
    def __init__(self,time) -> None:
        parts = time.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        
        timer = datetime.timedelta(
            minutes=minutes,
            seconds=seconds
        )
        
        self.time = timer

    def consult_time(self):
        return self.time

    def change_time(self,new_time):
        parts = new_time.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])

        time_changed = datetime.timedelta(
            minutes=minutes,
            seconds=seconds
        )

        self.time = time_changed

timer_a = Timer("17:52")
before_change_time = timer_a.consult_time()
timer_a.change_time("17:48")
after_change_time = timer_a.consult_time()
