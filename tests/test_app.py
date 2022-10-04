import unittest
import json

from source import app


class TestHandler(unittest.TestCase):
    def test_base(self):
        """
        Test that it can sum a list of integers
        """
        event = {}
        context = {}
        result = app.handler(event, context)
        base_result = {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
        self.assertEqual(result, base_result)


if __name__ == "__main__":
    unittest.main()
