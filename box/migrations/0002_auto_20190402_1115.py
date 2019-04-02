# Generated by Django 2.1.7 on 2019-04-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buginfo',
            name='createTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='description',
            field=models.TextField(default=1554203679000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='endTime',
            field=models.BigIntegerField(default=1554203679000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='influenceRange',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='influenceType',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='lastModifyTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='moreReason',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='notifyType',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='process',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buginfo',
            name='startTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='actualFinishTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='createTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='expectFinishTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='lastModifyTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='creatTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='lastModifyTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='firstLoginTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastLoginTime',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
