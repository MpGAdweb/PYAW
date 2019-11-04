from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Project
from django.core.mail import BadHeaderError, send_mail
from .forms import *
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data['from_name']
            from_email = form.cleaned_data['from_email']
            newslleter = form.cleaned_data['newslleter']
            message = "{0} wrote it:\nQuero receber: {1}\n\nMensagem:\n{2}".format(from_name, newslleter, form.cleaned_data['message'])
            try:
                send_mail('Web Contact', message, from_email, ['pakexo1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('index')
    return render(request, "site/index.html", {'form': form})

def detail(request, slug):
    try:
        qs = Project.objects.get(slug = slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    d_list = Project.objects.values_list('soluctions', flat=True).order_by('soluctions')
    return render(request, 'Projects/projects.html', {"qs": qs, "d_list": d_list})

def about(request):
    qs = Project.objects.all()
    return render(request, 'site/about.html', {"qs": qs})

def webdesign(request):
    if request.method == 'GET':
        form = AuditForm()
    else:
        form = AuditForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            url = form.cleaned_data['url']
            message = "{0} wrote it:\n\nURL: {1}\n\n".format(name, url)
            try:
                send_mail('Website Audit', message, email, ['pakexo1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Solicitação enviada!')
            return redirect('webdesign')
    return render(request, 'site/webdesign.html', {'form': form})

def paidads(request):
    return render(request, 'site/paidsearch.html')

def emkt(request):
    return render(request, 'site/email-marketing.html')

def iviusal(request):
    return render(request, 'site/branding.html')

def contactPage(request):
    if request.method == 'GET':
        form = FormContact()
    else:
        form = FormContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = "{0}\n{1}\n\n{2}".format(name, phone, form.cleaned_data['message'])
            try:
                send_mail('Web Contact Us', message, email, ['pakexo1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Formulário enviado!')
            return redirect('contact')
    return render(request, 'site/contact.html', {'form': form})
