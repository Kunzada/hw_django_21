from django.db import models

# Create your models here.
class Person(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth=models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        abstract=True


class Employee(Person):
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
     
    def __str__(self):
        return f"{self.full_name} - {self.position}"
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

class Student(Person):
    placeOfStudy=models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    grade = models.IntegerField()
    GPA=models.FloatField()

    def __str__(self):
        return f"{self.full_name} - {self.placeOfStudy}"
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        abstract=True

class isWorkingStudent(Student):
    isWorking = models.BooleanField()

    def __str__(self):
        return f"{self.full_name} - {self.placeOfStudy} ({'Working' if self.isWorking else 'Not Working'})"