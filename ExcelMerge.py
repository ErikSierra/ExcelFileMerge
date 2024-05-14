import pandas as pd
import os
import datetime

def combine_downloads():
    # combines CSV files in Downloads directory into one data frame and adds "Date" and "Type" columns
    downloads_folder = os.path.expanduser("~") + "\\Downloads\\"
    file1 = 'file1.csv'
    file2 = 'file2.csv'
    df1 = pd.read_csv(os.path.join(downloads_folder, file1))
    df2 = pd.read_csv(os.path.join(downloads_folder, file2))
    df_comb = pd.concat([df1, df2], ignore_index=True)
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    date_string = yesterday.strftime('%m/%d/%y 00:00')
    df_comb['Date'] = date_string
    df_comb.insert(len(df_comb.columns), "Type", ['Type1']*len(df1) + ['Type2']*len(df2))
    print("Combined CSV files into DataFrame")
    return df_comb

def save_data_frame(df, filename):
    # saves data frame to an Excel file
    df.to_excel(filename, index=False)
    print(f"Data saved to file: {filename}")


if __name__ == '__main__':
    df_final = combine_downloads()
    save_data_frame(df_final, 'combined_data.xlsx')
