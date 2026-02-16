from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskForm
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})

def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form})

def editTask(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "edit_task.html", {"form": form})

def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect("home")

