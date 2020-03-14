#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: test_name_function.py
# Created on : 2020-03-14 19:53:53
# Author: cogito0823
# Last Modified: 2020-03-14 19:53:53
# Description:
#########################################################################

import unittest
from name_function import *

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确处理姓名吗？"""
        formatted_name = get_formatted_name('aaas','sede')
        self.assertEqual(formatted_name,'Aaas Sede')
        
unittest.main()