# Generated by Django 3.2.8 on 2022-08-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220819_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='synopsis',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
