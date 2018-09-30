# Generated by Django 2.1.1 on 2018-09-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180929_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='date',
            field=models.DateField(default='2018-09-05'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='property',
            field=models.ForeignKey(on_delete='CASCADE', related_name='images', to='projects.Project'),
        ),
    ]
