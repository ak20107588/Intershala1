# Generated by Django 2.2 on 2023-08-22 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='UserId',
            new_name='UserID',
        ),
    ]
