# Generated by Django 2.1.5 on 2019-04-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_allot', '0010_auto_20190406_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='pref_1',
            field=models.CharField(default='0', max_length=200, verbose_name='Preference 1'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='pref_2',
            field=models.CharField(default='0', max_length=200, verbose_name='Preference 2'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='pref_3',
            field=models.CharField(default='0', max_length=200, verbose_name='Preference 3'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='0', max_length=100, verbose_name='Email of Student'),
        ),
    ]