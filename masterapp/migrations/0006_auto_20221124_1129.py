# Generated by Django 3.2.16 on 2022-11-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0005_auto_20221124_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='productionorder',
            name='packaging_Version',
            field=models.CharField(max_length=40, null=True),
        ),
    ]