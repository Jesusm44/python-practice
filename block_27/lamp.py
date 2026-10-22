class Lamp:
    def __init__(self) -> None:
        self.lamp = False

    def turn_on_the_lamp(self,turn_on):
        if turn_on == "on":
            self.lamp = True

    def turn_off_lamp(self, turn_off):
        if turn_off == "off":
            self.lamp = False


    def show_state(self):
        print(f"State of the lamp is: {self.lamp}")

lamp = Lamp()
show_lamp = lamp.show_state()

turn_on = lamp.turn_on_the_lamp("on")
show_lamp = lamp.show_state()

turn_off = lamp.turn_off_lamp("off")
show_lamp = lamp.show_state()