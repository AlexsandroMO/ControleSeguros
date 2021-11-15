from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Cliente, Agency #Employee, Project, DocumentModel, LdProj, Subject
from .forms import AgencyForm #, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages
import code as CODE
from datetime import datetime

date_today = datetime.today()

@login_required
def home(request):
    #AuthUser = auth_user.objects.all()
    #user = request.user

    return render(request,'task/index.html') #, {'user':user})


@login_required
def clients(request):
    #AuthUser = auth_user.objects.all()
    #user = request.user
    Clientes = Cliente.objects.all()

    return render(request,'task/clients-list.html', {'Clientes':Clientes}) #, {'user':user})


def Spreadsheet(request):

    return render(request,'task/carga-plan.html')

def CreateDB(request):

    read_item = CODE.creat_sub_item()

    for i in read_item[0][0]:
        CODE.insert_ag(str(i), '', date_today)

    for i in read_item[0][1]:
        CODE.insert_prod(i, '', date_today)

    for i in read_item[0][2]:
        CODE.insert_seg_type(i, '', date_today)
    
    for i in read_item[0][3]:
        CODE.insert_renew(i, '', date_today)

    #-----------
    read_df = CODE.read_all()
    read_all = CODE.read_sql_all()
    
    read_ag = CODE.read_sql('task_agency')
    read_prod = CODE.read_sql('task_product')
    read_sec = CODE.read_sql('task_secure')
    read_renew = CODE.read_sql('task_renew')

    for a in read_df.index:
        for b in read_ag.index:
            if read_ag['name_agency'].loc[b] == str(read_df['AG'].loc[a]):
                ag = read_ag['id'].loc[b]

        for c in read_prod.index:
            if read_prod['name_product'].loc[c] == read_df['PRODUTO'].loc[a]:
                prod = read_prod['id'].loc[c]

        for d in read_sec.index:
            if read_sec['name_secure'].loc[d] == read_df['TIPO_SEGURO'].loc[a]:
                sec = read_sec['id'].loc[d]

        for e in read_renew.index:
            if read_renew['name_renew'].loc[e] == read_df['REN'].loc[a]:
                ren = read_renew['id'].loc[e]

        if len(str(read_df['CPF'].loc[a])) > 12:
            cnpj = read_df['CPF'].loc[a]
            cpf = ''
        else:
            cpf = read_df['CPF'].loc[a]
            cnpj = ''

        CODE.insert_clientes(read_df['NOME_CLIENTE'].loc[a],ren,cpf,cnpj,prod,ag,sec,read_df['CORRETOR'].loc[a], \
        '',read_df['APOLICE'].loc[a],read_df['VALOR'].loc[a],read_df['TEL1'].loc[a],read_df['TEL2'].loc[a], \
        read_df['CEL1'].loc[a], read_df['CEL2'].loc[a],'',read_df['OBS'].loc[a], \
        datetime.strptime(str(read_df['DATA'].loc[a]), '%Y-%m-%d %H:%M:%S').date(),date_today)

    return render(request,'task/clients-list.html')


