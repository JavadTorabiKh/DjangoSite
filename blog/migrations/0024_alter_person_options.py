# Generated by Django 4.2.3 on 2023-10-29 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_person_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['age']},
        ),
    ]