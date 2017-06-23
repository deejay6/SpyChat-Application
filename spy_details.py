from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating, spy_is_online, current_status_message, old_status, friend_list):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = spy_is_online
        self.current_status_message = current_status_message
        self.old_status = old_status
        self.friend_list = friend_list

class Friend:

    def __init__(self, name, salutation, age, rating, spy_is_online, chats):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = spy_is_online
        self.chats = chats


spy_list = []


class Chat:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me