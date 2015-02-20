# -*- coding: utf-8 -*-


class employee:

    def __init__(self,id,name,bd,salary):
        self.id = id
        self.name = name
        self.bd = bd
        self.salary = salary

#
"""
class name:

    def __init__(self,id,name):
        self.id = id
        self.name = name

class bd:

    def __init__(self,id,bd):
        self.id = id
        self.bd = bd

class salary:

    def __init__(self,id,salary):
        self.id = id
        self.salary = salary
"""

def register(employeeid):

    print "名前を入力してください"
    tempname = raw_input()
    print "生年月日を入力してください"
    tempbd = raw_input()
    print "月額の給与を入力してください"
    tempsalary = raw_input()
    EmployeeList.append(employee(employeeid,tempname,tempbd,tempsalary))

    employeeidtemp = employeeid + 1

    return(employeeidtemp)

def intro():

    print "*****************************"
    print "ID   名前       生年月日     給与"
    print "*****************************"
    for i in EmployeeList:
#        strid = str(i.id)
        string = str(i.id) + "   " + i.name + "    " + i.bd + "      " + i.salary
        print string
    print "*****************************"


def delete():

    print "削除する社員のIDを入力してください"
    deleteid = input() - 1

    deletedlist = EmployeeList.pop(deleteid)
    print "%sを削除しました" % deletedlist.name


def edit():

    print "更新したい社員のIDを入力してください"
    editid = input()
    index = editid - 1

    print "新しい情報を入力してください"
    print "名前を入力してください"
    tempname = raw_input()
    print "生年月日を入力してください"
    tempbd = raw_input()
    print "月額の給与を入力してください"
    tempsalary = raw_input()

    EmployeeList.pop(index)
    EmployeeList.insert(index,employee(editid,tempname,tempbd,tempsalary))



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
            delete()
        elif select == "4":
            edit()
        else:
            print "無効なコマンドです。"
