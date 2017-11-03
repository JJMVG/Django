from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404, HttpResponse
from .models import Person
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from random import randint
from django.core.mail import EmailMessage, send_mail
from django.conf import settings




def home(request):
    all_people = Person.objects.all()

    context ={'all_people':all_people}
    return render(request,'teasite/home.html',context)

class HomeView(generic.ListView):
    template_name = 'teasite/home.html'
    context_object_name = 'all_people'

    def get_queryset(self):
        return Person.objects.all()


class DetailView(generic.DetailView):
    model = Person
    template_name = 'teasite/detail.html'

class PersonCreate(CreateView):
    model = Person
    fields =['name','drink','sugar','milk','profile_picture','email']

class PersonUpdate(UpdateView):
    model = Person
    fields = ['name','drink','sugar','milk','profile_picture','email']

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('teasite:home')

def TeaMail(request):

    all_people = Person.objects.all()
    id_selector = randint(0,len(all_people))
    maker = all_people[id_selector]
    content = '{} has been selection to make tea! Get your orders in..'.format(maker.name)
    recip = []
    for add in all_people:
        recip.append(add.email)

    '''
    email = EmailMessage(
            "Teabot V1.0",
            content,
            'tearoom.django@gmail.com',
            recipients,
            headers = {'Reply-To': 'julien.grondin@ifpi.org' })
    email.send()
    '''
    send_mail('Teabot V1.0', content, settings.EMAIL_HOST_USER,
    recip, fail_silently=False)

    return HttpResponse('{} has been selected for this tea round'.format(maker.name))