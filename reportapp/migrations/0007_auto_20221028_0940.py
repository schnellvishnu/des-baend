# Generated by Django 3.2.16 on 2022-10-28 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0006_auto_20221027_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionreport',
            old_name='accepted',
            new_name='Accepted',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='challenged',
            new_name='Challenged',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='damaged',
            new_name='Damaged',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='in_process',
            new_name='InProcess',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='rejected_by_camera',
            new_name='RejectedByCamera',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='sample',
            new_name='Sample',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='specimen',
            new_name='Specimen',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='teach',
            new_name='Teach',
        ),
        migrations.RenameField(
            model_name='productionreport',
            old_name='unused',
            new_name='Unused',
        ),
    ]