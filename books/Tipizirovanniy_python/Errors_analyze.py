from dataclasses import dataclass
import datetime

@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None

def check_what(user):
    print(user.username, user.created_at, user.birthday)
def check_wh(_): pass
def validate_user(user: User) -> None:
    check_what(user)
    check_wh(user)

user = User("string", datetime.datetime.now())
validate_user(user)

