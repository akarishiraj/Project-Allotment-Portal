# Generated by Django 2.1.5 on 2019-04-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof_add', '0002_professor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AddField(
            model_name='professor',
            name='groups_assigned',
            field=models.CharField(default='0,', max_length=200, verbose_name='Groups Assigned'),
        ),
        migrations.AddField(
            model_name='professor',
            name='nog_assigned',
            field=models.IntegerField(default=0, verbose_name='No. of groups assigned'),
        ),
    ]
