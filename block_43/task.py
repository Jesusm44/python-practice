def input_task()  :
    task_name = input("Enter your task: ").strip().capitalize()
    task_state = False

    return task_name, task_state
    
def validation_task() :
    task_name, task_state = input_task()

    if not isinstance(task_name, str):
        raise TypeError("ERROR: Name is not a word.")
    if not task_name.strip():
        raise ValueError("ERROR: Empty name.")
    if len(task_name.strip()) < 3:
        raise ValueError("ERROR: The name cannot have fewer than 3 letters.")

    task= {
        "name": task_name,
        "task_state": task_state
    }

    return task

class Task:
    def __init__(self,name,task_state):
        self.name = name
        self.task_state = task_state

    def show_task(self):
        print (f"""
Name : {self.name}
task_state: {self.task_state}""")

    def change_state(self, new_state):
        if not isinstance(new_state, bool):
            raise TypeError("The state does not indicate whether it is true or false.")
        if self.task_state == False:
            self.task_state = new_state
        else:
            raise ValueError("The task status cannot be changed.")
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def change_name(self, new_name):
        if not(isinstance(new_name,str) and new_name.strip() and not len(new_name.strip()) < 3): 
            raise ValueError("ERROR: Name not is valid")

        self.name = new_name

validation_task_1 = validation_task()

conver_task_1 = Task.from_dict(validation_task_1)

conver_task_1.show_task()
conver_task_1.change_state(True)
conver_task_1.show_task()