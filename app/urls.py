from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("courses/<str:username>", views.courses, name="courses"),
    path("course/<int:id>", views.course, name="courses"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("me/<str:username>", views.profile, name="profile"),
    path(
        "user/<int:video_id>/<str:username>/<int:score>",
        views.handelScore,
        name="handelScore",
    ),
    path("handelPay/<str:username>", views.handelPay, name="handelPay"),
]
