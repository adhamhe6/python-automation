## News Data Extraction Automation

This script automates the extraction of data from a news website (The Sun) and saves it to CSV files arranged by date. The script utilizes Selenium WebDriver to navigate the website and retrieve the desired data. It can be converted into an executable file for easy execution.

### Prerequisites

- Python 3.x
- Selenium WebDriver
- pandas library
- webdriver_manager library

### Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:

   ```shell
   pip install selenium webdriver_manager pandas
   ```

### Usage

1. Open the `news-automation.py` file in a text editor.
2. Run the script using the following command:

   ```shell
   python news-automation.py
   ```
This will execute the script and save the extracted data to a CSV file named football_headlines_MM-DD-YYYY.csv, where MM-DD-YYYY represents the current date.

### Converting to Executable

To convert the script into an executable file for easy distribution and execution, you can use tools like PyInstaller or cx_Freeze. Here's an example using PyInstaller:

1. Install PyInstaller by running the following command:
   ```shell
   pip install pyinstaller
   ```
2. Navigate to the project directory in the command line.

3. Run the following command to convert the script into an executable:
   ```shell
   pyinstaller --onefile news-automation.py
   ```
4. After the conversion is complete, you will find the executable file in the dist directory.

### Notes

* The script uses headless mode, which means the Chrome browser will run in the background without a visible window. If you want to see the browser window during execution, you can remove the options.headless = True line.

* This script serves as a basic example and may require modifications to work with different websites or handle specific scenarios.