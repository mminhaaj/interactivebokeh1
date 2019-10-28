#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports

# Module under test
import bokeh.util.dependencies as dep

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class Test_import_optional(object):

    def test_success(self):
        assert dep.import_optional('sys') is not None

    def test_fail(self):
        assert dep.import_optional('bleepbloop') is None

class Test_import_required(object):

    def test_success(self):
        assert dep.import_required('sys', 'yep') is not None

    def test_fail(self):
        with pytest.raises(RuntimeError) as excinfo:
            dep.import_required('bleepbloop', 'nope')
        assert 'nope' in str(excinfo.value)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
