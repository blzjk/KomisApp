# Generated by Django 4.1.3 on 2022-12-18 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Komis', '0017_remove_samochod_data_dodania_samochod_data_wynajecia'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='data_dodania',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='data_wynajecia',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
