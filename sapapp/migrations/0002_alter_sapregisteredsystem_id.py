# Generated by Django 3.2.16 on 2022-11-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sapregisteredsystem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]