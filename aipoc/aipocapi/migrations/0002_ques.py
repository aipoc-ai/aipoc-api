# Generated by Django 3.0.8 on 2021-01-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aipocapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ques',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asked_ques', models.TextField()),
            ],
        ),
    ]
