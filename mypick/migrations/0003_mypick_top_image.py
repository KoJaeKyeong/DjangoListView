# Generated by Django 3.1.1 on 2020-10-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypick', '0002_remove_mypick_top_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypick',
            name='top_image',
            field=models.URLField(default='', unique=True, verbose_name='Top Image URL'),
        ),
    ]