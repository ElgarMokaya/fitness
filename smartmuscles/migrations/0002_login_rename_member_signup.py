# Generated by Django 4.1.7 on 2023-02-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartmuscles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Member',
            new_name='Signup',
        ),
    ]
