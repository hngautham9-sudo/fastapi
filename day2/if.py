age=20
if age>=20:
    print("welcome to the party")


num=10
if(num%2==0):
    print("even number")
else:
    print("odd number")


marks=82
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
else:
    print("fail")


color="red"
if color=="red":
    print("stop")
elif color=="yellow":
    print("get ready")
elif color=="green":
    print("go")
else:
    print("invalid color")

hallticket=True
id_card=True
if hallticket:
    if id_card:
        print("allowed to exam")
    else:
        print("get your id card")
else:
    print("get your hall ticket")


day=2
match  day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case _:
        print("invalid day")

dept="aiml"
match dept:
    case "aiml":
        print(f"{dept} available")
    case "aids":
        print(f"{dept} available")
    case "cse":
        print(f"{dept} available")
    case _:
        print("join sit")


name="varshi"
for i in name:
    print(i)

friend=["varshi","varshitha","varshu"]
for i in friend:
    print(i)

total=0
for num in range(1,5):
    total=total+num
    print("sum of total:",total)

for bench in range(1,16):
    print("bench-",bench)
    for student in range(1,5):
        print("student-",student)


number=1
while number<=5:
    print(number)
    number=number+1

class Student:
    def __init__(self,roll_no,name,age):
        self.roll_no=roll_no
        self.name=name
        self.age=age

    def display_details(self):
        print("roll_no:",self.roll_no)
        print("name:",self.name)
        print("age:",self.age)
    def dob(self):
        print(f"hey i'm {self.name} and i was born in {2026-self.age}")
student_1=Student(101,"varshi",20)
student_2=Student(102,"varshitha",21)
student_1.display_details()
student_2.display_details()
student_1.dob()
student_2.dob()