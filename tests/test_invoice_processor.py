import unittest
import json
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from invoice_processor import extract_invoice_data, is_valid_invoice_format

class TestInvoiceProcessor(unittest.TestCase):

    def test_is_valid_invoice_format(self):
        valid_invoice = {
            "vendor": {"name": "Test Vendor"},
            "bill_to": {"name": "Test Customer"},
            "invoice_number": "INV001",
            "date": "2023-05-20",
            "line_items": [
                {"sku": "ITEM1", "description": "Test Item", "quantity": 1, "tax_rate": 0.1, "price": 100, "total": 110}
            ]
        }
        self.assertTrue(is_valid_invoice_format(valid_invoice))

        invalid_invoice = {
            "vendor": {"name": "Test Vendor"},
            "bill_to": {"name": "Test Customer"},
            "invoice_number": "INV001",
            # Missing date and line_items
        }
        self.assertFalse(is_valid_invoice_format(invalid_invoice))

    def test_extract_invoice_data(self):
        input_json = {
            "vendor": {"name": "Test Vendor", "address": "123 Test St"},
            "bill_to": {"name": "Test Customer"},
            "invoice_number": "INV001",
            "date": "May 20, 2023",
            "line_items": [
                {"sku": "ITEM1", "description": "Test Item", "quantity": 1, "tax_rate": 0.1, "price": 100, "total": 110}
            ]
        }
        
        expected_output = {
            "vendor_name": "Test Vendor",
            "vendor_address": "123 Test St",
            "bill_to_name": "Test Customer",
            "invoice_number": "INV001",
            "date": "2023-05-20",
            "line_items": [
                {"sku": "ITEM1", "description": "Test Item", "quantity": 1, "tax_rate": 0.1, "price": 100, "total": 110}
            ]
        }
        
        self.assertEqual(extract_invoice_data(input_json), expected_output)

    def test_extract_invoice_data_invalid_format(self):
        invalid_input = {
            "vendor": {"name": "Test Vendor"},
            # Missing required fields
        }
        
        with self.assertRaises(ValueError):
            extract_invoice_data(invalid_input)

if __name__ == '__main__':
    unittest.main()