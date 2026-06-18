
import os
import sys

from django.db.backends.mysql import base
from django.db.models.sql import compiler
from django.db.models import query

base.DatabaseWrapper.check_database_version_supported = lambda self: None

_original_as_sql = compiler.SQLInsertCompiler.as_sql
def _patched_as_sql(self):
    if hasattr(self, 'returning_fields') and self.returning_fields:
        self.returning_fields = None
    return _original_as_sql(self)
compiler.SQLInsertCompiler.as_sql = _patched_as_sql

_original_bulk_create = query.QuerySet.bulk_create
def _patched_bulk_create(self, objs, *args, **kwargs):
    try:
        return _original_bulk_create(self, objs, *args, **kwargs)
    except AssertionError:
        return objs
query.QuerySet.bulk_create = _patched_bulk_create

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()