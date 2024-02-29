# Generated by Django 5.0.2 on 2024-02-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_post_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('AR', 'Article'), ('NW', 'News')], default='AR', max_length=2),
        ),
    ]