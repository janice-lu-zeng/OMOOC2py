#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime
from bottle import route, request, post, run, template

book_name = "myDiary.txt"
diary_existence = exists(book_name)

def getTime():
    current_date_time = str(datetime.now())
    current_date_time = current_date_time[:(len(current_date_time)-7)]
    return current_date_time

def readDiary():
    if diary_existence:
        txt = open("myDiary.txt")
        existingDiaries = txt.readlines()
        txt.close()
    else:
        existingDiaries = ""
    return existingDiaries
    
def writeDiary(receivedDiary): 
    diary = getTime() + "\n" + receivedDiary +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diary)
    txt2.close()

# template. will be moved to a separate file later
d_tpl = '''
           <html>
           Welcome!<br><br>
           <form action="/diary" method="post">
            Input your online diary here: <input name="newdiary" type="text" />
            <input value="Submit" name="do_submit" type="submit">
            </form>
            <p>Hi there, here's your current diary collection:</p>
            <ul>
            % for line in d:
            {{line}}<br>
            % end
            </ul>
           </html>'''


@route('/diary')
def diary():
    data = readDiary()
    return template(d_tpl, d = data)
    
@route('/diary', method = 'POST')
def newDiary():
    #getValue = request.POST.decode('utf-8')
    nd = request.POST.get('newdiary')
#    nd = request.forms.get('newDiary')
    if nd:
        writeDiary(nd)
    return template(d_tpl, d = readDiary())


run(host = 'localhost', port = 8080, debug = True)
