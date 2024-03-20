#SNAKE GAME!

input1 = input("Please enter feeding map as a list:")
all_of_letters_list= []
u = 0 #Amount of cells
mainlist= []

for x in input1:
    a = input1.count("[")
k = (a-1) #Amount of inside lists

for t in input1:
    if t=="A" or t=="C" or t=="P" or t=="M" or t=="W" or t=="X" or t=="*":
        all_of_letters_list.append(t)

for z in all_of_letters_list:
    u += 1
number_of_elements_in_one_list = u/k
n = int(number_of_elements_in_one_list)

for g in range(k):
    mainlist.append(all_of_letters_list[g*n:(g+1)*n]) #Combining all cells

first = 0
second = 0

for b in range(len(mainlist)): #Finding where "*" is
    for c in range(len(mainlist[b])):
        if mainlist[b][c] == "*":
            first = b
            second = c
directions = input("Please enter direction of movements as a list:")
print("Your board is:")
for v in range(len(mainlist)):
    print("{}".format(" ".join(mainlist[v])))
movements= []
point = 0
second_copy = int(second)
first_copy = int(first)
for y in directions:
    if y == "U" or y == "D" or y == "L" or y == "R":
        movements.append(y)
for q in movements:
    if q == "R":
        if mainlist[first][second] == mainlist[first][-1]:
            continue
        elif mainlist[first][second+1] == "A":
            point += 5
            second += 1
        elif mainlist[first][second+1] == "C":
            point += 10
            second += 1
        elif mainlist[first][second+1] == "M":
            point -= 5
            second += 1
        elif mainlist[first][second+1] == "X":
            second += 1
        elif mainlist[first][second+1] == "P":
            second += 1
            mainlist[first][second_copy] = "X"
            mainlist[first][second_copy+1] = "*"
            second_copy += 1
            break
        elif mainlist[first][second+1] == "W":
            continue
        mainlist[first][second_copy] = "X"
        mainlist[first][second_copy+1]= "*"
        second_copy += 1
    if q == "L":
        if mainlist[first][second] == mainlist[first][0]:
            continue
        elif mainlist[first][second-1] == "A":
            point += 5
            second -= 1
        elif mainlist[first][second-1] == "C":
            point += 10
            second -= 1
        elif mainlist[first][second-1] == "M":
            point -= 5
            second -= 1
        elif mainlist [first][second-1] == "X":
            second -= 1
        elif mainlist[first][second-1] == "P":
            second -= 1
            mainlist[first][second_copy] = "X"
            mainlist[first][second_copy-1] = "*"
            second_copy -= 1
            break
        elif mainlist[first][second-1] == "W":
            continue
        mainlist[first][second_copy] = "X"
        mainlist[first][second_copy-1] = "*"
        second_copy -= 1
    if q == "D":
        if mainlist[first][second] == mainlist[-1][second]:
            continue
        elif mainlist[first+1][second] == "A":
            point += 5
            first += 1
        elif mainlist[first+1][second] == "C":
            point += 10
            first += 1
        elif mainlist[first+1][second] == "M":
            point -= 5
            first += 1
        elif mainlist[first+1][second] == "X":
            first += 1
        elif mainlist[first+1][second] == "P":
            first += 1
            mainlist[first_copy][second] = "X"
            mainlist[first_copy+1][second] ="*"
            first_copy += 1
            break
        elif mainlist[first+1][second] == "W":
            continue
        mainlist[first_copy][second] = "X"
        mainlist[first_copy+1][second] = "*"
        first_copy += 1
    if q == "U":
        if mainlist[first][second] == mainlist[0][second]:
            continue
        elif mainlist[first-1][second] == "A":
            point += 5
            first -= 1
        elif mainlist[first-1][second] == "C":
            point += 10
            first -= 1
        elif mainlist[first-1][second] == "M":
            point -= 5
            first -= 1
        elif mainlist[first-1][second] == "X":
            first -= 1
        elif mainlist[first-1][second] == "P":
            first -= 1
            mainlist[first_copy][second]="X"
            mainlist[first_copy+1][second] ="*"
            first_copy -=1
            break
        elif mainlist[first-1][second] == "W":
            continue
        mainlist[first_copy][second] = "X"
        mainlist[first_copy-1][second] = "*"
        first_copy -= 1
print("Your output should be like this:")
for v in range(len(mainlist)):
    print("{}".format(" ".join(mainlist[v])))
print("Your score is:",point)
