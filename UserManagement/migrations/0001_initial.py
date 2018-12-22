# Generated by Django 2.1.3 on 2018-12-22 12:54

import UserManagement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('registration_datetime', models.DateTimeField(auto_now=True)),
                ('profile_img', models.URLField(blank=True, max_length=10000, null=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', UserManagement.models.MyUserManager()),
            ],
        ),
    ]
