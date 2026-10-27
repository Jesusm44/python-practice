class States:
    def __init__(self) -> None:
        self.state = False

    def __enter__(self):
        self.state = True
        return self

    def __exit__(self, exc_type, exc, tb):
        self.state = False

    def __str__(self) -> str:
        if self.state == True:
            return f'{self.state} state'
        else:
            return f'{self.state} state'

state = States()

with state as file:
    if state.state == False:
        raise ValueError("The state was not activated.")
