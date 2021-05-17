from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile


def home(request):
    texts = Profile.objects.all()
    return render(request, 'home.html', {'texts': texts})

def my_projects(request):

    return render(request, 'my_projects.html')

def contacts(request):

    return render(request, 'contacts.html')

def upload(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form = ProfileForm()
    
    return render(request, 'upload.html', {'form': form})