# Generated by Django 4.2.2 on 2023-06-23 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebadb', '0003_website_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
    ]
