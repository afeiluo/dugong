# Generated by Django 2.2.10 on 2020-03-06 06:20

import apps.images.handlers
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import json.encoder
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exif',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=json.encoder.JSONEncoder),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(height_field='height', upload_to=apps.images.handlers.hexdigest_filename, width_field='width')),
                ('width', models.IntegerField(default=0, editable=False)),
                ('height', models.IntegerField(default=0, editable=False)),
                ('description', models.TextField(blank=True, default='')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='photos.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.Category'),
        ),
    ]
