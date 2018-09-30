# Generated by Django 2.1.1 on 2018-09-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='main_image',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='property',
            field=models.ForeignKey(on_delete='CASCADE', related_name='images', to='projects.Project'),
        ),
    ]