import requests
import sys
import socket
import os
import datetime
from functools import reduce
import time
from random import randint
DEBUG=False
import gc
def url_maker_following(Name,page_number):
    return "https://github.com/"+Name+"?page="+str(page_number)+"&tab=following"
def url_maker_follower(Name,page_number):
    return "https://github.com/" + Name + "?page=" + str(page_number) + "&tab=followers"

def user_list_gen(input_string,follower_name):
    user_list=[]
    index=0
    while(index!=-1):
        index=input_string.find('alt="@',index+6,len(input_string))
        length=input_string[index+6:].find('"')
        user_name=input_string[index+6:index+6+length]
        if user_name!=follower_name:
            if user_name!=follower_name:
                user_list.append(user_name)
    return user_list[:-1]


def get_html(url):
    time.sleep(create_random_sleep())
    if internet()==True:
        new_session=requests.session()
        new_session.cookies.clear()
        raw_html=new_session.get(url)
        new_session.close()
        raw_data=raw_html.text
        if "Not Found" in raw_data:
            print("Invalid Github User")
            sys.exit()
        return raw_data
    else:
        print("Error In Internet")
        sys.exit()


def end_check(input_string):
    if input_string.find("reached the end")!=-1:
        return True
    else:
        return False
def follower_list_gen(follower_name):
    follower_list = []
    page_number=0
    while (True):
        page_number += 1
        follower_url = url_maker_follower(follower_name, page_number)
        follower_html = get_html(follower_url)
        if end_check(follower_html) == True:
            break
        temp_list = user_list_gen(follower_html,follower_name)
        follower_list.extend(temp_list)
    return follower_list
def following_list_gen(follower_name):
    following_list = []
    page_number=0
    while (True):
        page_number+=1
        following_url = url_maker_following(follower_name, page_number)
        following_html = get_html(following_url)
        if end_check(following_html) == True:
            break
        temp_list = user_list_gen(following_html,follower_name)
        following_list.extend(temp_list)
    return following_list

def error_log(msg):
    """
    Create the errorlog of the app
    :param msg: error message
    :type msg:str
    """
    if "log" not in os.listdir():
        os.mkdir("log")
    file = open(reduce(os.path.join, [os.getcwd(), "log", "error_log.txt"]), "a")
    file.write(str(datetime.datetime.now()) + " --> " + str(msg) + "\n")
    file.close()

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Check Internet Connections.
    :param  host: the host that check connection to
    :param  port: port that check connection with
    :param  timeout: times that check the connnection
    :type host:str
    :type port:int
    :type timeout:int
    :return bool: True if Connection is Stable
    >>> internet() # if there is stable internet connection
    True
    >>> internet() # if there is no stable internet connection
    False
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        error_log(str(ex))
        return False

def create_random_sleep(index=1,min_time=1,max_time=7):
    '''
    This function generate sleep time with random processes
    :param index: index to determine first page  and messages(index = 0 is for first page)
    :param min_time: minimum time of sleep
    :param max_time: maximum time of sleep
    :type index:int
    :type min_time:int
    :type max_time:int
    :return: time of sleep as integer (a number between max and min)
    '''
    if index==0:
        time_sleep = 5
        if DEBUG==True:
            print("Wait "+str(time_sleep)+" sec for first search . . .")
    else:
        time_sleep = randint(min_time, max_time)
        if DEBUG==True:
            print("Wait "+str(time_sleep)+" sec for next search . . .")
    if DEBUG==True:
        print_line(70,"*")
    return time_sleep

def print_line(number=30,char="-"):
    '''
    This function print line in screen
    :param number: number of items in each line
    :param char: each char of line
    :return: None
    '''
    line=""
    for i in range(number):
        line=line+char
    print(line)
if __name__=="__main__":
    follower_name="sepandhaghighi"
    print("Collecting Follower Information ...")
    list_1=follower_list_gen(follower_name)
    file = open(follower_name + "_follower.log", "w")
    file.write("\n".join(list_1))
    file.close()
    print('Collecting Following Informnation ...')
    list_2=following_list_gen(follower_name)
    file = open(follower_name + "_following.log", "w")
    file.write("\n".join(list_2))
    file.close()
    following_not_follower=[]
    file=open(follower_name+"_dif.log","w")
    for i in list_2:
        if i not in list_1:
            following_not_follower.append(i)
            file.write(i+"\n")
    file.close()
    gc.collect()












