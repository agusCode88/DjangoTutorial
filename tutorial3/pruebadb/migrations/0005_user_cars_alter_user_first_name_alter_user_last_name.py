# Generated by Django 4.2.2 on 2023-06-23 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebadb', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='pruebadb.car', verbose_name='Los carro del usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='el nombre de la persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='el apellido de la persona'),
        ),
    ]
