# Generated by Django 2.2 on 2020-06-02 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_site_app', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_likes',
            field=models.ManyToManyField(related_name='liked_posts', to='collectors_site_app.User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='collectors_site_app.Post')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='collectors_site_app.User')),
            ],
        ),
    ]