# Generated by Django 5.0.2 on 2024-06-10 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0006_lux_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lux',
            name='luxdesc',
        ),
        migrations.RemoveField(
            model_name='lux',
            name='luxloc',
        ),
        migrations.RemoveField(
            model_name='lux',
            name='luxtitle',
        ),
    ]
