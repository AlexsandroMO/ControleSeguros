from django.db import models
from django.contrib.auth import get_user_model

class AuthUser(models.Model): #Títulos de projeto

    name_complet = models.CharField(max_length=255, verbose_name='NOME USUÁRIO')
    name_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    photo = models.FileField(upload_to='uploads/', help_text='ARQUIVO FOTO')

    def __str__(self):
        return self.name_complet


class Product(models.Model): #Títulos de projeto

    name_product = models.CharField(max_length=255, verbose_name='TIPOS DE PRODUTO')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_product


class Agency(models.Model): #Títulos de projeto

    name_agency = models.CharField(max_length=255, verbose_name='ANGÊNCIAS')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_agency

class Secure(models.Model): #Títulos de projeto

    name_secure = models.CharField(max_length=255, verbose_name='TIPOS DE SEGUROS')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_secure


class Renew(models.Model): #Títulos de projeto

    name_renew = models.CharField(max_length=255, verbose_name='TIPOS DE SEGUROS')
    comments = models.TextField(blank=True, null=False,verbose_name='OBS')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_renew


class Cliente(models.Model): #Títulos de projeto

    name = models.CharField(max_length=255, verbose_name='NOME DO CLIENTE')
    renew = models.ForeignKey(Renew, on_delete=models.CASCADE, verbose_name='RENOVAÇÃO')
    cpf = models.CharField(max_length=11, blank=True, null=False, verbose_name='CPF')
    #cpf = CPFField('cpf', blank=True, null=False, verbose_name='CPF')
    cnpj = models.CharField(max_length=14, blank=True, null=False, verbose_name='CNPJ')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUTO')
    agency =models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name='AGÊNCIA')
    conta = models.CharField(max_length=20, blank=True, null=False, verbose_name='NÚMERO DA CONTA')
    gerency = models.CharField(max_length=255, blank=True, null=False, verbose_name='NOME DO GERENTE')
    secure = models.ForeignKey(Secure, on_delete=models.CASCADE, verbose_name='SEGURO')
    policy = models.CharField(max_length=30, verbose_name='NÚMERO DA APOLICE')
    amount_paid = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='VALOR PAGO') #default_currency='BRA'
    tel1 = models.CharField(max_length=10, blank=True, null=False, verbose_name='TELEFONE OPÇÃO 1')
    tel2 = models.CharField(max_length=10, blank=True, null=False, verbose_name='TELEFONE OPÇÃO 2')
    cel1 = models.CharField(max_length=11, blank=True, null=False, verbose_name='CELULAR OPÇÃO 1')
    cel2 = models.CharField(max_length=11, blank=True, null=False, verbose_name='CELULAR OPÇÃO 2')
    email = models.CharField(max_length=255, blank=True, null=False, verbose_name='E-MAIL')
    comments = models.TextField(blank=True, null=False, verbose_name='OBS')
    date_contract = models.DateField(blank=True, null=True, verbose_name='DATA SEGURO')
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/', help_text='localizar Arquivo')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)


'''
class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')
    emp_office = models.CharField(max_length=255, verbose_name='FUNÇÃO')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name


class ProjControl(models.Model): #Tabela = Lista de Documentos LD
    
    proj_name = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DO DOCUMENTO')
    doc_number = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='NÚMERO DO DOCUMENTO')
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='resp', verbose_name='RESPONSÁVEL')
    elab = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='elab', verbose_name='ELABORADOR')
    verif = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='verif', verbose_name='VERIFICADOR')
    aprov = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='aprov', verbose_name='APROVADOR')
    emiss = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='emiss', verbose_name='EMISSOR')
    status = models.ForeignKey(StatusDoc, on_delete=models.CASCADE, blank=True, null=True, verbose_name='STATUS')
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True, verbose_name='AÇÃO')
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    comments = models.TextField()
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)


'''

