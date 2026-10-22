class Thermostat:
    def __init__(self, temperature) -> None:
        if temperature < 10 or temperature > 30:
            raise ValueError("ERROR: Temperature is not valid")

        self.temperature = temperature

    def increase(self, grades):
        new_temperature = self.temperature + grades

        if new_temperature > 30:
            raise ValueError("ERROR: Temperature is not valid")

        self.temperature = new_temperature

    def reduce(self, grades):
        new_temperature = self.temperature - grades

        if new_temperature < 10:
            raise ValueError("ERROR: Temperature is not valid")

        self.temperature = new_temperature

    def current_temperature(self):
        return self.temperature


temperature = Thermostat(11)

temperature.increase(10)
temperature.reduce(2)

print(temperature.current_temperature())