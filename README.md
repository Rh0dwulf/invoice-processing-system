# Invoice Processing System

This system fetches invoice data from an API and processes it to extract structured information. It consists of two main components: an API fetcher and an invoice processor.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Troubleshooting](#troubleshooting)
7. [Approach](#aproach)
8. [Assumptions](#assumptions)
9. [Coding Best Practices](#coding-best-practices)
10. [Future Improvements](#future-improvements)

## Requirements

- Python 3.9 or higher
- Conda (for environment management)
- Access to the invoice processing API (credentials required)

## Installation

1. Clone this repository:

```
git clone https://github.com/Rh0dwulf/invoice-processing-system.git
cd invoice-processing-system
```

### Option 1: Automatic Setup (requires Conda)

1. Ensure Conda is installed and initialized in your system.
2. Run the setup script:
```bash
bash env_setup.sh
```
3. Activate the environment:
```bash
conda activate invoice_processor
```
### Option 2: Manual Setup

If you don't have Conda or prefer manual setup:

1. Ensure you have Python 3.9 or higher installed.

2. Create a virtual environment:
```bash
python -m venv invoice_env
```

3. Activate the virtual environment:
- On Windows:
  ```
  invoice_env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source invoice_env/bin/activate
  ```

4. Install the required packages:
```
pip install -r requirements.txt
```
5. Set up environment variables:
- Create a file named `.env` in the project root directory.
- Add the following lines to the `.env` file:
  ```
  CLIENT_ID_ENV=your_client_id
  CLIENT_SECRET_ENV=your_client_secret
  USERNAME_ENV=your_username
  API_KEY_ENV=your_api_key
  ```
- Replace `your_client_id`, `your_client_secret`, `your_username`, and `your_api_key` with your actual API credentials.

## Configuration

After installation, whether automatic or manual:

1. Open the `.env` file in the project root directory.
2. Replace the placeholder values with your actual API credentials.
3. Save and close the `.env` file.

## Usage

1. Place the documents you want to process in the `Documents` folder.

2. Run the API fetcher to retrieve invoice data:

```
python api_response.py
```
This will process all documents in the `Documents` folder and save the API responses in the `income_data` folder.

3. Run the invoice processor to extract structured data:

```
python invoice_processor.py
```

This will process the API responses in the `income_data` folder and save the extracted data in the `output_data` folder.

### Optional Arguments

Both scripts accept optional arguments to specify custom input and output directories:

- `api_response.py`:
```
python api_response.py --input custom_input_folder --output custom_output_folder
```

- `invoice_processor.py`:
```
python invoice_processor.py --input custom_input_folder --output custom_output_folder
```

## Project Structure

invoice-processing-system/
│
├── api_fetcher.py
├── invoice_processor.py
├── requirements.txt
├── conda_env_setup.sh
├── .env
├── README.md
├── approach_and_practices.md
│
├── Documents/
│   └── (place input documents here)
│
├── income_data/
│   └── (API responses will be saved here)
│
└── output_data/
└── (processed invoice data will be saved here)

## Troubleshooting

- If you encounter any "Module not found" errors, ensure you have activated the Conda environment:

```
conda activate invoice_processor
```

- If you get API authentication errors, double-check your credentials in the `.env` file.

- For any other issues, please check the console output for error messages and refer to the error handling sections in the respective Python scripts.

## Approach

Our invoice processing system consists of two main components:

1. **API Fetcher (`api_fetcher.py`)**: This script interacts with an external API to fetch invoice data based on input documents.
2. **Invoice Processor (`invoice_processor.py`)**: This script processes the fetched invoice data and extracts relevant information.

The system follows a two-step process:
1. Fetch data from the API for each document in the 'Documents' folder.
2. Process the fetched data and extract structured information from each invoice.

## Assumptions

1. The API requires authentication using client ID, client secret, username, and API key.
2. Input documents are stored in a 'Documents' folder.
3. The API responses should be saved in an 'income_data' folder.
4. Processed invoice data should be saved in an 'output_data' folder.
5. The API client is implemented in a separate `API` module.
6. The system is run on a machine with Conda installed.

## Coding Best Practices

1. **Modular Design**: The system is split into two separate scripts, each with a single responsibility, following the Single Responsibility Principle.

2. **Environment Variables**: Sensitive information like API credentials are stored as environment variables, not hardcoded in the scripts.

3. **Error Handling**: Both scripts implement try-except blocks to handle potential errors gracefully.

4. **Logging**: The scripts use Python's logging module to provide informative output during execution.

5. **Code Organization**: Functions are used to organize code into logical units, improving readability and maintainability.

6. **Type Hinting**: While not implemented in the current version, future iterations could benefit from type hinting for improved code clarity.

7. **Configurability**: The scripts allow for custom input and output directories, making the system more flexible.

8. **Documentation**: Each script and function includes docstrings explaining their purpose and usage.

9. **Consistent Naming**: Variables and functions are named clearly and consistently, following Python's snake_case convention.

10. **Dependency Management**: A `requirements.txt` file is provided to easily install necessary dependencies.

11. **Environment Isolation**: A Conda environment is used to isolate the project's dependencies from the system-wide Python installation.

12. **Version Control**: While not explicitly mentioned, it's assumed that the project uses a version control system like Git.

## Future Improvements

1. Implement unit tests to ensure code reliability.
2. Add more robust input validation and error handling.
3. Implement parallel processing for handling large numbers of documents more efficiently.
4. Create a configuration file for easily adjustable settings.
5. Implement a user interface for easier interaction with the system.