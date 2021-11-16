# Generated by Django 3.2.9 on 2021-11-16 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_agency', models.CharField(max_length=255, verbose_name='ANGÊNCIAS')),
                ('comments', models.TextField(blank=True, verbose_name='OBS')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='TIPOS DE PRODUTO')),
                ('comments', models.TextField(blank=True, verbose_name='OBS')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Renew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_renew', models.CharField(max_length=255, verbose_name='TIPOS DE SEGUROS')),
                ('comments', models.TextField(blank=True, verbose_name='OBS')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_secure', models.CharField(max_length=255, verbose_name='TIPOS DE SEGUROS')),
                ('comments', models.TextField(blank=True, verbose_name='OBS')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arq', models.FileField(help_text='localizar Arquivo', upload_to='uploads/')),
                ('update_arq', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='NOME DO CLIENTE')),
                ('cpf', models.CharField(blank=True, max_length=11, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=14, verbose_name='CNPJ')),
                ('conta', models.CharField(blank=True, max_length=20, verbose_name='NÚMERO DA CONTA')),
                ('gerency', models.CharField(blank=True, max_length=255, verbose_name='NOME DO GERENTE')),
                ('policy', models.CharField(max_length=30, verbose_name='NÚMERO DA APOLICE')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='VALOR PAGO')),
                ('tel1', models.CharField(blank=True, max_length=10, verbose_name='TELEFONE OPÇÃO 1')),
                ('tel2', models.CharField(blank=True, max_length=10, verbose_name='TELEFONE OPÇÃO 2')),
                ('cel1', models.CharField(blank=True, max_length=11, verbose_name='CELULAR OPÇÃO 1')),
                ('cel2', models.CharField(blank=True, max_length=11, verbose_name='CELULAR OPÇÃO 2')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='E-MAIL')),
                ('comments', models.TextField(blank=True, verbose_name='OBS')),
                ('date_contract', models.DateField(blank=True, null=True, verbose_name='DATA SEGURO')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.agency', verbose_name='AGÊNCIA')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.product', verbose_name='PRODUTO')),
                ('renew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.renew', verbose_name='RENOVAÇÃO')),
                ('secure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.secure', verbose_name='SEGURO')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_complet', models.CharField(max_length=255, verbose_name='NOME USUÁRIO')),
                ('photo', models.FileField(help_text='ARQUIVO FOTO', upload_to='uploads/')),
                ('name_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
