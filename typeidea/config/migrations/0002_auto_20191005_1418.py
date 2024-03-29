# Generated by Django 2.2.5 on 2019-10-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
        migrations.AlterModelOptions(
            name='sidebar',
            options={'verbose_name': '侧边栏', 'verbose_name_plural': '侧边栏'},
        ),
        migrations.RenameField(
            model_name='link',
            old_name='owenr',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='sidebar',
            old_name='created_tiem',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (2, '下线')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论')], default=1, verbose_name='展示类型'),
        ),
    ]
