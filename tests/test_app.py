import json

from source import app


def test_base():
    """
    Test that it can sum a list of integers
    """
    event = {}
    context = {}
    result = app.handler(event, context)
    base_result = {"statusCode": 20, "body": json.dumps("Hello from Lambda!")}
    assert result == base_result

def test_base2():
    """
    Test that it can sum a list of integers
    """
    event = {}
    context = {}
    result = app.handler(event, context)
    base_result = {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
    assert result == base_result