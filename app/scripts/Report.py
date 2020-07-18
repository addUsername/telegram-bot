# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:06:40 2020

@author: SERGI
"""
from scripts.Files import Files
class Report:

    def __init__(self):
        '''

        Returns
        -------
        None.

        '''
        pass

    def report(update, context):
        """
        Report system, This method should be called when command "/reportar userName" is written.
        Data are stored in /app/resources/users_strikes.json as dict.

        str context.args[0] The userName
        int max When an user generate more than [max] reports, [Admin] is mentioned
        str admin User with ban privileges
        """
        max = 4
        admin = "@Admin"

        try:
            users_strikes = Files.readJson("users_strikes.json")
            if(context.args[0] not in users_strikes.keys()):
                users_strikes[context.args[0]] = 1
                update.message.reply_text('ok')
            else:
                users_strikes[context.args[0]] += 1
                if (users_strikes[context.args[0]] > max ):
                    update.message.reply_text(admin+" ban " + context.args[0] +" pls")
            users_strikes = Files.writeJson("users_strikes.json", users_strikes)
        except:
            update.message.reply_text('user not found')

