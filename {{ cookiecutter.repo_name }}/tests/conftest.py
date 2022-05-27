#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from py._path.local import LocalPath
from _pytest.fixtures import SubRequest
from distutils import dir_util


@pytest.fixture
def datadir(tmpdir: LocalPath, request: SubRequest) -> LocalPath:
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.

    Allows:
        - generates file path to auxiliar case files.
        - possible concurrent test case access to files
        - prevents modifying the original file by a test case.

    Example:
        Folder structure.
        tests/                # test folder root
            |- conftest.py    # global fixtures automatically imported by pytest
            |- test_case.py   # test file
            |- test_case/     # matching test_case folder containing resources
                |⨽ file1.txt
                |⨽ subfolder/
                     |⨽file2.txt


        # content of test_case.py
        import os
        import pytest

        def test_case_1(datadir):
            full_path = datadir.join('file.txt')
            assert os.path.exists(full_path)

        def test_case_2(datadir):
            assert datadir.join('sub_folder','file2.txt') # prefered
            assert datadir.join('sub_folder/file2.txt')   #possible

    Args:
        tmpdir (LocalPath): global pytest fixture returning the temp
                            directory location where a test is running.
        request (SubRequest): global pytest fixture to access test case
                              metadata

    Returns:
        LocalPath: returning the temp directory location where a test is
                   running. All files in a folder called with the same
                   test case name will be avilable here.
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir

