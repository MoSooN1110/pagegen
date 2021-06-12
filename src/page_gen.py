 # -- coding: utf-8 --
from sys import stdin
import math
import re
# import queue
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
    file_name_html = file_str+"_data.html"
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


def data_mege(file_str):
    file_name_html2 = file_str+"_data.html"
    file_name_html1 = file_str+".html"
    # ファイルを読み込む
    
    with open(file_name_html1,"r",encoding="utf-8") as file1:
        filedata1=file1.read()
        filedata = ''
        with open(file_name_html2,"r",encoding="utf-8") as file2:
            filedata2=file2.read()
            idx = filedata1.find("<!-- #ID0001:article -->")
            filedata += filedata1[:idx]
            filedata += filedata2
            filedata += filedata1[idx:]
            # with open(file_name_html1,"w",encoding="utf-8") as file:
            #     file.write(filedata1[:idx])
            # with open(file_name_html1,"a",encoding="utf-8") as file:
            #     file.write(filedata2)
            # with open(file_name_html1,"a",encoding="utf-8") as file:
            #     file.write(filedata1[idx:])
            
    # ファイルに書き込む
    # print(filedata)
    with open(file_name_html1,"w",encoding="utf-8") as file:
        file.write(filedata)

    return
def main_proc():
    file_name = sys.argv[1]
    file_str = file_name[:-3]
    if len(sys.argv) == 1:
        print("uasge >> python page_gen.py input.md template.html")
        return

    print("process >> "+file_str)
    doc_pre_proc(file_str)
    template_file_path = sys.argv[2]
    subprocess.call(["pandoc", "tmp.md", "-o", file_str+"_data.html"])
    subprocess.call(["cp", template_file_path , file_str+".html"])
    
    template_proc(file_str)
    doc_proc(file_str)
    data_mege(file_str)
    
    subprocess.call(["rm",file_str+"_data.html"])
    # subprocess.call(["mv",file_str+".html","output/"+file_str+".html"])
    subprocess.call(["rm","tmp.md"])
    print("successfuly generated >"+file_str+".html" )

    



if __name__ == '__main__':
    main_proc()
