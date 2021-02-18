from django.db import models

# Create your models here.
from django.db.models import ManyToManyField

# Create your models here.


class Department(models.Model):
    dept = models.CharField(max_length=50 )
    # semester = models.CharField(max_length=12)

    def __str__(self):
        return self.dept
#     #     # relation = models.ManyToManyField(Department)
class Semester(models.Model):
    # sem_duration = models.IntegerField()
    semester = models.CharField(max_length=12)
    Department = models.ManyToManyField(Department)

    def __str__(self):
        return self.semester
    # def re(self):
    #     semester = self.semester
    #     return semester

    class Meta:
        ordering = ('semester',)

class Book(models.Model):
    department  = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.ForeignKey, null=True)
    # dept = models.CharField(max_length=50,  null=True )
    # sem = models.CharField(max_length=12, null=True)
    book_name = models.CharField(max_length=40, null=True)
    # def Ob(self):
    #     t = Semester()
    #
    #     return t.semester
    def __str__(self):
        return self.book_name