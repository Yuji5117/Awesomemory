# Generated by Django 2.2.6 on 2020-01-24 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200121_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='カテゴリー'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
