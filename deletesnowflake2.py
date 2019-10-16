#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import snowflake.connector
import os
import pprint

# from codecs import open
# import sys
# import subprocess
# databasename=${1}


# def openfiles(filename,filetype):
#     f = open(filename,filetype)
#     return f
#     f.close()
#
#
# f = openfiles('33.txt','r')
# with open('33.txt','r') as f:
#     for databasename in f.readlines():
#         if databasename.strip('\n'):
#             pass
#             # print(databasename)
list1 = []
with open('nouse.txt', 'r') as f:
    while True:
        str1 = f.readline()
        str2 = str1.strip("\n").strip("\t")
        if str2:
            list1.append('drop database "' + str2 + 'Data"' + '\n')
            list1.append('drop database "' + str2 + 'Reports"' + '\n')
        if not str1:
            break

# args=sys.argv
with open("nouse.txt", "w") as f1:
    for i in list1:
        f1.write(i)
pprint.pprint(list1)


# databasename=args[1]+"Data"
# databasename1=args[1]+"Reports"


class Shell():

    # Note: CMD command like opening a process does not quit. Do not use this method to execute.
    # For error example, CMD = python.

    @staticmethod
    def run(cmd, cwd=None):
        # shell set is true，the cmd will be executed through shell
        # stdin, stdout, stderr, it represents the standard input, output and error handle of the program respectively.
        # They can be PIPE, file descriptor or file object, or can be set to None, which is inherited from the parent process.
        # subprocess.PIPE, Provide a caching area for text streams
        child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        output, errors = child.communicate()
        code = child.returncode
        # out = output.decode("gbk" if IsZeorOrNull(output) else chardet.detect(output).get('encoding', 'gbk')).encode("utf-8")
        # err = errors.decode("gbk" if IsZeorOrNull(errors) else chardet.detect(errors).get('encoding', 'gbk')).encode("utf-8")
        # if not IsZeorOrNull(err) or int(code) != 0:
        #    raise My_ShellError('Shell Run Error: %s'% out if IsZeorOrNull(err) else err)
        return output, errors

# ExcutiSql2Changeng select on Snowflake
# def Sql2Change(sql):
#     try:
#         ctx = snowflake.connector.connect(user='READWRITE',password='Mzthx664@',account='encompass_dev')
#         cs = ctx.cursor()
#         a = cs.execute(sql)
#         ctx.commit()
#         cs.close()
#         ctx.close()
#         return a
#     except Exception,ex:
#         print "Error %s" %ex
#
#
# try:
#     SQL="USE WAREHOUSE DWTest;"
#     Sql2Change(sql=SQL)
#     print 'USE DWTest successfully!'
#     SQL="Drop database %s" % (databasename)
#     Sql2Change(sql=SQL)
#     print 'delete %s successfully!' % (databasename)
#     SQL="Drop database %s" % (databasename1)
#     Sql2Change(sql=SQL)
#     print 'delete %s successfully!' % (databasename1)
#
# except:
#     raise
