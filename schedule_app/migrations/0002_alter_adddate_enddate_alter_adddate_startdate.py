# Generated by Django 4.0.5 on 2022-06-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddate',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='adddate',
            name='startdate',
            field=models.DateField(null=True),
        ),
    ]