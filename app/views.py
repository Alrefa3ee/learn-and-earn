from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, SimpleCookie
from .forms.studentForm import StudentForm

from .models import Student, Course, Video

# Create your views here.


def home(request):
    return render(request, "home/home.html")


def courses(request, username):
    gread = Student.objects.get(username=username).gread
    courses = Course.objects.filter(gread=gread)
    context = {"courses": courses, "username": username}
    return render(request, "course/courses.html", context)


def course(request, id):
    course = Course.objects.get(id=id)
    videos = Video.objects.filter(course=course)
    context = {"videos": videos, "course": course}
    return render(request, "course/course.html", context)


def login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            student = Student.objects.get(username=username, password=password)
            print(student)
            return render(request, "home/home.html", {"student": student})
        except:
            return render(request, "login/login.html", {"error": "Invalid Credentials"})
    return render(request, "login/login.html")


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(
            {
                "name": request.POST.get("name"),
                "username": request.POST.get("username"),
                "password": request.POST.get("password"),
                "age": request.POST.get("age"),
                "gread": request.POST.get("grade"),
            }
        )
        if form.is_valid():
            form.save()
            print("valid")
            return HttpResponseRedirect("/login")
        else:
            print(form.errors)
            return render(request, "login/register.html", {"form": form})

    return render(request, "login/register.html")


def profile(request, username):

    try:
        student = Student.objects.get(username=username)
        print(student)
        context = {"student": student}
        return render(request, "profile/profile.html", context)
    except Exception as errors:
        errors = "Invalid Credentials"
        return render(request, "profile/profile.html", {"errors": errors})


def handelScore(request, video_id, username, score):
    student = Student.objects.get(username=username)
    if str(video_id) in student.videos_watched:
        return HttpResponse("video already watched")
    student.points += score
    student.videos_watched += str(video_id) + ","
    student.save()
    return redirect("/me/" + student.username)

def handelPay(request, username):
    student = Student.objects.get(username=username)
    if request.method == "POST":
        if student.points >= int(250):
            student.points -= int(250)
            student.save()
            return redirect("/me/" + student.username)
        else:
            return HttpResponse("not enough points")
        