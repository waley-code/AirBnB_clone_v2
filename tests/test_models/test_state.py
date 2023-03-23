#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import MySQLdb
import os


username = os.getenv("HBNB_MYSQL_USER")
password = os.getenv("HBNB_MYSQL_PWD")
dbase = os.getenv("HBNB_MYSQL_DB")


class test_state(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_statetable(self):
        """ """
        db = MySQLdb.connect(user=username, passwd=password, db=dbase)
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM states")
        first_count = cur.fetchone()[0]
        subprocess.run(["create", "State", "name=California"],
                       capture_output=true)
        cur.execute("SELECT COUNT(*) FROM states")
        second_count = cur.fetchone()[0]
        assert second_count - first_count == 1
        db.close()
