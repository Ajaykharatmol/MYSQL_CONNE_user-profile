# Generated by Django 3.2.6 on 2021-08-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Degree',
            field=models.CharField(max_length=100),
        ),
    ]
