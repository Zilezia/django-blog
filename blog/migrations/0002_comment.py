# Generated by Django 5.0.3 on 2024-03-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=500)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
