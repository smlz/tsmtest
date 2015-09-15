## Django-Extensions 1.5.6 TimeStampedModel Migration Error Sample App

### Installation Steps


#### All by Hand
```
virtualenv tsmtest-env
source tsmtest-env/bin/activate
pip install Django==1.8.4
django-admin startproject tsmtest
cd tsmtest
./manage.py startapp myapp

cat > requirements.txt <<EOF
Django==1.8.4
django-extensions==1.5.5
EOF

pip install -r requirements.txt

cat > myapp/models.py <<EOF
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class MyTimeStampedModel(TimeStampedModel):
    some_other_field = models.IntegerField()
EOF

cat >> tsmtest/settings.py <<EOF

INSTALLED_APPS += ('django_extensions', 'myapp')
EOF

./manage.py makemigrations

./manage.py migrate

```

#### Or easier, using this git repository:
```
virtualenv tsmtest-env
source tsmtest-env/bin/activate
git clone https://github.com/smlz/tsmtest.git
cd tsmtest
pip install -r requirements.txt
```

Okay, now we are set!

### Update and generate migrations

First, update `django_extensions` to 1.5.6:
```
$ pip install django_extensions==1.5.6
```

Second, `./manage.py migrate` tells us that there are changes in the models:
```
$ ./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, django_extensions, messages
  Apply all migrations: admin, contenttypes, myapp, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  No migrations to apply.
  Your models have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
```

Third, when trying to generate the migration files we get an error message:
```
$ ./manage.py makemigrations 
Migrations for 'myapp':
  0002_auto_20150915_1007.py:
    - Alter field created on mytimestampedmodel
    - Alter field modified on mytimestampedmodel
Traceback (most recent call last):
  File "./manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 338, in execute_from_command_line
    utility.execute()
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 330, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/base.py", line 393, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/base.py", line 444, in execute
    output = self.handle(*args, **options)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/commands/makemigrations.py", line 143, in handle
    self.write_migration_files(changes)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/core/management/commands/makemigrations.py", line 171, in write_migration_files
    migration_string = writer.as_string()
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 166, in as_string
    operation_string, operation_imports = OperationWriter(operation).serialize()
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 124, in serialize
    _write(arg_name, arg_value)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 87, in _write
    arg_string, arg_imports = MigrationWriter.serialize(_arg_value)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 377, in serialize
    return cls.serialize_deconstructed(path, args, kwargs)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 268, in serialize_deconstructed
    arg_string, arg_imports = cls.serialize(arg)
  File "/home/marco/code/tsmtest-env/local/lib/python2.7/site-packages/django/db/migrations/writer.py", line 465, in serialize
    "topics/migrations/#migration-serializing" % (value, get_docs_version())
ValueError: Cannot serialize: <class django.db.models.fields.NOT_PROVIDED at 0x7fc78ba416d0>
There are some values Django cannot serialize into migration files.
For more, see https://docs.djangoproject.com/en/1.8/topics/migrations/#migration-serializing
```
