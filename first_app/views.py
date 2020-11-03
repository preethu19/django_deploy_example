from django.shortcuts import render, redirect
from first_app.models import AccessRecord, Topic, Webpage, User
from . import forms

# Create your views here.
def index(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    user = User.objects.all()
    date_dict = {'access_records': Webpages_list, 'user_list': user}
    return render(request,'first_app/index.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation Success')
            print('Name: '+form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
    return render(request, 'first_app/form_name.html', {'form': form})

def users(request):
    form = forms.NewUser()
    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print('Error form invalid')
    return render(request, 'first_app/users.html', {'form': form})