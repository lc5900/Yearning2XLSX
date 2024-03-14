# -*- coding: utf-8 -*-
import xlsxwriter as xw
import sys
import json


def xw_to_excel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    # 获取data[0]的所有json key
    title = data[0].keys()  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = []
        for k in data[j].keys():
            insertData.append(data[j][k])
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


if __name__ == '__main__':
    # 检查是否提供了命令行参数
    if len(sys.argv) != 2:
        print("请拖入一个文件到脚本中")
    else:
        # 获取文件路径
        file_path = sys.argv[1]
        # Construct the output file name by changing the extension to '.xlsx'
        output_file_path = file_path.rsplit('.', 1)[0] + '.xlsx'
        with open(file_path) as f:
            json_str = f.read().replace("\n", " ")
            payload = json.loads(json_str)['payload']
            xw_to_excel(payload['data'], output_file_path)




