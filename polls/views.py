from django.shortcuts import render, redirect
from .models import Question, Choice
from .forms import ChoiceForm

# Create your views here.

def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/questions.html', context)

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    context = {'question': question, 'choices': choices}
    return render(request, 'polls/question.html', context)

def about(request):
    return render(request, 'polls/about.html')

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method != 'POST':
        form = ChoiceForm()
    
    else:
        form = ChoiceForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('polls:vote', question_id=question_id)
    
    context = {'form': form, 'question': question}
    return render(request, 'polls/vote.html', context)