from spy_details import spy, spy_list , friends , friends_list
print 'Welcome To SpyChat Application'


def add_friend(name):
    friends['friend_of'] = name
    while True:
        friends['name'] = raw_input("Enter Friend's Name : ")
        if friends['name'].isalpha() == True and len(friends['name']) > 0:
            break
        else:
            print 'Please Enter Valid Name'
    while True:
        friends['salutation'] = raw_input('Should I Call Him Mister or Miss?? : ')
        if friends['salutation'] == "Mister" or friends['salutation'] == "Miss":
            break
        else:
            print "Please Enter Valid Salutation"
    while True:
        friends['age'] = raw_input("Enter Friend's Age : ")
        try:
            friends['age'] = int(friends['age'])
            break
        except:
            print 'Please Enter Valid Option'
    friends['age'] = int(friends['age'])
    if friends['age'] > 12 and friends['age'] < 50:
        while True:
            friends['rating'] = raw_input("Enter Friend's Rating : ")
            try:
                friends['rating'] = float(friends['rating'])
                break
            except:
                print 'Please Enter Valid Option'
        friends['rating'] = float(friends['rating'])
        if friends['rating'] > 4.5:
            print 'Great ace!'
        elif friends['rating'] > 3.5 and friends['rating'] <= 4.5:
            print 'Your friend is one of the good ones.'
        elif friends['rating'] >= 2.5 and friends['rating'] <= 3.5:
            print 'Your friend can always do better'
        else:
            print 'We can always use somebody to help him in the office.'
        friends['spy_is_online'] = True
        print "Friend Added Successfully"
        friends_list.append(friends.copy())
        print friends_list
    else:
        print 'Sorry your friend is not of the correct age'


def add_status(name):
    print 'Status'


def send_message():
    print 'Send Message'


def read_chats():
    print 'Read Chats'



def login():
    name = raw_input("Please Enter Your Name Spy: ")
    print spy_list
    for i in range(0, len(spy_list)):
        if name == spy_list[i]['name']:
            print "Spy Details Are: \n" + "Name: " + spy_list[i]['salutation'] + " " + spy_list[i]['name'] + \
                  " " + "Age: " + str(spy_list[i]['age']) + " " + "Rating: " + str(spy_list[i]['rating'])
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
                    add_friend(name)
                elif choice == 2:
                    add_status(name)
                elif choice == 3:
                    send_message()
                elif choice == 4:
                    read_chats()
                elif choice == 5:
                    start()
                else:
                    print 'Enter Valid Choice'
                ch = raw_input(" Do You Wish To Continue(Y/N): ")
                if ch == 'N' or ch == 'n':
                    break
        else:
            print 'You are not an existing spy!!'


def signup():
    while True:
        spy['name'] = raw_input('Hey What\'s Your Name Buddy!!!?? : ')
        if spy['name'].isalpha() == True and len(spy['name']) > 0:
            break
        else:
            print 'Please Enter Valid Name'
    while True:
        spy['salutation'] = raw_input('Should I Call You Mister or Miss?? : ')
        if spy['salutation'] == "Mister" or spy['salutation'] == "Miss":
            break
        else:
            print "Please Enter Valid Salutation"
    while True:
        spy['age'] = raw_input("What\'s Your Age Buddy:? : ")
        try:
            spy['age'] = int(spy['age'])
            break
        except:
            print 'Please Enter Valid Option'
    spy['age'] = int(spy['age'])
    if spy['age'] > 12 and spy['age'] < 50:
        while True:
            spy['rating'] = raw_input("What\'s Your Spy Rating?? : ")
            try:
                spy['rating'] = float(spy['rating'])
                break
            except:
                print 'Please Enter Valid Option'
        spy['rating'] = float(spy['rating'])
        if spy['rating'] > 4.5:
            print 'Great ace!'
        elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
            print 'You are one of the good ones.'
        elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
        spy['spy_is_online'] = True
        print 'Authentication complete. Welcome %s age: %d  and rating of: %.2f Proud to have you onboard' % (
            spy['name'], spy['age'], spy['rating'])
        spy_list.append(spy.copy())
    else:
        print 'Sorry you are not of the correct age to be a spy'


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
        if ch == 'N'or ch == 'n':
            break
start()