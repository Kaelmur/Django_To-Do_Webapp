from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import user_passes_test, login_required


@user_passes_test(lambda u: not u.is_authenticated, login_url='todo-home')
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account {username} has been created! Log In to proceed.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {
        'form': form
    })
