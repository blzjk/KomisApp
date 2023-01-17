# Generated by Django 4.1.3 on 2023-01-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Komis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='przebieg',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='foto',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='numer_rejestracyjny',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='numer_seryjny',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]