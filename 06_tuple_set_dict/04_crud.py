# CRUD: Create Read Upate Delete
from turtle import update


users = [
    {"id": 1, "first_name": "Simone", "last_name": "Cranson", "email": "scranson0@mapy.cz"},
    {"id": 2, "first_name": "Merrielle", "last_name": "Troctor", "email": "mtroctor1@cam.ac.uk"},
    {"id": 3, "first_name": "Randall", "last_name": "Smithend", "email": "rsmithend2@usa.gov"},
    {"id": 4, "first_name": "Abner", "last_name": "Southwick", "email": "asouthwick3@godaddy.com"},
    {"id": 5, "first_name": "Sibyl", "last_name": "Schwartz", "email": "sschwartz4@geocities.jp"},
    {"id": 6, "first_name": "Casie", "last_name": "Kitlee", "email": "ckitlee5@gov.uk"},
    {"id": 7, "first_name": "Hugo", "last_name": "Such", "email": "hsuch6@omniture.com"},
    {"id": 8, "first_name": "Debor", "last_name": "Musker", "email": "dmusker7@opera.com"},
    {"id": 9, "first_name": "Brennen", "last_name": "Killingworth", "email": "bkillingworth8@hugedomains.com"},
    {"id": 10, "first_name": "Doralynn", "last_name": "Brigshaw", "email": "dbrigshaw9@163.com"},
]


def fetch_users():
    return users


def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    # return None


def create_user(create_payload):
    users.append(create_payload)
    return users[-1]


def update_user(user_id, update_payload):
    user = find_user(user_id)
    if user is not None:
        index = users.index(user)
        users[index].update(update_payload)
        return users[index]


def remove_user(user_id):
    user = find_user(user_id)
    users.remove(user)


print(find_user(100))
print(create_user({"id": 11, "first_name": "Doralynn", "last_name": "Brigshaw", "email": "dbrigshaw9@163.com"}))
print(update_user(11, {"first_name": "SMITH"}))
remove_user(1)
print(find_user(1))
