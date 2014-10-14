print "How many numbers do you want to add?"
userInput = int(raw_input())
total = 0 
for x in range(userInput):
    total = total + int(raw_input())
print total 


totalList = []
print "How many numbers do you want to add?"
userInput2 = int(raw_input())
for x in range(userInput2):
    print "How much does the item cost?" 
    userInput2 = int(raw_input())
    totalList.append(userInput2)
print sum(totalList) 


print "What do you want the factorial of?"
total = 1
userInput3 = int(raw_input()) + 1 
for x in range(1,userInput3,1):
    total = total * x
print total

print "what number do you want to find the factor of"
userInput4 = int(raw_input())
for x in range(1,userInput4):
    if userInput4%x == 0:
        print x 

