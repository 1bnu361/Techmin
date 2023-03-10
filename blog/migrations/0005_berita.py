# Generated by Django 4.1.2 on 2022-12-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_artikel_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('thumb', models.URLField(blank=True, null=True)),
                ('author', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('key', models.CharField(max_length=255)),
            ],
        ),
    ]
