#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:11:47 2015

@author: Niuzexiong


"""

import xlrd
import xlwt
import re

def parseTable(xlsTable):
    blocks = xlsTable.merged_cells
    valueMap = {}
    for (rlow,rhigh,clow,chigh) in blocks:
        for i in range(rlow,rhigh):
            for j in range(clow,chigh):
                valueMap[str(i)+'_'+str(j)] = str(rlow)+'_'+str(clow)
    array =[]
    nrow = xlsTable.nrows
    ncol = xlsTable.ncols
    for i in range(nrow):
        rowValues = []
        for j in range(ncol):
            if str(i)+'_'+str(j) in valueMap:
                x,y = map(lambda x:int(x),valueMap[str(i)+'_'+str(j)].split('_'))
                value = xlsTable.cell_value(x,y)
                print type(value)
                if  type(value) != float:
                    value = value.replace('&','&amp;')
                else:
                    pass
                rowValues.append(value)
            else:
                value = xlsTable.cell_value(i,j)
                if type(value) != float:
                    value = value.replace('&','&amp;')
                else:
                    pass
                rowValues.append(value)
        array.append(rowValues)
    return array

def parse_excel(aExcel):
    allData = {}

    data = xlrd.open_workbook(aExcel,encoding_override="cp1251")
    sheetNames = data.sheet_names()
    for item in sheetNames:

        table = data.sheet_by_name(item)
        allData[item] = table
    return allData,sheetNames

def re_replace(q,stra,strb,astr):
    m = q.findall(astr)
    if m:
        for x in m:
            astr = astr.replace(x,x.replace(stra,strb))
    return astr

def wt_asheet(atable,asheet):
    style1 = xlwt.easyxf('font: name Times New Roman, color-index black')
    i,j = 0,0
    for aline in atable:
        for acell in aline:
            asheet.write(i,j,acell,style1)
            j += 1
        i += 1

if __name__ == "__main__":
    input = "D:\\work\\report\\classed-2015-12-10-xff.xls"
    output = "D:\\work\\report\\classed-2015-12-10-xff.ch.xls"

    wb = xlwt.Workbook()

    allData,sheetNames = parse_excel(input)

    style1 = xlwt.easyxf('font: name Times New Roman, color-index black')
    for k in sheetNames:
        ws = wb.add_sheet(k)
        atable = allData[k]
        nrow = atable.nrows
        ncol = atable.ncols
        for i in range(nrow):
            for j in range(ncol):
                value = atable.cell_value(i,j)
                
                value = re_replace(re.compile(r'\(\d{6}'),'(','[',value)
                value = re_replace(re.compile(r'\(A\d{6}'),'(','[',value)
                value = re_replace(re.compile(r'\(B\d{6}'),'(','[',value)
                value = re_replace(re.compile(r'\(C\d{6}'),'(','[',value)
                value = re_replace(re.compile(r'\d{6}\)'),')',']',value)
                ws.write(i,j,value,style1)


