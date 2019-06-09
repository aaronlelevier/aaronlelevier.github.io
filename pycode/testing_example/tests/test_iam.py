import unittest

from iam import Role


class RoleTests(unittest.TestCase):

    def test_arn(self):
        name = 'rds-monitoring-role'
        role = Role(name=name)

        ret = role.arn

        assert ret == 'arn:aws:iam::123456789:role/rds-monitoring-role'
