# Generated by Django 2.2 on 2023-08-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_appointment_appointend'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='FirstName',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='LastName',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
