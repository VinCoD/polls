from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('questions', views.questions, name='index'),
    path('about', views.about, name='about'),
    path('questions/<int:question_id>/', views.question, name='question'),
]