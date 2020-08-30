# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    return render(request,"base.html")


from .forms import *
from .models import *

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
    print(pitchDeck.objects.all())

    return render(request,"profile.html")


@login_required
def input(request):
    if request.method == 'POST':
            form = pitchDeckForm(request.POST)
            form.instance.user = request.user
            
            ##titleslide
            tform = titleSlideForm(request.POST)
            tform.instance.pitchDeckId = form.instance
            
            pform = problemTryingToSolveForm(request.POST)
            pform.instance.pitchDeckId = form.instance
            
            vform = visionForm(request.POST)
            vform.instance.pitchDeckId = form.instance
            
            USPform = uniqueValuePropositionForm(request.POST)
            USPform.instance.pitchDeckId = form.instance
            
            mform = milestonesForm(request.POST)
            mform.instance.pitchDeckId = form.instance
            
            tamform = totalAddressableMarketForm(request.POST)
            tamform.instance.pitchDeckId = form.instance
            
            bmform = businessModalForm(request.POST)
            bmform.instance.pitchDeckId = form.instance
            
            cform = CompetitionForm(request.POST)
            cform.instance.pitchDeckId = form.instance
            
            caform = competitiveAdvantageForm(request.POST)
            caform.instance.pitchDeckId = form.instance
            
            if form.is_valid() and tform.is_valid():
                form.save()
                tform.save()
                return redirect('next/'+str(tform.instance.pitchDeckId.pitchDeckId)+'/')
                ''' vform.save()
                USPform.save()
                mform.save()
                tamform.save()
                bmform.save()
                cform.save()
                caform.save()'''
                
    else:
        form = pitchDeckForm()
        tform = titleSlideForm()
        '''pform = problemTryingToSolveForm()
        vform = visionForm()
        USPform = uniqueValuePropositionForm()
        mform = milestonesForm()
        tamform = totalAddressableMarketForm()
        bmform = businessModalForm()
        cform = CompetitionForm()
        caform = competitiveAdvantageForm()'''
            
           
    return render(request,'data.html',{'form':form,
                                        'tform':tform
                                                     })

@login_required
def next(request):
    return HttpResponse("profile.html")

'''             'vform':vform,
                                                     'USPform':USPform,
                                                     'mform':mform,
                                                     'tamform':tamform,
                                                     'bmform':bmform,
                                                     'cform':cform,
                                                     'caform':caform'''

