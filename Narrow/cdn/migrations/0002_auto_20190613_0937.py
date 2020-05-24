# Generated by Django 2.2.2 on 2019-06-13 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='name',
            field=models.TextField(default='<function now at 0x7f2134260158>xDDD', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profileImage', to=settings.AUTH_USER_MODEL),
        ),
    ]