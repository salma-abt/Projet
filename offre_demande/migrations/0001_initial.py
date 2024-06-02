# Generated by Django 5.0.6 on 2024-06-01 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AUTH_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id_competence', models.AutoField(primary_key=True, serialize=False)),
                ('nom_competence', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('id_diplome', models.AutoField(primary_key=True, serialize=False)),
                ('nom_diplome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeDEmploi',
            fields=[
                ('id_demande', models.AutoField(primary_key=True, serialize=False)),
                ('date_soumission', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH_APP.candidat')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_catego', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('diplome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offre_demande.diplome')),
            ],
        ),
        migrations.CreateModel(
            name='OffreDEmploi',
            fields=[
                ('id_offre', models.AutoField(primary_key=True, serialize=False)),
                ('titre_poste', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('competence', models.CharField(max_length=50)),
                ('date_publication_present', models.DateField()),
                ('date_limite_candidature', models.DateField()),
                ('salaire_propose', models.PositiveIntegerField()),
                ('recruteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH_APP.recruteur')),
            ],
        ),
        migrations.CreateModel(
            name='Posseder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_metrise', models.CharField(max_length=50)),
                ('candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH_APP.candidat')),
                ('id_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offre_demande.competence')),
            ],
            options={
                'unique_together': {('candidat', 'id_competence')},
            },
        ),
    ]
