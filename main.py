import time

while True:
    current_gpa = float(input("please enter your current average as a number between 0 to 100:"))
    if not (0 <= current_gpa <= 100):
        print("please enter a number between 0 to 100")
        continue
    else:
        break

while True:
    number_of_courses = float(input("please enter the number of credits in your average as a "
                                    "number between 0.25 to 30:"))
    if not (0 < number_of_courses <= 30):
        print("please enter a number between 0.25 to 30")
        continue
    else:
        break

while True:
    desired_gpa = float(input("please enter your desired gpa as a number between 0 to 100:"))
    if (desired_gpa == 100) and (current_gpa != 100):
        print("lol rip, that's impossible ;-; try something else")
        continue
    if (desired_gpa == 0) and (current_gpa != 0):
        print("huh. that's interesting, but no")
        continue
    elif not (0 < desired_gpa < 100):
        print("please enter a number between 0 to 100")
        continue
    else:
        break

while True:
    number_of_future_courses = float(input("please enter the number of future credits you wish"
                                           " to take to achieve this average:"))
    if not (0 < number_of_future_courses <= 30):
        print("please enter a number between 0.25 to 30")
        continue
    else:
        break

avg = (desired_gpa * (number_of_courses + number_of_future_courses)
               - number_of_courses * current_gpa) / number_of_future_courses
avg1 = str(avg)

print("the number below is the average you will need in your future classes")
time.sleep(0.5)
print("are you sure you are ready for this?")
time.sleep(0.5)
print("i am not responsible for you crying")
time.sleep(0.5)
print("okay, here it is")
time.sleep(0.5)
if avg > 100:
    print(avg1)
    print("rip, better luck next time")
else:
    print(avg1)