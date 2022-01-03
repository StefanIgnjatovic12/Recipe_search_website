from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, you are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#User updating user info (username, email) and profile info (image)
@login_required
def profile(request):
    if request.method == "POST":
        # if the request is POST, we populate the form with the data inputted in the form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Update succesful')
            return redirect('profile')
    else:
        # if the request isn't POST, we leave the current user info populated in the fields
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # context lets us use the forms on the profile.html file
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, "users/profile.html", context)