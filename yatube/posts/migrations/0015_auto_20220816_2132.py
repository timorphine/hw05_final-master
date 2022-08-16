# Generated by Django 2.2.16 on 2022-08-16 21:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0014_auto_20220816_2122'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'author')},
        ),
        migrations.AddIndex(
            model_name='follow',
            index=models.Index(fields=['user', 'author'], name='posts_follo_user_id_13f95c_idx'),
        ),
    ]