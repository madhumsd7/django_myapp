# Generated by Django 2.0.13 on 2019-08-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
