from django.shortcuts import render
from .models import Question, Choice

# Create your views here.

def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/question.html', context)

def about(request):
    return render(request, 'polls/about.html')