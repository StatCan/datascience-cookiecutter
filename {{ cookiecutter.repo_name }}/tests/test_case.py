#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

def test_case_1(datadir):
    """Test Case 1 using datadir fixture defined in conftest.py"""
    assert os.path.exists(datadir.join('file1.txt'))

def test_case_2(datadir):
    """Test Case 2 using datadir fixture defined in conftest.py"""
    # prefered way
    assert os.path.exists(datadir.join('subfolder','file2.txt')) 
    # possible
    assert os.path.exists(datadir.join('subfolder/file2.txt'))   