# Generated by Django 3.0.5 on 2020-04-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='related_image',
            field=models.ImageField(null=True, upload_to='post', verbose_name='imágen relacionada'),
        ),
    ]
