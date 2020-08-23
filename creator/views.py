# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    return render(request,"base.html")


from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm

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


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        print("hello")
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
          
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile_update.html',context)

@login_required
def profile(request):
    return render(request,"profile.html")

