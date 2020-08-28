# Generated by Django 3.0.7 on 2020-08-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_downlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducatorsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educators_name', models.CharField(max_length=200)),
                ('educators_email', models.EmailField(max_length=254)),
                ('educators_no', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'educatorsData',
            },
        ),
    ]
