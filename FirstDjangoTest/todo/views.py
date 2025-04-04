from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.filter(is_deleted=False)
    return render(request, 'todo/list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add.html', {'form': form})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_deleted = True
    todo.save()
    return redirect('todo_list')
