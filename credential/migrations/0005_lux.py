# Generated by Django 5.0.2 on 2024-06-10 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0004_cad_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luxtitle', models.CharField(max_length=250)),
                ('luximg', models.ImageField(upload_to='gallery')),
                ('luximgs', models.ImageField(upload_to='gallery')),
                ('luximgss', models.ImageField(upload_to='gallery')),
                ('luxdesc', models.CharField(max_length=750)),
                ('luxloc', models.CharField(max_length=250)),
            ],
        ),
    ]