# Generated by Django 4.1.6 on 2023-02-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_post_phrase_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phrase',
            field=models.TextField(),
        ),
    ]