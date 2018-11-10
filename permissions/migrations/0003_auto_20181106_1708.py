# Generated by Django 2.1.3 on 2018-11-06 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_auto_20181106_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinvitation',
            name='invited_user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectinvitation',
            name='project',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='permissions.Project'),
        ),
    ]
