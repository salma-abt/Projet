# Generated by Django 5.0.6 on 2024-06-01 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recruteur',
            fields=[
                ('id_recruteur', models.AutoField(primary_key=True, serialize=False)),
                ('type_recruteur', models.CharField(choices=[('Entreprise', 'Entreprise'), ('Individuel', 'Individuel')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('num_telephone', models.CharField(max_length=50)),
                ('secteur_activite', models.CharField(max_length=50)),
                ('nom_recruteur', models.CharField(max_length=50)),
                ('presentation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('motdepass', models.CharField(max_length=128)),
                ('is_candidat', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id_candidat', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('num_telephone', models.CharField(max_length=50)),
                ('presentation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('motdepass', models.CharField(max_length=128)),
                ('is_candidat', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
