from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Todo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from django.utils import timezone


class TodosListView(ListView):
    model = Todo
    template_name = 'app/index.html'
    context_object_name = 'todos'
    paginate_by = 8

    def get_queryset(self):
        expired_tasks = Todo.objects.filter(date_field__lt=timezone.localtime().now())
        expired_tasks.update(is_expired=True)
        return Todo.objects.all()


class TodosCreateView(LoginRequiredMixin, CreateView):
    form_class = TodoForm
    template_name = 'app/todo_form.html'
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "To-Do created!")
        return super().form_valid(form)


@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo-home')


def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        u_form = TodoForm(request.POST, instance=todo)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"To-do has been updated!")
            return redirect('todo-home')
    else:
        u_form = TodoForm(instance=todo)
    return render(request, 'app/todo_form.html', {
        'u_form': u_form,
        'update': True,
    })
