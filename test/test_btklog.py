#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import datetime
from click.testing import CliRunner
from btklog import *


def test_btklog():
    """Test main functionality"""
    runner = CliRunner()
    result = runner.invoke(btklog, ['-k', 'test/dhcpd.leases', '-h', 'test'])
    assert result.exit_code == 0
    assert u'log dosya' in result.output


class TestBtkLog(unittest.TestCase):
    def test_align(self):
        """
        Test that it can add 3 whitespaces to end of the string 'foo'
        """
        data = "foo"
        result = align(data, 3)
        self.assertEqual(result, "foo   ")


    def test_date_format(self):
        """
        Test 'date_format' function
        """
        data = datetime.datetime(2017, 11, 28, 23, 55, 59)
        result =  date_format(data)
        self.assertEqual(result, "28.11.2017-23:55:59")


    def test_ip_format(self):
        """
        Test 'ip_format' function
        """
        data = "192.168.1.21"
        result =  ip_format(data)
        self.assertEqual(result, "192.168.1.21        ")


    def test_mac_format(self):
        """
        Test 'mac_format' function
        """
        data = "00:0c:29:b6:53:f1"
        result =  mac_format(data)
        self.assertEqual(result, "00-0c-29-b6-53-f1")
