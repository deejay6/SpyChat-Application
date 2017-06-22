from spy_details import spy, spy_list, friends, friends_list,chat
from datetime import datetime
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
        friends['friend_is_online'] = True
        print "Friend Added Successfully"
        friends_list.append(friends.copy())
        print friends_list
    else:
        print 'Sorry your friend is not of the correct age'


def add_status(name):
    print spy_list
    for i in range(0, len(spy_list)):
        if spy_list[i]['name'] == name:
            if not spy_list[i]['old_status']:
                status_message = raw_input("Enter Your Status Message: ")
                if len(status_message) > 0:
                    print spy_list[i]['name']
                    spy_list[i]['old_status'].append(status_message)
                    spy_list[i]['current_status_message'] = status_message
                    print spy_list
                    break
                else:
                    print 'Status Mesage Cannot Be Blank'
            else:
                print spy_list
                print "Your Old Status Messages Are:"
                print spy_list[i]['old_status']
                print len(spy_list[i]['old_status'])
                status_number = 1
                for j in range(0, len(spy_list[i]['old_status'])):
                    print 'hey'
                    print '%d %s' % (status_number, spy_list[i]['old_status'][j])
                while True:
                    index = raw_input("Enter Your Choice: ")
                    if len(index) > 1:
                        print 'Please Enter Valid Option'
                    else:
                        try:
                            index = int(index)
                            break
                        except:
                            print 'Please Enter Valid Option'
                index = int(index)
                spy_list[i]['current_status_message'] = spy_list[i]['old_status'][index-1]
                print spy_list[i]['current_status_message']
                print spy_list

        break


def select_friend(name):
    print "Select Your Friend From Given List"
    friend_number = 1
    if not friends_list:
        print 'Add Friends'
        return 0
    else:
        for i in range(0, len(friends_list)):
            if friends_list[i]['friend_of'] == name:
                print "%d %s %s aged %d having ratings %.2f is online" % (friend_number, friends_list[i]['salutation'],
                                                                          friends_list[i]['name'],
                                                                          friends_list[i]['age'],
                                                                          friends_list[i]['rating'])
                friend_number = friend_number + 1
        while True:
            select = raw_input("Enter Your Choice: ")
            if len(select) > 1:
                print 'Please Enter Valid Option'
            else:
                try:
                    select = int(select)
                    break
                except:
                    print 'Please Enter Valid Option'
        select = int(select)
        return select-1


def send_message(name):
    friend_id = select_friend(name)
    while True:
        chat['message'] = raw_input("Enter Secret Message: ")
        if len(chat['message']) > 0:
            break
        else:
            print "Message can't be kept blank"
    chat['sent_by_me'] = True
    chat['datetime'] = datetime.now()
    print friends_list[friend_id]['name']
    print friends_list[friend_id]['chats']
    friends_list[friend_id]['chats'].append(chat.copy())
    print friends_list


def read_message():
    print 'Read Message'


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
                    send_message(name)
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