# Generated by Django 3.0.7 on 2020-08-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200818_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='downlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downlink_title', models.CharField(max_length=200)),
                ('downlink_published', models.DateTimeField(verbose_name='date published')),
                ('downlink_slug', models.CharField(default=1, max_length=200)),
            ],
        ),
    ]
