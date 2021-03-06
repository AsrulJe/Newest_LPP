# Generated by Django 3.2.13 on 2022-05-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('downtime', models.DateTimeField(blank=True, null=True)),
                ('average', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cctv',
            fields=[
                ('cctv_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('iframe', models.CharField(blank=True, max_length=199, null=True)),
            ],
            options={
                'db_table': 'cctv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dryer',
            fields=[
                ('dryer_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_id', models.IntegerField(blank=True, null=True)),
                ('conveyor_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('datecreated', models.DateTimeField()),
                ('data1', models.IntegerField(blank=True, null=True)),
                ('data2', models.IntegerField(blank=True, null=True)),
                ('sampling', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dryer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('elevator_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('sensor_address', models.IntegerField()),
                ('station_id', models.IntegerField()),
                ('site_id', models.IntegerField()),
                ('flag', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'elevator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loglogin',
            fields=[
                ('logid', models.AutoField(db_column='logID', primary_key=True, serialize=False)),
                ('userid', models.IntegerField(db_column='userID')),
                ('datecreated', models.DateTimeField()),
            ],
            options={
                'db_table': 'LogLogin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('operator_id', models.AutoField(primary_key=True, serialize=False)),
                ('operator_name', models.CharField(max_length=255)),
                ('operator_address', models.CharField(max_length=255)),
                ('datecreated', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('date_modified', models.DateTimeField()),
                ('modified_by', models.IntegerField()),
            ],
            options={
                'db_table': 'operator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sens',
            fields=[
                ('sensor_id', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_type', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('datecreated', models.DateTimeField()),
                ('site_id', models.IntegerField()),
                ('dryer_id', models.IntegerField()),
                ('station_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sens',
                'managed': False,
            },
        ),
    ]
