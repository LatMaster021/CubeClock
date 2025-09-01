from PIL import Image
#introduce the user to the game!
image = Image.open('CubeClockImage.jpg')
image.show()
print("Welcome to CubeClock!👋")
print("You are given two cubes (6 faces each). The task is simple: apply a SINGLE DIGIT to each of the faces on cube a, and cube b, so that you can represent all the possible  dates of the month (01 up to 31) using just the two cubes")
print("You have three attempts!")
def cubeclock():
    #create an array representing all the possible dates in a month:
    array_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    for i in range(10, 32):
        array_days.append(str(i))
    created_days = []
    not_created_days = []
    not_created_days_final = []

    #define the cubes
    cube_a = []
    cube_b = []
    for i in range(1, 7):
        a_input = input("Enter the #" + str(i) +  " digit for cube a: ")
        cube_a.append(a_input)
    for i in range(1, 7):
        b_input = input("Enter the #" + str(i) +  " digit for cube b: ")
        cube_b.append(b_input)

    #check if you can form the date
    for i in range(0, len(array_days)):
        for j in range(0, 6):
            for k in range(0, 6):
                if (cube_a[j] + cube_b[k]) == array_days[i]:
                    created_days.append(array_days[i])
                elif (cube_b[j] + cube_a[k]) == array_days[i]:
                    created_days.append(array_days[i])

    #get in the dates you couldn't create
    for i in range(0, len(array_days)):
        if array_days[i] not in created_days:
            not_created_days.append(array_days[i])

    #check for 6 or 9 as these can multi-task - 69/96 not a date
    contains_6 = False
    contains_9 = False
    for i in range(0, 6):
        if cube_a[i] == '6' or cube_b[i] == '6':
            contains_6 = True
        elif cube_a[i] == '9' or cube_b[i] == '9':
            contains_9 = True
    if contains_6 == False and contains_9 == False:
            print("You need either 6 or 9")

    if contains_6 == True:
        for i in range(0, len(not_created_days)):
            if not_created_days[i] == '09':
                created_days.append(not_created_days[i])
            elif not_created_days[i] == '19':
                created_days.append(not_created_days[i])
            elif not_created_days[i] == '29':
                created_days.append(not_created_days[i])

    if contains_9 == True:
        for i in range(0, len(not_created_days)):
            if not_created_days[i] == '06':
                created_days.append(not_created_days[i])
            elif not_created_days[i] == '16':
                created_days.append(not_created_days[i])
            elif not_created_days[i] == '26':
                created_days.append(not_created_days[i])

    #get in the dates you couldn't create overall
    for i in range(0, len(array_days)):
        if array_days[i] not in created_days:
            not_created_days_final.append(array_days[i])

    #output your results!
    if len(created_days) == 0:
        print("No dates created")
        return False
    else:
        print("These dates were successfully created with your guess: ")
        for i in range(0, len(created_days) - 1):
            print(created_days[i], end=", ")
        print(created_days[len(created_days) - 1])
    if len(not_created_days_final) == 0:
        print("ALL DAYS SUCCESSFULY CREATED!")
        return True
    else:
        print("These are the dates you're missing: ")
        for i in range(0, len(not_created_days_final) - 1):
            print(not_created_days_final[i], end=", ")
        print(not_created_days_final[len(not_created_days_final) - 1])
        return False

result = False
count = 1
while result == False and count <= 3:
    if count > 1:
        print("This is your #" + str(count) + " try!")
        print("Clue: some digits may be re-used 😉")
    result = cubeclock()
    count += 1

#run it!
if result == True:
    print("Great job!")
else:
    print("Better luck next time!")
