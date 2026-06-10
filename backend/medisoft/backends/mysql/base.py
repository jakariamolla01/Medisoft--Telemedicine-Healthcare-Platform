from django.db.backends.mysql import base as mysql_base
from django.db.backends.mysql import features as mysql_features
from django.db.backends.mysql import operations as mysql_ops


class DatabaseFeatures(mysql_features.DatabaseFeatures):

    can_return_columns_from_insert = False
    can_return_rows_from_bulk_insert = False
    can_return_rows_from_update = False

    @property
    def supports_returning(self):
        return False


class DatabaseOperations(mysql_ops.DatabaseOperations):


    @property
    def returning_clause(self):
        return ""


class DatabaseWrapper(mysql_base.DatabaseWrapper):
    """Drop-in replacement that uses our patched features / operations
    and bypasses the MariaDB 10.6+ version check."""

    features_class = DatabaseFeatures
    ops_class = DatabaseOperations

    def check_database_version_supported(self):
        """No-op: skip the MariaDB >= 10.6 version check."""
        pass
