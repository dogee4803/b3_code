# Generated by Django 5.1.6 on 2025-03-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='images',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='video',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
