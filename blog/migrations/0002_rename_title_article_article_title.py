# Generated by Django 4.2.2 on 2023-07-03 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='article_title',
        ),
    ]
