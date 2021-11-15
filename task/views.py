from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Agency #Employee, Project, DocumentModel, LdProj, Subject
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

    return render(request,'task/clients-list.html') #, {'user':user})


def Spreadsheet(request):

    read_df = CODE.read_all()
    read_all = CODE.read_sql_all()
    
    read_ag = CODE.read_sql('task_agency')
    read_prod = CODE.read_sql('task_product')
    read_sec = CODE.read_sql('task_secure')
    read_renew = CODE.read_sql('task_renew')

    for a in read_df.index:
        for b in read_ag.index:
            #print('>>>>>', a, read_ag['name_agency'].loc[b], len(read_ag['name_agency'].loc[b]), read_all['AG'].loc[a], len(read_all['AG'].loc[a]))
            if read_ag['name_agency'].loc[b] == str(read_df['AG'].loc[a]):
                #print('OK AG :', a, read_ag['id'].loc[b])
                ag = read_ag['id'].loc[b]

        for c in read_prod.index:
            if read_prod['name_product'].loc[c] == read_df['PRODUTO'].loc[a]:
                #print('OK prod :', a, read_prod['id'].loc[c])
                prod = read_prod['id'].loc[c]

        for d in read_sec.index:
            if read_sec['name_secure'].loc[d] == read_df['TIPO_SEGURO'].loc[a]:
                #print('OK - sec: ', a, read_sec['id'].loc[d])
                sec = read_sec['id'].loc[d]

        for e in read_renew.index:
            if read_renew['name_renew'].loc[e] == read_df['REN'].loc[a]:
                #print('OK renew :', a, read_renew['id'].loc[e])
                ren = read_renew['id'].loc[e]

        if len(str(read_df['CPF'].loc[a])) > 12:
            print('>>>cnpj',read_df['CPF'].loc[a])
        else:
            print('cpf', read_df['CPF'].loc[a])

        print('>>>>',a, ren,prod,read_df['NOME_CLIENTE'].loc[a],sec,read_df['CPF'].loc[a])
        print(ag,read_df['APOLICE'].loc[a],read_df['VALOR'].loc[a],read_df['DATA'].loc[a])
        print(read_df['CORRETOR'].loc[a], read_df['OBS'].loc[a],read_df['TEL1'].loc[a])
        print(read_df['CEL1'].loc[a], read_df['TEL2'].loc[a],read_df['CEL2'].loc[a])
        print('\n')

        #ver se regra de cpf vai pro code o9u fica aqui...  <<<<<<<<<<<<<<<<<<<


        # CODE.insert_clientes(ren,prod,read_df['NOME_CLIENTE'].loc[a],sec,read_df['CPF'].loc[a],
        # ag,read_df['APOLICE'].loc[a],read_df['VALOR'].loc[a],read_df['DATA'].loc[a],
        # read_df['CORRETOR'].loc[a], read_df['OBS'].loc[a],read_df['TEL1'].loc[a],
        # read_df['CEL1'].loc[a], read_df['TEL2'].loc[a],read_df['CEL2'].loc[a])
            
            

    # for i in read_all.index:
    #     print(read_all['name'].loc[i], read_all['renew'].loc[i],read_all['cpf'].loc[i],read_all['cnpj'].loc[i], \
    #     read_all['prod'].loc[i],read_all['agency'].loc[i],read_all['conta'].loc[i], read_all['gerency'].loc[i], \
    #     read_all['secure'].loc[i], read_all['policy'].loc[i],read_all['amount_paid'].loc[i], \
    #     read_all['tel1'].loc[i], read_all['tel2'].loc[i], read_all['cel1'].loc[i], read_all['cel2'].loc[i], \
    #     read_all['email'], read_all['comments'], read_all['date_contract'])

        

        #print(read['REN'].loc[a], read['PRODUTO'].loc[a], read['TIPO_SEGURO'].loc[a], read['REN'].loc[a])

    #print(read)

    return render(request,'task/carga-plan.html')

def CreateDB(request):

    read_item = CODE.creat_sub_item()
    #print(read)
    for i in read_item[0][0]:
        print('>>>>>>>>>>>>>>>>>>', i)
        CODE.insert_ag(str(i), '', date_today)

    for i in read_item[0][1]:
        print('>>>>>>>>>>>>>>>>>>', i)
        CODE.insert_prod(i, '', date_today)

    for i in read_item[0][2]:
        print('>>>>>>>>>>>>>>>>>>', i)
        CODE.insert_seg_type(i, '', date_today)
    
    for i in read_item[0][3]:
        print('>>>>>>>>>>>>>>>>>>', i)
        CODE.insert_renew(i, '', date_today)

    return render(request,'task/clients-list.html')









'''
def NewSegur(request):

    #agency_list = Agency.objects.all()

    if request.method == 'POST':
        form = AgencyForm(request.POST)
        agency_list = form.save(commit=False)

        agency_list.name_agency = ''

        agency_list.save()
        return redirect('/')
'''

'''
if form.is_valid():
    agency_list = form.save(commit=False)
    agency_list.name_agency = ''
    #if task.policy == '0':
        #task.policy = '{}00000000000000000{}'.format(cont_implement, length)
    agency_list.save()
    return redirect('/')'''
    #else:
        #form = AgencyForm()
        #return render(request, 'task/clients-list.html', {'form': form})

