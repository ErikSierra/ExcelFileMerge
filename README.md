# Project Title

Combine Downloads CSV Files

## Description

This script combines two CSV files, "file1.csv" and "file2.csv", both located in the Downloads directory, into one Pandas data frame. It then adds a "Date" column with yesterday's date and a "Type" column indicating whether the row came from "file1" or "file2". The final data frame is saved as an Excel file called "combined_data.xlsx". 

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library

### Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the Pandas library by running the following command in your terminal: 
```bash
pip install pandas
```

### Usage

1. Put your two CSV files, "file1.csv" and "file2.csv", in the Downloads folder.
2. Open the terminal and navigate to the folder where the "combine_csv.py" script is located.
3. Run the script by typing `python combine_csv.py`.
4. The combined data frame will be printed in the terminal, and an Excel file called "combined_data.xlsx" will be saved in the same folder.
