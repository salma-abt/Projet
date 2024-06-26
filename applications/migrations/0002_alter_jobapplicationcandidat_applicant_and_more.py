# Generated by Django 5.0.6 on 2024-06-02 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTH_APP', '0001_initial'),
        ('applications', '0001_initial'),
        ('offre_demande', '0003_alter_posseder_niveau_metrise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplicationcandidat',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH_APP.candidat'),
        ),
        migrations.AlterField(
            model_name='jobapplicationcandidat',
            name='job_offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offre_demande.offredemploi'),
        ),
        migrations.AlterField(
            model_name='jobapplicationrecruter',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH_APP.recruteur'),
        ),
        migrations.AlterField(
            model_name='jobapplicationrecruter',
            name='job_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offre_demande.demandedemploi'),
        ),
    ]
