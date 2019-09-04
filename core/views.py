from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail

from .forms import RequestForm, DonateForm
from .models import Request, Donation

def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def success(request):
    done=False
    while not done:
        toFill=Request.objects.all().order_by('time').first()
        if not toFill:
            done=True
        else:
            donors=[Donation.objects.filter(tickets__gte=toFill.tickets).order_by('tickets').first()]
            if not donors[0]:
                donors=[]
                potentials=Donation.objects.all().order_by('-tickets')
                left=toFill.tickets

                finished=False
                count=0
                while count<len(potentials) and not finished:
                    if left-potentials[count].tickets<=0:
                        potentials[count].tickets-=left
                        left=0
                        finished=True
                    else:
                        left-=potentials[count].tickets
                        potentials[count].tickets=0
                    donors.append(potentials[count])
                    count+=1
                if left!=0: #cant fill any more
                    done=True

            else:
                donors[0].tickets -= toFill.tickets

            if not done:
                emails=[toFill.email]
                for donor in donors:
                    emails.append(donor.email)
                    donor.save()
                    if donor.tickets==0:
                        donor.delete()
                toFill.delete()
                print(emails)
        ###if can be filled
            ##donoremails.append
            ###send email code
            #send_mail('Ticket Swap','Ill have a number 9 large','info@graduation.mbhs.edu',[dmails,'jessesilverberg11@gmail.com'],fail_silently=False,)

    ###### Maybe make context for which type like what kind of instructions hmm
    context = {}
    return render(request, 'core/success.html', context)

def donate(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DonateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            donation = form.save()
            donation.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/success')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = DonateForm()

    context = {'form': form}
    return render(request, 'core/donate.html', context)

def request(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            request = form.save(commit=False)
            request.time = timezone.now()
            request.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/success')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

    context = {'form': form}
    return render(request, 'core/request.html', context)




