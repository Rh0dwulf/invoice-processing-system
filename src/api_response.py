import os
import json
import logging
from veryfi import Client
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Get API credentials from environment variables
client_id = os.getenv('CLIENT_ID_ENV')
client_secret = os.getenv('CLIENT_SECRET_ENV')
username = os.getenv('USERNAME_ENV')
api_key = os.getenv('API_KEY_ENV')

# Categories for document processing
categories = ['Logistic', 'Internet', 'Services', 'Telecom', 'Transport']

def process_documents(input_directory, output_directory):
    """Process documents from input directory and save API responses to output directory"""
    
    # Initialize API client
    client = Client(client_id, client_secret, username, api_key)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Process each file in the input directory
    for file in os.listdir(input_directory):
        input_file = os.path.join(input_directory, file)
        if os.path.isfile(input_file):
            base = os.path.basename(input_file)
            name = os.path.splitext(base)[0]
            logging.info(f"Processing: {name}")
            
            try:
                # Process document using API client
                response = client.process_document(input_file, categories=categories)
                logging.info(f"Received response for: {name}")
                
                # Save API response to output directory
                output_file = os.path.join(output_directory, f'data_{name}.json')
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(response, f, ensure_ascii=False, indent=4, default=str)
                
                logging.info(f"Saved response to: {output_file}")
            
            except Exception as e:
                logging.error(f"Error processing {name}: {str(e)}")

def main():
    input_directory = 'Documents'
    output_directory = 'income_data'
    
    logging.info("Starting document processing...")
    process_documents(input_directory, output_directory)
    logging.info("Document processing completed.")

if __name__ == "__main__":
    main()