# Generated by Django 3.0.5 on 2020-04-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='USN',
            field=models.CharField(max_length=30),
        ),
    ]
