# Generated by Django 3.2.9 on 2021-11-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_alter_master_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
