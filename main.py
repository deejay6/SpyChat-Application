from spy_details import Spy, Friend, spy_list, Chat
import time
from termcolor import colored
import random

random_number = random.randint(1, 10)

# global variables

store = []
values = []
encryption_key = 0
s = []
some_special_words = {
    'SOS': "Help me out !!",
    'ILU': "I LOVE YOU ",
    'OMW': "ON MY WAY"
}


def add_friend(login_name):
    while True:
        name = raw_input('Hey What\'s Your Friend\'s Name !!!?? : ')
        if name.isalpha() == True and len(name) > 0:
            break
        else:
            print 'Please Enter Valid Name'
    while True:
        salutation = raw_input('Should I Call Your Friend Mister or Miss?? : ')
        if salutation == "Mister" or salutation == "Miss":
            break
        else:
            print "Please Enter Valid Salutation"
    while True:
        age = raw_input("What\'s Your Friend's Age :? : ")
        try:
            age = int(age)
            break
        except:
            print 'Please Enter Valid Age'
    age = int(age)
    if (age > 12) and (age < 50):
        while True:
            rating = raw_input("What\'s Your Friend's Rating?? : ")
            try:
                rating = float(rating)
                break
            except:
                print 'Please Enter Valid Rating'
        rating = float(rating)
        friend_is_online = True
        for i in range(0, len(spy_list)):
            if spy_list[i].name == login_name:
                spy_list[i].friend_list.append(Friend(name, salutation, age, rating, friend_is_online, []))
                for j in range(0, len(spy_list[i].friend_list)):
                    print "%s %s " % (spy_list[i].friend_list[j].name, spy_list[i].friend_list[j].chats)

    else:
        print 'Sorry you are not of the correct age to be a friend'


def add_status(login_name):
    for i in range(0, len(spy_list)):
        if spy_list[i].name == login_name:
            if not spy_list[i].old_status:
                while True:
                    status_message = raw_input("Enter Your Status Message: ")
                    if len(status_message) > 0:
                        break
                    else:
                        print "Message can't be kept blank"
                spy_list[i].old_status.append(status_message)
                spy_list[i].current_status_message = status_message
                print "Your current status message is: " + spy_list[i].current_status_message
            else:
                print "Your Old Status Messages Are:"
                status_number = 1
                for j in range(0, len(spy_list[i].old_status)):
                    print '%d %s' % (status_number, spy_list[i].old_status[j])
                    status_number = status_number + 1
                ch = raw_input("Do you want to add new Status(Y/N):")
                if ch.upper() == "Y":
                    while True:
                        status_message = raw_input("Enter Your Status Message: ")
                        if len(status_message) > 0:
                            break
                        else:
                            print "Mesage can't be kept blank"
                    spy_list[i].old_status.append(status_message)
                    print spy_list[i].old_status
                    spy_list[i].current_status_message = status_message
                    print spy_list[i].current_status_message
                    print spy_list[i]
                elif ch.upper() == "N":
                    while True:
                        index = raw_input("Please Select Your Status From Above Menu: ")
                        if len(index) > 1:
                            print 'Please Enter Valid Option'
                        else:
                            try:
                                index = int(index)
                                break
                            except:
                                print 'Please Enter Valid Option'
                    index = int(index)
                    spy_list[i].current_status_message = spy_list[i].old_status[index - 1]
                    print "Your current status is: " + spy_list[i].current_status_message


def select_friend(login_name):
    select = 1
    print login_name
    for i in range(0, len(spy_list)):
        if spy_list[i].name == login_name:
            if not spy_list[i].friend_list:
                print "You Dont Have Any Friends Buddy"
                return 0
            else:
                print "Your Friends Are: "
                for j in range(0, len(spy_list[i].friend_list)):
                    print "%d. %s %s aged %d having ratings %d is online" % (
                    select, spy_list[i].friend_list[j].salutation, spy_list[i].friend_list[j].name,
                    spy_list[i].friend_list[j].age, spy_list[i].friend_list[j].rating)
                    select = select + 1
                while True:
                    choice = raw_input("Please Select Your Friend From Above Menu: ")
                    if len(choice) > 1:
                        print 'Please Enter Valid Option'
                    else:
                        try:
                            choice = int(choice)
                            break
                        except:
                            print 'Please Enter Valid Option'
                choice = int(choice)
                return choice - 1


def send_message(login_name):
    print colored("WARNING", "red")
    print colored("words limit is 100,if message is exceeded by 100,you will be deleted automatically\n", "red")

    friend_choice = select_friend(login_name)
    print friend_choice

    print "What do you want to say? \n 1.Send a secret message \n 2. Send a direct short message to user"
    choice = int(raw_input("Enter Your Choice: "))

    if choice == 1:
        message = raw_input("Enter your text message to be encrypted:? \n")
        for i in range(0, len(spy_list)):
            if spy_list[i].name == login_name:
                if 0 < len(message) < 100:
                    encryption_key = int(raw_input("Enter your encryption key:? \n"))
                    for j in range(0, len(message)):
                        store.append(ord(message[j]) + encryption_key + random_number)
                        print store
                    chat_message = store
                    chat_sent_by_me = True
                    spy_list[i].friend_list[friend_choice].chats.append(Chat(chat_message, chat_sent_by_me))
                    time.sleep(2)
                    print colored("MESSAGE IS ENCRYPTING..................", "red")
                    time.sleep(0.5)
                    print "ENCRYPTED"
                    print "Your secret message  is ready!"
                    print colored(store, "yellow")
                    break
                elif len(message) > 100:
                    print "Friend Deleted Is:" + spy_list[i].friends_list[friend_choice].name
                    del spy_list[i].friends_list[friend_choice]
        else:
            print "enter the correct detail"

    elif choice == 2:
        print(" HINT ", some_special_words.keys())
        sos_message = raw_input("Enter The Message :")

        for i in some_special_words.keys():
            if sos_message == i:
                values.append(some_special_words[i])
        chat_message = values
        chat_sent_by_me = False
        for i in range(0, len(spy_list)):
            if spy_list[i].name == login_name:
                spy_list[i].friends_list[friend_choice].chat.append(Chat(chat_message, chat_sent_by_me))


def read_message():
    print ""


def signup():
    while True:
        spy_name = raw_input('Hey What\'s Your Name Buddy!!!?? : ')
        if spy_name.isalpha() == True and len(spy_name) > 0:
            break
        else:
            print 'Please Enter Valid Name'
    while True:
        spy_salutation = raw_input('Should I Call You Mister or Miss?? : ')
        if spy_salutation == "Mister" or spy_salutation == "Miss":
            break
        else:
            print "Please Enter Valid Salutation"
    while True:
        spy_age = raw_input("What\'s Your Age Buddy:? : ")
        try:
            spy_age = int(spy_age)
            break
        except:
            print 'Please Enter Valid Age'
    spy_age = int(spy_age)
    if spy_age > 12 and spy_age < 50:
        while True:
            spy_rating = raw_input("What\'s Your Spy Rating?? : ")
            try:
                spy_rating = float(spy_rating)
                break
            except:
                print 'Please Enter Valid Rating'
        spy_rating = float(spy_rating)
        if spy_rating > 4.5:
            print 'Great Maan!!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
        spy_is_online = True
        print 'Authentication complete. Welcome %s %s spy_age: %d  and rating of: %.2f Proud to have you onboard' % (
            spy_salutation, spy_name, spy_age, spy_rating)
        spy_list.append(Spy(spy_name, spy_salutation, spy_age, spy_rating, spy_is_online, None, [], []))
    else:
        print 'Sorry you are not of the correct age to be a spy'


def login():
    while True:
        login_name = raw_input("Hey Spy!! Please enter your name please: ")
        if len(login_name) > 0:
            break
        else:
            print "Name can't be kept blank!!"

    for i in range(0, len(spy_list)):
        if spy_list[i].name == login_name:
            print "Your Details: "
            print " Name: %s %s Age: %d Rating: %.2f Online: %s " % (
            spy_list[i].salutation, spy_list[i].name, spy_list[i].age, spy_list[i].rating,
            spy_list[i].spy_is_online)
            while True:
                print "What Do You Want To Do?\n1.Add Friend\n2.Add Status Update\n3.Send Secret Message" \
                      "\n4.Read Chats\n5.Exit"
                while True:
                    choice = raw_input("Enter Your Choice: ")
                    if len(choice) > 1:
                        print 'Please Enter Valid Option'
                    else:
                        try:
                            choice = int(choice)
                            break
                        except:
                            print 'Please Enter Valid Option'
                choice = int(choice)
                if choice == 1:
                    add_friend(login_name)
                elif choice == 2:
                    add_status(login_name)
                elif choice == 3:
                    send_message(login_name)
                elif choice == 4:
                    read_message()
                elif choice == 5:
                    start()
                else:
                    print 'Enter Valid Choice'
                ch = raw_input(" Do You Wish To Continue(Y/N): ")
                if ch == 'N' or ch == 'n':
                    break

        else:
            print "You Are Not Existing Spy!! Please Sign Up"


def start():
    while True:
        print "Please Choose The Option From The Given Menu: \n 1.SignUp \n 2.Login \n 3.Exit"
        while True:
            choice = raw_input("Enter Your Choice: ")
            if len(choice) > 1:
                print 'Please Enter Valid Option'
            else:
                try:
                    choice = int(choice)
                    break
                except:
                    print 'Please Enter Valid Option'
        choice = int(choice)
        if choice == 1:
            signup()
        elif choice == 2:
            login()
        elif choice == 3:
            exit()
        else:
            print 'Enter Valid Choice'
        ch = raw_input(" Do You Wish To Continue(Y/N): ")
        if ch == 'N' or ch == 'n':
            break


start()
