from django.test import TestCase

# Create your tests here.
#{% load crispy_forms_tags %} 







    # if request.method == 'POST':
    #     print('>>>>>>>>>>>>>>>>',request.method)
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newdoc = Document(docfile = request.FILES['docfile'])
    #         newdoc.save()

    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('myapp.views.list'))
    # else:
    #     form = DocumentForm() # A empty, unbound form
    
    # if 'photo' in request.files:
    #     photo = request.files['photo']
    #     print('---------', photo)
    #     if photo.filename != '':
    #         print('foi')
    #         photo.save(os.path.join('static/', photo.filename))



""" 
    CODE.create_table()
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

    ag, prod, sec_, ren = 0,0,0,0
    cpf, cnpj = '',''

    for a in read_df.index:
        for b in read_ag.index:
            if read_ag['name_agency'].loc[b] == str(read_df['AG'].loc[a]):
                ag = read_ag['id'].loc[b]

        for c in read_prod.index:
            if read_prod['name_product'].loc[c] == read_df['PRODUTO'].loc[a]:
                prod = read_prod['id'].loc[c]

        for d in read_sec.index:
            if read_sec['name_secure'].loc[d] == read_df['TIPO_SEGURO'].loc[a]:
                sec_ = read_sec['id'].loc[d]

        for e in read_renew.index:
            if read_renew['name_renew'].loc[e] == read_df['REN'].loc[a]:
                ren = read_renew['id'].loc[e]

        if len(str(read_df['CPF'].loc[a])) > 12:
            cnpj = read_df['CPF'].loc[a]
            cpf = ''
        else:
            cpf = read_df['CPF'].loc[a]
            cnpj = ''

        #----------------------------------------
        if len(str(read_df['TEL1'].loc[a])) == 11:
            cel1 = str(read_df['CEL1'].loc[a])[:-2]
            tel1 = ''
        else:
            tel1 = str(read_df['TEL1'].loc[a])[:-2]
            cel1 = ''
        
        if len(str(read_df['TEL2'].loc[a])) == 11:
            cel2 = str(read_df['CEL2'].loc[a])[:-2]
            tel2 = ''
        else:
            tel2 = str(read_df['TEL2'].loc[a])[:-2]
            cel2 = ''

        if len(str(read_df['CEL1'].loc[a])) == 11:
            cel1 = str(read_df['CEL1'].loc[a])[:-2]
            tel1 = ''
        else:
            tel1 = str(read_df['TEL1'].loc[a])[:-2]
            cel1 = ''
        
        if len(str(read_df['CEL2'].loc[a])) == 11:
            cel2 = str(read_df['CEL2'].loc[a])[:-2]
            tel2 = ''
        else:
            tel2 = str(read_df['TEL2'].loc[a])[:-2]
            cel2 = ''
        #----------------------------------------

        CODE.insert_clientes(read_df['NOME_CLIENTE'].loc[a],ren,cpf,cnpj,prod,ag,sec_,read_df['CORRETOR'].loc[a], \
        '',read_df['APOLICE'].loc[a],read_df['VALOR'].loc[a],tel1,tel2, cel1, cel2,'',read_df['OBS'].loc[a], \
        datetime.strptime(str(read_df['DATA'].loc[a]), '%Y-%m-%d %H:%M:%S').date(),date_today)

    #return render(request,'task/clients-list.html')
    


 """