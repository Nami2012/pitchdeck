
# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                return redirect('login')
    else:
        form = SignUpForm()


    return render(request,'authenticate/signup.html',{'form':form})

def home(request):
    return render(request,"base.html")


