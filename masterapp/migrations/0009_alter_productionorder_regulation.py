# Generated by Django 3.2.16 on 2022-11-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0008_alter_productionorder_regulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='regulation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
