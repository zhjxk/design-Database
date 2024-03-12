from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id
    name = models.CharField(max_length= 10)
    # 重写admin以显示书籍名称
    def __str__(self):
        return self.name
# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length = 10)
    gender = models.BooleanField
    # 外键约束，人物是输入那一本书
    book = models.ForeignKey(BookInfo,on_delete= models.CASCADE)