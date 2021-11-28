#https://www.alura.com.br/artigos/django-query-sets-e-orm?gclid=CjwKCAiAp8iMBhAqEiwAJb94zwnHSnYj2h_GswQd-LI9sPtYwfhFICsMB790UGFjzzg5ONKHcXmCeRoC5vEQAvD_BwE
#https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import AuthUser, Cliente, Agency #Employee, Project, DocumentModel, LdProj, Subject
from .forms import AgencyForm #, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages
import code as CODE
from datetime import datetime, timedelta

date_today = datetime.today()

@login_required
def home(request):
    
    #tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    #tasksDone = Task.objects.filter(done='done', user=request.user).count()
    #task.done = 'done'

    AuthUsers = AuthUser.objects.filter(name_user=request.user)

    startdate = date_today - timedelta(days=395)
    enddate = date_today - timedelta(days=325)
    #print('>>>>>>>>>>', startdate, '++++++', enddate)
    # Sample.objects.filter(date__range=[startdate, enddate])
    Clientes = Cliente.objects.filter(date_contract__range=[startdate, enddate])

    #Clientes = Cliente.objects.all()

    return render(request,'task/index.html', {'Clientes':Clientes, 'AuthUsers':AuthUsers}) #, {'user':user})


@login_required
def clients(request):

    AuthUsers = AuthUser.objects.filter(name_user=request.user)
    Clientes = Cliente.objects.all().order_by('name')

    return render(request,'task/clients-list.html', {'Clientes':Clientes, 'AuthUsers':AuthUsers}) #, {'user':user})


@login_required
def Spreadsheet(request):
    
    AuthUsers = AuthUser.objects.filter(name_user=request.user)

    

    return render(request,'task/carga-plan.html',{'AuthUsers':AuthUsers})


@login_required
def CreateDB(request):

    CODE.compare_tables()

    return redirect('/')







