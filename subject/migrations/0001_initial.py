# Generated by Django 3.0.5 on 2020-07-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectId', models.AutoField(primary_key=True, serialize=False)),
                ('subjectName', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'Subject_Table',
            },
        ),
    ]
