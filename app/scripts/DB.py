# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:44:40 2020

@author: SERGI
"""
import pymysql
import time
class DB:

    def __init__(self, params):
        '''
        Returns
        -------
        None.

        '''
        print("Connecting to mysql..")
        time.sleep(1)
        self.mydb = pymysql.connect(host=params["host"],
                                            user=params["user"],
                                            password=params["pass"],
                                            database=params["database"])
        print("connected")
    def addReports(self, params, num_reports):
        cursor = self.mydb.cursor()
        if(num_reports == 0):
            cursor.execute("insert into report (nombre,value) values ('"+
                       str(params)+"',"+str(1)+")")
        else:
            cursor.execute("update report set value = "+str(num_reports+1)+" where nombre = '"+params+"';")
        self.mydb.commit()
    
    def updateTable(self, params):
        cursor = self.mydb.cursor()
        cursor.execute("insert into mssg (nombre,fecha,post) values ('"+
                       str(params[1])+"', current_timestamp, '"+str(params[0])+"');")
        self.mydb.commit()
        
    def checkNumReports(self, params):
        cursor = self.mydb.cursor()
        cursor.execute("select value from report where nombre='"+str(params)+"';")
        data = cursor.fetchone()
        if(data == None):
            return 0
        else:
            return data[0]
        
    def showStats(self, params):
        cursor = self.mydb.cursor()
        cursor.execute("select count(post) from mssg where nombre='"+str(params)+"';")
        data = cursor.fetchone()
        return "params: "+str(data[0])+" mens."
