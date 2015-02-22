# -*- coding: utf-8 -*-

import re

class employee:

    def __init__(self,id,name,bd,salary):
        self.id = id
        self.name = name
        self.bd = bd
        self.salary = salary


class p_bd:

    def __init__(self,year,month,date):
        self.year = year
        self.month = month
        self.date = date


def register(employeeid):

    print "名前を入力してください"
    tempname = raw_input()
    print "生年月日を入力してください(yyyy/mm/ddの形で)"
    while(1):
        tempbd = raw_input()
        bdlist = tempbd.split("/")
        if len(bdlist) != 3:
            print "不正な値です．再度入力してください"
        elif int(bdlist[0]) > 2015:
            print "不正な値です．再度入力してください"
        elif int(bdlist[1]) > 12 or int(bdlist[1]) < 1:
            print "不正な値です．再度入力してください"
        elif int(bdlist[2]) > 31 or int(bdlist[2]) < 1:
            print "不正な値です．再度入力してください"
        else:
            break
    bdclass = p_bd(bdlist[0],bdlist[1],bdlist[2])

    print "月額の給与を入力してください(8桁まで)"
    while(1):
        tempsalary = raw_input()
        if tempsalary.isdigit():
            tempintsalary = int(tempsalary)
            if tempintsalary <= 99999999:
                break
            else:
                print "桁数が多すぎます．再度入力してください"
        else:
            print "数値ではありません．再度入力してください"

    EmployeeList.append(employee(employeeid,tempname,bdclass,tempintsalary))

    employeeidtemp = employeeid + 1

    return(employeeidtemp)


def intro():

    print "*****************************"
    print "ID   名前       生年月日     給与"
    print "*****************************"
    for i in EmployeeList:
        string = str(i.id) + "   " + i.name + "    " + i.bd.year + "年" + i.bd.month +"月" + i.bd.date + "日" + "      " + '{:,d}'.format(i.salary) + "円"
        print string
    print "*****************************"



def delete(requiredid):

    j = 0
    if requiredid == 0:
        print "削除する社員のIDを入力してください"
        deleteid = input()

    else:
        deleteid = requiredid

    for deletenum in EmployeeList:
        if deletenum.id == deleteid:
            deletedList = EmployeeList.pop(j)
            if requiredid == 0:
                print "%sを削除しました" % deletedList.name
            break
        j = j + 1


def edit():

    print "更新したい社員のIDを入力してください"
    editid = input()

    delete(editid)
    register(editid)




if __name__ == "__main__":

    employeeid = 1
    EmployeeList = []

    while(1):
        print "<MENU>\n"
        print "========================"
        print "1. 登録"
        print "2. 紹介"
        print "3. 削除"
        print "4. 更新"
        print "========================"

        select = raw_input()

        if select == "1":
            employeeid = register(employeeid)
        elif select == "2":
            intro()
        elif select == "3":
            delete(0)
        elif select == "4":
            edit()
        else:
            print "無効なコマンドです。"
