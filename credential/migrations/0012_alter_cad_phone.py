# Generated by Django 5.0.2 on 2024-07-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0011_interior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad',
            name='phone',
            field=models.IntegerField(max_length=15),
        ),
    ]