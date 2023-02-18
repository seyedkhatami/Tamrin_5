
#abstraction

"""
.انتزاع در شی گرایی فرایندی است که طی ان تنها ویژگی های اصلی ان هم بدون پیاده سازی جزئیات ارایه میگردد

.این مفهوم همراه با موجودیت کلاس تعریف میشود کلاس های ابسترکت

.دو نوع کلاس در شی گرایی وجود دارد : 1- کلاس های عادی که توانایی نمونه سازی دارند و به ان ها کانکریت کلاس گفته میشود 2- کلاس هایی که تونایی نمونه سازی ندارند و به ان ها ابسترکت کلاس گفته میشود

.کلاس های ابسترکت قابلیت نمونه سازی ندارند و نمیتوان از ان ها شی ایجاد نمود چرا که هدف از توسعه ان ها قرار گرفتن در بالاترین سطح یا چند سطح بالایی سلسله مراتب وراثت به عنوان کلاس پایه برای ارث  بری کلاس های پایین تر میباشد


در زبان برنامه نویسی پایتون ابسترکشن از طریق ماژول abc ارایه میشود.

"""

#دو ویژگی مهم ان


"""

1: I can't instanciate from a abstract class.

2: Contains abstract and concrete/normal methods.

"""


#example

from abc import ABC, abstractmethod

class MyABC(ABC):

    @abstractmethod
    def abs_instance_method(self):
        """This method should implement how to ..."""

    @classmethod
    @abstractmethod
    def abs_class_method(cls):
        """This method should implement how to ..."""


    @staticmethod
    @abstractmethod
    def abs_static_method():
        """This method should implement how to ..."""


