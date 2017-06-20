s = raw_input("Enter String: ")
flag = 0
for i, j in zip(range(0, len(s)-3),  range(2, len(s)-1)):
    if s[i] != s[j]:
        flag = 0
        print 'no'
        break
    else:
        flag = 1
        print 'yes'
if flag == 1:
    print 'yes1'
else:
    print 'no'
