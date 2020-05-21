# Generated by Django 2.2.8 on 2020-03-28 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('trending_id', models.IntegerField(primary_key=True, serialize=False)),
                ('trending_title', models.CharField(max_length=500)),
                ('trending_logo', models.FileField(upload_to='')),
                ('trending_author', models.CharField(max_length=500)),
                ('trending_date', models.CharField(max_length=500)),
                ('trending_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('tech_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tech_title', models.CharField(max_length=500)),
                ('tech_logo', models.FileField(upload_to='')),
                ('tech_author', models.CharField(max_length=500)),
                ('tech_date', models.CharField(max_length=500)),
                ('tech_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Hotnews',
            fields=[
                ('hotnews_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hotnews_title', models.CharField(max_length=500)),
                ('hotnews_logo', models.FileField(upload_to='')),
                ('hotnews_author', models.CharField(max_length=500)),
                ('hotnews_date', models.CharField(max_length=500)),
                ('hotnews_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('editor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('editor_summary', models.CharField(max_length=1000000)),
                ('editor_title', models.CharField(max_length=500)),
                ('editor_logo', models.FileField(upload_to='')),
                ('editor_author', models.CharField(max_length=500)),
                ('editor_date', models.CharField(max_length=500)),
                ('editor_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_text', models.CharField(max_length=1000000)),
                ('article_title', models.CharField(max_length=500)),
                ('article_logo', models.FileField(upload_to='')),
                ('author', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=500)),
                ('article_summary', models.CharField(max_length=50000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
    ]
