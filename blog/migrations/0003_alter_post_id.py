# Generated by Django 3.2.8 on 2022-08-10 07:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220810_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('adc3447d-5a09-4bd2-b0d0-2b05d2f588fd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
