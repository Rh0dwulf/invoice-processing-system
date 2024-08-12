import json
import os
from datetime import datetime
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Validate the incoming format
def is_valid_invoice_format(data):
    """
    Check if the JSON data has the expected invoice format.

    Returns a boolean.
    """
    required_keys = {"vendor", "bill_to", "invoice_number", "date", "line_items"} 
    # Required keys we are looking for. It could be an argument of the funtion
    
    if not all(key in data for key in required_keys):
        return False
    
    if not isinstance(data["vendor"], dict) or "name" not in data["vendor"]:
        return False
    
    if not isinstance(data["bill_to"], dict) or "name" not in data["bill_to"]:
        return False
    
    if not isinstance(data["line_items"], list) or len(data["line_items"]) == 0:
        return False
    
    required_item_keys = {"sku", "description", "quantity", "tax_rate", "price", "total"}
    # Required keys for each line item. It could be an argument of the funtion

    for item in data["line_items"]:
        if not all(key in item for key in required_item_keys):
            return False
    
    return True

def extract_invoice_data(input_json):
    """ 
    Extract relevant data from the JSON input.
    """
    if not is_valid_invoice_format(input_json):
        raise ValueError("Invalid invoice format")

    # Output format
    output = {
        "vendor_name": "",
        "vendor_address": "",
        "bill_to_name": "",
        "invoice_number": "",
        "date": "",
        "line_items": []
    }
    
    output["vendor_name"] = input_json["vendor"].get("name", "")
    output["vendor_address"] = input_json["vendor"].get("address", "")
    output["bill_to_name"] = input_json["bill_to"].get("name", "")
    output["invoice_number"] = input_json.get("invoice_number", "")
    
    date_str = input_json.get("date", "")
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            output["date"] = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            output["date"] = ""
    
    for item in input_json["line_items"]:
        line_item = {
            "sku": item.get("sku", ""),
            "description": item.get("description", ""),
            "quantity": item.get("quantity", ""),
            "tax_rate": item.get("tax_rate", ""),
            "price": item.get("price", ""),
            "total": item.get("total", "")
        }
        output["line_items"].append(line_item)
    
    return output

def process_invoice_file(input_file, output_folder):
    """
    Process an invoice file and save the extracted data to a JSON file.
    """
    try:
        with open(input_file, 'r') as file:
            input_json = json.load(file)
        
        output_json = extract_invoice_data(input_json)
        
        # Create output filename
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + "_processed.json"
        output_path = os.path.join(output_folder, output_filename)
        
        # Write processed data to output file
        with open(output_path, 'w') as outfile:
            json.dump(output_json, outfile, indent=2)
            
        # Logging 
        logging.info(f"Successfully processed {input_file} and saved to {output_path}")
    except json.JSONDecodeError:
        logging.error(f"Error: {input_file} is not a valid JSON file.")
    except ValueError as e:
        logging.error(f"Error processing {input_file}: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error processing {input_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Process invoice JSON files from income_data folder.")
    parser.add_argument('--input', default='income_data', help='Input folder containing JSON files (default: income_data)')
    parser.add_argument('--output', default='output_data', help='Output folder for processed JSON files (default: output_data)')
    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process all JSON files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file = os.path.join(input_folder, filename)
            logging.info(f"Processing: {input_file}")
            process_invoice_file(input_file, output_folder)

if __name__ == "__main__":
    main()