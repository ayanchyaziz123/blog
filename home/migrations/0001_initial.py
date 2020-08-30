# Generated by Django 3.0.7 on 2020-07-28 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('siNo', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=100)),
                ('TellUs', models.TextField()),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('postAuthor', models.CharField(max_length=200)),
                ('postTitle', models.CharField(max_length=200)),
                ('postTimeDate', models.DateTimeField(auto_now_add=True)),
                ('postInC', models.TextField()),
                ('postInCplus', models.TextField()),
                ('postInPython', models.TextField()),
                ('postDescriptions', models.TextField()),
                ('postUrl', models.TextField(blank=True)),
                ('postImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='home.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.Post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
