from spy_details import Spy, Friend, spy_list, friend_list


def add_friend(login_name):
    friend_of = login_name
    while True:
        friend_name = raw_input('Hey What\'s Your Friend\'s Name !!!?? : ')
        if friend_name.isalpha() == True and len(friend_name) > 0:
            break
        else:
            print 'Please Enter Valid Name'
    while True:
        friend_salutation = raw_input('Should I Call Your Friend Mister or Miss?? : ')
        if friend_salutation == "Mister" or friend_salutation == "Miss":
            break
        else:
            print "Please Enter Valid Salutation"
    while True:
        friend_age = raw_input("What\'s Your Friend's Age :? : ")
        try:
            friend_age = int(friend_age)
            break
        except:
            print 'Please Enter Valid Age'
    friend_age = int(friend_age)
    if friend_age > 12 and friend_age < 50:
        while True:
            friend_rating = raw_input("What\'s Your Friend's Rating?? : ")
            try:
                friend_rating = float(friend_rating)
                break
            except:
                print 'Please Enter Valid Rating'
        friend_rating = float(friend_rating)
        friend_is_online = True
        friend_list.append(Friend(friend_name, friend_salutation, friend_age, friend_rating, friend_is_online,friend_of))
        for i in range(0 , len(friend_list)):
            if friend_list[i].friend_of == friend_of:
                print "Friends are: "
                print friend_list[i].name
    else:
        print 'Sorry you are not of the correct age to be a friend'



def add_status(login_name):
    for i in range(0 , len(spy_list)):
        if spy_list[i].name == login_name:
            if not spy_list[i].old_status:
                while True:
                    status_message = raw_input("Enter Your Status Message: ")
                    if len(status_message) > 0:
                        break
                    else:
                        print "Mesage can't be kept blank"
                spy_list[i].old_status.append(status_message)
                spy_list[i].current_status_message = status_message
                print "Your current status message is: " + spy_list[i].current_status_message
            else:
                print "Your Old Status Messages Are:"
                status_number = 1
                for j in range(0, len(spy_list[i].old_status)):
                    print '%d %s' % (status_number, spy_list[i].old_status[j])
                    status_number = status_number +1
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
                elif ch.upper()=="N":
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
                    spy_list[i].current_status_message = spy_list[i].old_status[index-1]
                    print "Your current status is: " + spy_list[i].current_status_message


def send_message(login_name):
    print ""


def read_message(login_name):
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
        spy_list.append(Spy(spy_name, spy_salutation, spy_age, spy_rating, spy_is_online,None,[], []))
    else:
        print 'Sorry you are not of the correct age to be a spy'


def login():
    while True:
        login_name = raw_input("Hey Spy!! Please enter your name please: ")
        if len(login_name) > 0:
            break
        else:
            print "Name can't be kept blank!!"

    for i in range(0 ,len(spy_list)):
        if spy_list[i].name == login_name:
            print "Your Details: "
            print " Name: %s %s Age: %d Rating: %.2f Online: %s " %(spy_list[i].salutation, spy_list[i].name, spy_list[i].age, spy_list[i].rating,
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
        if ch == 'N'or ch == 'n':
            break
start()