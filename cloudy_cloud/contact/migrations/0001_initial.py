# Generated by Django 3.2.5 on 2021-07-28 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('question_category', models.CharField(max_length=100)),
                ('date_sent', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'messages',
            },
        ),
    ]
