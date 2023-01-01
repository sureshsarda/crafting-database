from behave import *
from btrees import BTree

@given('we have a non empty btree')
def step_impl(context):
    pass

@when('we try to find an element')
def step_impl(context):
    assert True is not False

@then('it returns the element pointer and the node that contains it')
def step_impl(context):
    assert context.failed is False