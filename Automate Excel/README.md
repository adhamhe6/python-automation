## Excel Automation

This script automates the creation of a sales report in Excel. It reads a pivot table from an Excel file, adds a bar chart, applies formulas, and formats cells. The script allows you to enter the name of the month and generates the output report with the chart and formatted data. The output is saved as an Excel file in the `xlsx` folder.

### Prerequisites

- Python 3.x
- openpyxl library

### Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
    ```shell
    pip install openpyxl
    ```

### Usage

1. Place the `pivot_table.xlsx` file in the `xlsx` folder.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using the following command:

    ```shell
    python 6.py-to-exe.py
    ```
4. Enter the name of the month when prompted.
5. The script will generate the sales report with the bar chart, formulas, and formatted cells.
6. The output file report_<month>.xlsx will be saved in the xlsx folder.

### Customization

* You can modify the input file by replacing pivot_table.xlsx with your own file. Ensure that the file is located in the xlsx folder.
* Feel free to customize the chart title, font styles, and other formatting options in the script according to your requirements.

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

* Ensure that the xlsx folder exists in the same directory as the script, and the input file pivot_table.xlsx is placed inside it.
* This script serves as a basic example and may require modifications to work with different Excel files or handle specific scenarios.