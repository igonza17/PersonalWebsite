# Generated by Django 3.0.8 on 2020-07-16 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200716_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_id',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='course_id',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='prereq1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='prereq2',
            field=models.IntegerField(max_length=100),
        ),
    ]
