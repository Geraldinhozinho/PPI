# Generated by Django 5.0.3 on 2024-03-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('ativo', models.BooleanField()),
                ('nome_mae', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=20)),
                ('idade', models.IntegerField()),
            ],
        ), 
    ]
