"""
URL configuration for workshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import login
from polls.views import questions
from polls.views import add_question
from polls.views import get_questions
from polls.views import add_choice
from polls.views import get_choices
from polls.views import delete_question
from polls.views import edit_question
from polls.views import get_question_text
from polls.views import  update_question_text
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path("polls/", include("polls.urls")),
     path('', questions),
    path('questions/', questions),
    path('add_question/', add_question),
    path('get_questions/',get_questions),
    path('add_choice/<int:question_id>/',add_choice),
    path('get_choices/<int:question_id>/', get_choices),
    path('delete_question/<int:question_id>/', delete_question),
    path('edit_question/<int:question_id>/', edit_question),
    path('get_question_text/<int:question_id>/',get_question_text),
    path('update_question_text/<int:question_id>/', update_question_text),

    


]
