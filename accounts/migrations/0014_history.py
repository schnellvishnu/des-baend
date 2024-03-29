# Generated by Django 3.2.5 on 2022-12-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_register_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelName', models.CharField(max_length=100)),
                ('savedID', models.CharField(max_length=100)),
                ('operationDone', models.CharField(max_length=100)),
                ('doneByUser', models.CharField(max_length=100)),
                ('doneByUserRole', models.CharField(max_length=100)),
                ('doneDateTime', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
