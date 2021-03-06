#!/usr/bin/env python

"""Tests for `selfish_barnacle` package."""

import pytest


from selfish_barnacle import selfish_barnacle


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_simple_true(response):
    """trivial test"""
    assert(True)
    
def test_another_simple_true2(response):
    """another trivial test"""
    assert(True)

def test_some_barnacle_function(response):
    retval = selfish_barnacle.some_barnacle_function(1)
    assert(2 == retval)
