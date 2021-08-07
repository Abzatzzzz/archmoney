# Generated by Django 3.2.5 on 2021-07-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
