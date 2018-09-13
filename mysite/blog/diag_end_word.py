#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import xlrd

def serce(word):
    data = xlrd.open_workbook("./blog/表.xlsx") #打开excel
    table = data.sheet_by_name("111")#读sheet
    nrows = table.nrows #获得行数
    lrow = [2,3,4,5,7,8,9,10,11,29,30,31,32]

    result = [[table.row_values(i)[j] for j in lrow] for i in range(1,nrows)]

    diag_weici = [s for s in result if (s[2] == '' or s[2] == '核')]

    diag_ciwei = [s[1] for s in diag_weici]


    print(1)
    ####################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


    data = xlrd.open_workbook("./blog/表.xlsx") #打开excel
    table = data.sheet_by_name("111")#读sheet
    nrows = table.nrows #获得行数
    lrow = [2,3,4,5,7,8,9]

    result = [[table.row_values(i)[j] for j in lrow] for i in range(1,nrows)]

    icd_ciwei = [s[1] for s in result]


    print(1)
    #############################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###########################

    # 导入ICD词

    data = xlrd.open_workbook("./blog/3.xlsx") #打开excel
    table = data.sheet_by_name("output3")#读sheet
    nrows = table.nrows #获得行数
    lrow = [0,1,2,3,4,5,6,7]

    result = [[table.row_values(i)[j] for j in lrow] for i in range(1,nrows)]

    icd_word = [s[0] for s in result if s[3] != '禁用']

    flag = ["0"]*3
    if word in diag_ciwei:
        flag[0] = '词'
    if word in icd_ciwei:
        flag[1] = '词'
    if word in icd_word:
        flag[2] = '词'

    return flag


是是是 = serce('病')


print(1)