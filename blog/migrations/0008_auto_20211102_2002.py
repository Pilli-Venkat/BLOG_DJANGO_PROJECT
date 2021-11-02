# Generated by Django 3.2.7 on 2021-11-02 14:32

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
