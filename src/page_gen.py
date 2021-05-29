from sys import stdin
import math
import re
import queue
import sys
import subprocess
input = stdin.readline
import datetime


def template_proc(file_str):
    file_name_html = file_str+".html"
    # ファイルを読み込む
    with open(file_name_html,"r",encoding="utf-8") as file:
        filedata=file.read()

    # 置換する
    filedata=filedata.replace("**file_name**",file_str+"_main.html")
    filedata=filedata.replace("**page_name**",file_str)
    now = datetime.datetime.now()
    filedata=filedata.replace("**gen_date**",now.strftime('%Y-%m-%d %H:%M:%S'))
    # filedata=filedata.replace("target_2","replaced_2")

    # ファイルに書き込む
    with open(file_name_html,"w",encoding="utf-8") as file:
        file.write(filedata)

    return


def doc_proc(file_str):
    file_name_html = file_str+"_main.html"
    # ファイルを読み込む
    with open(file_name_html,"r",encoding="utf-8") as file:
        filedata=file.read()

    # 置換する
    filedata=filedata.replace("||dollar_symbol||","$")
    filedata=filedata.replace("||back_slash||","\\")
    # filedata=filedata.replace("**page_name**",file_str)
    # now = datetime.datetime.now()
    # filedata=filedata.replace("**gen_date**",now.strftime('%Y-%m-%d %H:%M:%S'))
    # filedata=filedata.replace("target_2","replaced_2")

    # ファイルに書き込む
    with open(file_name_html,"w",encoding="utf-8") as file:
        file.write(filedata)

def doc_pre_proc(file_str):
    file_name_md = file_str+".md"
    # ファイルを読み込む
    with open(file_name_md,"r",encoding="utf-8") as file:
        filedata=file.read()

    # 置換する
    filedata=filedata.replace("$","||dollar_symbol||")
    filedata=filedata.replace("\\","||back_slash||")
    # filedata=filedata.replace("**page_name**",file_str)
    # now = datetime.datetime.now()
    # filedata=filedata.replace("**gen_date**",now.strftime('%Y-%m-%d %H:%M:%S'))
    # filedata=filedata.replace("target_2","replaced_2")

    # ファイルに書き込む
    with open("tmp.md","w",encoding="utf-8") as file:
        file.write(filedata)

    return

def main_proc():
    file_name = sys.argv[1]
    file_str = file_name[:-3]

    print("process >> "+file_str)
    doc_pre_proc(file_str)

    subprocess.call(["pandoc", "tmp.md", "-o", file_str+"_main.html"])
    subprocess.call(["cp", "/home/mosoon/Documents/page_gen/doc_template.html" , file_str+".html"])
    
    template_proc(file_str)
    doc_proc(file_str)
    
    subprocess.call(["mv",file_str+"_main.html","output/"+file_str+"_main.html"])
    subprocess.call(["mv",file_str+".html","output/"+file_str+".html"])

    



if __name__ == '__main__':
    main_proc()