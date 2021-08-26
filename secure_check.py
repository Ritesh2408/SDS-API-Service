from user import User

users = [ User('Jose',1234,'mypassword'),
          User('Mimi',45647,'secret')]

username_table = {u.name: u for u in users}
userid_table = {u.mis: u for u in users}


def authenticate(name, password):
    user = name_table.get(name, None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
