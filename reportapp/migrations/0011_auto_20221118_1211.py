# Generated by Django 3.2.16 on 2022-11-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0010_auto_20221103_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionreport',
            name='A',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Accept',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='B',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='C',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Chall',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='D',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Dam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='E',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='F',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='G',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='H',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='I',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='InPro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Rejected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Samp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Spec',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Tea',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productionreport',
            name='Unuse',
            field=models.IntegerField(default=0),
        ),
    ]
