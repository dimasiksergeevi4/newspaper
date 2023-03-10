# Generated by Django 4.1.3 on 2022-12-21 01:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_alter_post_type_of_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='rating_author',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='id_category', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating_comment',
            field=models.IntegerField(db_column='rating', default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(db_column='rating', default=0),
        ),
    ]
