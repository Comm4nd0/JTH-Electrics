# Generated by Django 2.1.1 on 2018-09-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180930_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete='CASCADE', related_name='images', to='projects.Project'),
        ),
    ]
