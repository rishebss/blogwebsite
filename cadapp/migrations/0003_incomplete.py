# Generated by Django 5.0.6 on 2024-06-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadapp', '0002_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incomplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='gallery')),
                ('title', models.CharField(max_length=700)),
                ('location', models.CharField(max_length=500)),
            ],
        ),
    ]
