# Generated by Django 2.1.1 on 2018-09-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180930_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete='CASCADE', related_name='images', to='projects.Project'),
        ),
    ]
