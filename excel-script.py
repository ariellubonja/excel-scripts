import pandas as pd
import re
import math

def time_to_seconds(time_str):
    minutes, seconds = time_str.split('m')
    seconds = seconds.replace('s', '')
    return int(minutes) * 60 + float(seconds)

def process_cell(cell_value):
    # Check if the cell value matches the desired pattern
    if not isinstance(cell_value, str) and math.isnan(cell_value):
        return cell_value
    if re.match(r'(real|user|sys)\s+\d+m\d+(\.\d+)?s', cell_value):
        _, time_str = cell_value.split()
        return time_to_seconds(time_str)
    else:
        return cell_value  # Return the original value if it doesn't match

def main():
    # Load the Excel file
    df = pd.read_excel('/Users/ariellubonja/My Drive (lubonjaariel@gmail.com)/PhD/EDNN/EDNN Runtimes.xlsx')

    for col in df.columns:
        df[col] = df[col].apply(process_cell)

    # Save the processed data to a new Excel file
    df.to_excel('/Users/ariellubonja/My Drive (lubonjaariel@gmail.com)/PhD/EDNN/processed_file.xlsx', index=False)

if __name__ == "__main__":
    main()
