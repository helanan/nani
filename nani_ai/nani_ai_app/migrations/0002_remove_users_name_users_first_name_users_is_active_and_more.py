# Generated by Django 5.2.4 on 2025-07-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nani_ai_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
