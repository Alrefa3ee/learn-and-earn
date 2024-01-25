from django.db import models

gread = (
    ("1", "1"),
    ("5", "5"),
    ("12", "12"),
)


class Student(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=220, unique=True)
    password = models.CharField(max_length=220)
    age = models.IntegerField()
    gread = models.CharField(choices=gread, max_length=220)
    points = models.IntegerField(default=0)
    # list_of_ids of watched videos
    videos_watched = models.CharField(max_length=220, default="", blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=220)
    image = models.CharField(max_length=220)
    gread = models.CharField( choices=gread, max_length=220)

    def __str__(self):
        return self.name + " " + self.gread


class Video(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=220)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz = models.CharField(max_length=220)
    answer = models.CharField(max_length=220)

    def __str__(self):
        return self.name
