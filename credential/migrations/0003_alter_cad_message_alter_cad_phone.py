# Generated by Django 5.0.6 on 2024-06-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0002_alter_cad_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad',
            name='message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cad',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
