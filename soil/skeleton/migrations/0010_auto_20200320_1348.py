# Generated by Django 2.2.3 on 2020-03-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0009_auto_20200320_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='emitter_spacing',
            field=models.FloatField(blank=True, null=True, verbose_name='Emitter Spacing (Meters)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='plant_spacing',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant Spacing (Meters)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='row_spacing',
            field=models.FloatField(blank=True, null=True, verbose_name='Row Spacing (Meters)'),
        ),
    ]
