# Generated by Django 3.2.18 on 2023-04-27 11:20

from django.db import migrations
import imagekit.models.fields
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=posts.models.Post.post_image_path),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=posts.models.Review.review_image_path),
        ),
    ]
