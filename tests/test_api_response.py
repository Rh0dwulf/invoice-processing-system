import unittest
from unittest.mock import patch, mock_open, MagicMock, call
import json
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import api_response

class TestAPIResponse(unittest.TestCase):

    @patch('src.api_response.Client')
    @patch('src.api_response.os.listdir')
    @patch('src.api_response.open', new_callable=mock_open)
    @patch('src.api_response.os.path.isfile', return_value=True)
    @patch('src.api_response.os.makedirs')
    def test_process_documents(self, mock_makedirs, mock_isfile, mock_file, mock_listdir, mock_client):
        # Mock the API client
        mock_client_instance = mock_client.return_value
        mock_client_instance.process_document.return_value = {"invoice_data": "mocked data"}

        # Mock the directory listing
        mock_listdir.return_value = ['doc1.pdf', 'doc2.pdf']

        # Call the function
        api_response.process_documents('input_dir', 'output_dir')

        # Print debug information
        print(f"process_document call count: {mock_client_instance.process_document.call_count}")
        print(f"Mock calls: {mock_client_instance.process_document.mock_calls}")
        print(f"mock_listdir calls: {mock_listdir.mock_calls}")
        print(f"mock_file calls: {mock_file.mock_calls}")
        print(f"mock_isfile calls: {mock_isfile.mock_calls}")

        # Assert that the client was called twice (once for each document)
        self.assertEqual(mock_client_instance.process_document.call_count, 2)

        # Assert that the output file was opened twice (once for each document)
        self.assertEqual(mock_file.call_count, 2)

        # Assert that json.dump was called twice (once for each document)
        expected_calls = [
            call('{'),
            call('\n    '),
            call('"invoice_data"'),
            call(': '),
            call('"mocked data"'),
            call('\n'),
            call('}'),
        ]
        mock_file().write.assert_has_calls(expected_calls * 2, any_order=False)

        # Check that the process_document method was called with the correct arguments
        mock_client_instance.process_document.assert_has_calls([
            call('input_dir\\doc1.pdf', categories=['Logistic', 'Internet', 'Services', 'Telecom', 'Transport']),
            call('input_dir\\doc2.pdf', categories=['Logistic', 'Internet', 'Services', 'Telecom', 'Transport'])
        ])

if __name__ == '__main__':
    unittest.main()