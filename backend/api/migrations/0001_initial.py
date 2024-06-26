# Generated by Django 3.2 on 2024-04-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChengduData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChengduQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortoQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='XianData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='XianQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajectory', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='XianResultsERP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='derp', to='api.xiandata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qerp', to='api.xianquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='XianResultsEDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dedr', to='api.xiandata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qedr', to='api.xianquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='XianResultsDTW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ddwt', to='api.xiandata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qdwt', to='api.xianquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortoResultsERP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='derp', to='api.portodata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qerp', to='api.portoquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortoResultsEDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dedr', to='api.portodata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qedr', to='api.portoquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortoResultsDTW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ddwt', to='api.portodata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qdwt', to='api.portoquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChengduResultsERP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='derp', to='api.chengdudata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qerp', to='api.chengduquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChengduResultsEDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dedr', to='api.chengdudata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qedr', to='api.chengduquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChengduResultsDTW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('score', models.FloatField(db_index=True, max_length=100)),
                ('dataid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ddwt', to='api.chengdudata')),
                ('queryid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qdwt', to='api.chengduquery')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
