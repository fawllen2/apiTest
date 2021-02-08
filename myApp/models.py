from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    stdNumber = models.IntegerField()

    TEACHER = (
        ("teacher 1", "Teacher 1"),
        ("teacher 2", "Teacher 2"),
        ("teacher 3", "Teacher 3")
    )
    teacher = models.CharField(max_length=9, choices=TEACHER)