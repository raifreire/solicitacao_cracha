# Generated by Django 4.2 on 2023-06-08 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0007_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cracha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_completo', models.CharField(max_length=150)),
                ('rg', models.TextField(max_length=150)),
                ('cpf', models.CharField(max_length=150)),
                ('funcao', models.TextField(choices=[('REPRESENTANTE', 'REPRESENTANTE COMERCIAL'), ('ESTAGIARIO', 'ESTAGIARIO'), ('ADMINISTRATIVO', 'ASSISTENTE ADMINISTRATIVO'), ('SUPERVISOR', 'SUPERVISOR COMERCIAL')], default='', max_length=150)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('publicada', models.BooleanField(default=True)),
                ('data_cracha', models.DateTimeField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Fotografia',
        ),
    ]