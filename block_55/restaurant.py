class AnonymousClub:
    membership = "standard"

    def __init__(self,booking,account,device,document) -> None:
        self.booking = booking
        self.account = account
        self.device = device
        self.document = document
        self.tasks = []

    def __str__(self) -> str:
        return f"welcome {self.account} yours tasks are: {self.tasks}, Your current membership is {self.membership} Do more tasks for a better membership"

    def __repr__(self) -> str:
        return f"AnonymousClub:(membership={self.membership!r}, bookinf={self.booking!r}, account={self.account!r}, device={self.device!r}, document={self.document!r},task={self.tasks!r})"

user_a = AnonymousClub("Today", "Juans", "Iphone", "A12345")
user_a.tasks.append("searcseek followers")

user_b = AnonymousClub("Tomorrow", "Marias", "Iphone", "A12346")
user_b.tasks.append("searcseek followers")

user_c = AnonymousClub("two days", "Marcos", "Iphone 17", "A12343")
user_c.membership = "Master"
user_c.tasks.append("The teacher has no tasks.")

print(user_a.membership is user_b.membership is not user_c.membership)
print(len(user_a.tasks) == len(user_b.tasks))
print(user_a.account is not user_c.account)
print(user_a.account == user_c.account)