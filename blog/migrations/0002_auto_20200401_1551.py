# Generated by Django 2.2.8 on 2020-04-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='editor_url',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotnews',
            name='hotnews_url',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tech',
            name='hotnews_url',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trending',
            name='trending_url',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
