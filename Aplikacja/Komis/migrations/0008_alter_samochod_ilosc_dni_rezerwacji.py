# Generated by Django 4.1.3 on 2022-12-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Komis', '0007_rename_iloscdnirezerwacji_samochod_ilosc_dni_rezerwacji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samochod',
            name='ilosc_dni_rezerwacji',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
