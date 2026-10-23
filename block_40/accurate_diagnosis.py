class Perfil:
    def __init__(self,name) -> None:
        self.name = name

    def obtain_name(self):
        return self.name

class Thermometer:
	def __init__(self, temperature):
		self.temperature = temperature
	
	def obtain_temperature(self):
		return self.temperature

thermometer_a = Thermometer(23)
print(f'Your temperature is: {thermometer_a.obtain_temperature()}')

class Accountant:
    def __init__(self, value):
        self.value = value

    def incrementar(self):
        value = self.value + 1
        self.value = value

    def show_value(self):
        return self.value


accountant_test = Accountant(5)
sum_accountant = accountant_test.incrementar()
show = accountant_test.show_value()
print(show)