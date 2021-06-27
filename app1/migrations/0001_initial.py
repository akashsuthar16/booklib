# Generated by Django 2.0 on 2021-06-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='Firstname', max_length=255)),
                ('lname', models.CharField(default='Lastname', max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('passwd', models.CharField(default='Password', max_length=255)),
            ],
        ),
    ]
