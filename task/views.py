from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
#from .models import auth_user #Employee, Project, DocumentModel, LdProj, Subject
#from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

@login_required
def home(request):
    #AuthUser = auth_user.objects.all()
    user = request.user

    return render(request,'task/index.html', {'user':user})


@login_required
def clients(request):
    #AuthUser = auth_user.objects.all()
    user = request.user

    return render(request,'task/clients-list.html', {'user':user})