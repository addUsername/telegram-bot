# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:05:43 2020

@author: SERGI
"""


from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from json import load, dump

from scripts.Files import Files
from scripts.DB import DB

class Controller:

    def __init__(self):
            '''
            Returns
            -------
            None.
    
            '''
            config = Files.readConfig()
            self.token = config["token"]
            config["token"]
            self.mysql_connection = DB(config)
            self.run()
    
    # Define command handler.
    def report(self, update, context):
        try:
            params = context.args[0]
            num_reports = self.mysql_connection.checkNumReports(params)
            self.mysql_connection.addReports(params, num_reports)
            if(num_reports > 4):
                mssg = "@Admin ban "+str(params)+ ", he gets "+str(num_reports)+" reports."
                update.message.reply_text(mssg)
        except:
            update.message.reply_text('user not found')
            
    def getReports(self, update, context):
        try:
            num_reports = self.mysql_connection.checkNumReports(context.args[0])
            update.message.reply_text(num_reports)
        except:
            update.message.reply_text('user not found')
        
    def updateTable(self, update, context):
        params = [update.message.text]
        params.append(update.message.from_user.first_name)
        self.mysql_connection.updateTable(params)
        
    def showStats(self, update, context):
        print("showstats")
        try:
            params = context.args[0]
            print("params:" + str(params))
            mssg = self.mysql_connection.showStats(params)
            update.message.reply_text(mssg)
        except:
            print("except")
            update.message.reply_text('user not found')
        
    def run(self):
        
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("report", self.report))
        dp.add_handler(CommandHandler("numReports", self.getReports))
        dp.add_handler(CommandHandler("num", self.showStats))
        dp.add_handler(MessageHandler(Filters.text, self.updateTable))              
        
        updater.start_polling()
        updater.idle()