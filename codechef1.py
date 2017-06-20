str = raw_input("Enter the string: ")
temp = [str[0], str[1]]

flag = True

for i in range(2, len(str)):
    if str[i] != temp[i%2]:
        flag = False
        break

if flag:
    print "YES"
else:
    print "NO"