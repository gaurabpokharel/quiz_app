from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/get-quiz', views.get_quiz, name="get_quiz"),
    path('quiz/', views.quiz, name="quiz")
]
