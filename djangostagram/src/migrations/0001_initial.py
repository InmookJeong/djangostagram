# Generated by Django 4.0.5 on 2022-06-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dsuser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
