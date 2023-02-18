# example [is a]

"""
Student is a human.
Teacher is a human.
banana is a fruit.
cucamber is a vegetable.
"""

#Difference in [is a] and [has a]
#is a

"""
ارث بری توسط 
is a
بیان میشود.این نسبت میگوید کلاس فرزند یک نوع از چیزی است که کلاس پایه هست.کلاس
a
از کلاس
b
ارثبری دارد.در این حالت میگوییم 
a is a type of b
یعنی درست است اگر بگوییم سیب یک نوع میوه است یا خودرو یک نوع وسیله نقلیه است ولی توجه داشته باشید که این یک ارتباط یک طرفه از کلاس فرزند به کلاس پایه است و نمیتوانیم بگوییم میوه یک نوع سیب است یا وسیله نقلیه یک نوع خودرو است 

"""

#has a 

"""
در برنامه نویسی شی گرا نسبت دیگری با عنوان
has a
وجود دارد که بیانگر مفهومی به نا ترکیب 
composition
است که شکل دیگری  از قابلیت استفاده مجدد کد میباشد ولی مفهومی متفاوت با وراثت دارد.این نسبت زمانی بیان میشود که درون یک کلاس مانند
C
از کلاس دیگری مانند
D
نمونه سازی شده باشد یعنی شی کلاس
C
درون خودش شی ای از کلاس 
D
را داشته باشید.دراین حالت میگوییم
C has a D
برای مثال کلاس خودرو از کلاس های کوچک تری ساخته شده است مثلا کلاس موتور یعنی درون این کلاس یک شی از کلاس موتور ایجاد شده است اکنون میتوانیم بگوییم خودرو یک موتور دارد
"""

class Human:
    pass

class Student(Human):
    pass

class Teacher(Human):
    pass

class Vegetable:
    pass

class Cucamber(Vegetable):
    pass

class Fruit:
    pass

class Banana(Fruit):
    pass


#example [has a]

"""
Composition:Two entities are related to each other.
Example:
Human has a heart.
Goat has a feet.
Panguin has a wings.


Aggregation:Two entities are independent and can separate them.
Example:
Department has a students.
City has a human.
Mr.Ali has a phone.

"""

#Composition
class Heart:
    pass

class Human:
    def __init__(self, name):
        self.name = name
        self.heart = Heart()

human = Human(name = "Ali")


#Aggregation
class Phone:
    pass

class MrAli:
    def __init__(self, phone):
        self.phone = phone

phone = Phone()
me = MrAli(phone=phone)