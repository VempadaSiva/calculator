import unittest
from api_service import fetch_data
from unittest.mock import patch

class Test_mock_fetch_data(unittest.TestCase):
    @patch('api_service.requests.get')
    def test_fetch_data_success(self,mock_get):
        response = {'success'}
        mock_get.return_value.status_code =200
        mock_get.return_value.json.return_value=response

        result = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
        self.assertEqual(result,response)
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1")

    @patch('api_service.requests.get')
    def test_fetch_data_failed(self,mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None
        result = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
        self.assertEqual(result,None)
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1")


if __name__ == '__main__':
    unittest.main()