# Generated by Django 2.2.10 on 2020-06-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IIN', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
