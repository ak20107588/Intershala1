# Generated by Django 2.2 on 2023-08-24 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20230824_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='FirstName',
            new_name='DoctorName',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='LastName',
            new_name='PatientName',
        ),
    ]
