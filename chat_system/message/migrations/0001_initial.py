# Generated by Django 5.0.6 on 2024-05-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('sender', models.CharField(max_length=30)),
                ('reciver', models.CharField(max_length=30)),
            ],
        ),
    ]
