# -*- coding: utf-8 -*-
import xlsxwriter as xw
import sys
import json


def xw_to_excel(data, file_name):  # xlsxwriter library stores data to excel
    workbook = xw.Workbook(file_name)  # Creating workbooks
    worksheet1 = workbook.add_worksheet("sheet1")  # Creating worksheet
    worksheet1.activate()  # activate table
    # Get all json keys for data[0]
    title = data[0].keys()  # Setting the table header
    worksheet1.write_row('A1', title)  # Write the table header starting from cell A1
    i = 2  # Write data from the second line
    for j in range(len(data)):
        insert_data = []
        for k in data[j].keys():
            insert_data.append(data[j][k])
        row = 'A' + str(i)
        worksheet1.write_row(row, insert_data)
        i += 1
    workbook.close()  # close table


if __name__ == '__main__':
    # Check if command line arguments are provided
    if len(sys.argv) != 2:
        print("Please input a filename")
    else:
        # Get file path
        file_path = sys.argv[1]
        # Construct the output file name by changing the extension to '.xlsx'
        output_file_path = file_path.rsplit('.', 1)[0] + '.xlsx'
        with open(file_path) as f:
            json_str = f.read().replace("\n", " ")
            payload = json.loads(json_str)['payload']
            xw_to_excel(payload['data'], output_file_path)




