class User():

    def __init__(self,name,mis,password):

        self.name = name
        self.mis = mis
        self.password = password

    def __str__(self):
        return f"User ID: {self.id}"
