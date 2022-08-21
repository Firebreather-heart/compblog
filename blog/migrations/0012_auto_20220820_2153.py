# Generated by Django 3.2.8 on 2022-08-20 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_post_synopsis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('news', 'News'), ('tech', 'Tech'), ('lifestyle', 'Lifestyle'), ('entertainment', 'Entertainment'), ('fashion', 'Fashion'), ('career', 'career'), ('general', 'General')], default='general', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
