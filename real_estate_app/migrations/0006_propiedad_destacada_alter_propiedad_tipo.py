# Generated by Django 5.1.3 on 2024-11-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_app', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='destacada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='tipo',
            field=models.CharField(choices=[('venta', 'En Venta'), ('alquiler', 'En Alquiler'), ('construcción', 'En Construcción')], max_length=50),
        ),
    ]
