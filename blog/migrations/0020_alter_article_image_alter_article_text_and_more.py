# Generated by Django 4.2.3 on 2023-09-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_article_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/articles/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default=1, max_length=110),
            preserve_default=False,
        ),
    ]
