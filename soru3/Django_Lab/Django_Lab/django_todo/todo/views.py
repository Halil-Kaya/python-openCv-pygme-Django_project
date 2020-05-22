from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo
import random


# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(quest=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.isComplete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(isComplete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

def rndQuest(request):

    newTodo = ["ödev yap","kod yaz","müzik çal","yemek ye","uyu"]
    
    rnd = random.randint(0, 4)

    new_todo = Todo(quest=newTodo[rnd])
    new_todo.save()


    return redirect('index')