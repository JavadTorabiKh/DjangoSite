# Generated by Django 4.2.1 on 2023-05-15 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topics')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
