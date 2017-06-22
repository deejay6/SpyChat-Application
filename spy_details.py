class Spy:

    def __init__(self, name, salutation, age, rating, spy_is_online, current_status_message, old_status, chats):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = spy_is_online
        self.current_status_message = current_status_message
        self.old_status = old_status

class Friend:

    def __init__(self, name, salutation, age, rating, friend_is_online, friend_of):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.friend_is_online = friend_is_online
        self.friend_of = friend_of
spy_list = []
friend_list = []