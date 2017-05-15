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
    '''
    This function return github following page url
    :param Name: Username
    :param page_number: page nubmer of following page
    :type Name:str
    :type Page:int
    :return: github following url as string
    '''
    return "https://github.com/"+Name+"?page="+str(page_number)+"&tab=following"
def url_maker_follower(Name,page_number):
    '''
    This function return github follower page url
    :param Name: username
    :param page_number: page number of follower page
    :type Name:str
    :type page_number:int
    :return: github follower url as string
    '''
    return "https://github.com/" + Name + "?page=" + str(page_number) + "&tab=followers"

def user_list_gen(input_string,follower_name):
    '''
    This function extract usernames from raw_html
    :param input_string: raw input html
    :param follower_name: follower_name
    :type input_string:str
    :type follower_name:str
    :return: user_list as list
    '''
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
    '''
    This function extract raw_html file
    :param url: url
    :type url:str
    :return: html data
    '''
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
    '''
    This function check end page
    :param input_string: raw html
    :type input_string:str
    :return: True or False
    '''
    if input_string.find("reached the end")!=-1:
        return True
    else:
        return False
def follower_list_gen(follower_name):
    '''
    This function generate follower_list
    :param follower_name: username
    :type follower_name:str
    :return: username follower list
    '''
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
    '''
    This function generate following list
    :param follower_name: username
    :type follower_name:str
    :return: username following list
    '''
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

def create_random_sleep(index=1,min_time=1,max_time=3):
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


def follow(username):
    '''
    This function create following and follower list
    :param username: username
    :type username:str
    :return: (list_1,list_2) as tuple
    '''
    print("Collecting Follower Information ...")
    print_line(70, "*")
    list_1 = follower_list_gen(username)
    file = open(username + "_follower.log", "w")
    print(str(len(list_1)) + " Followers --> " + username + "_follower.log")
    print_line(70, "*")
    file.write("\n".join(list_1))
    file.close()
    print('Collecting Following Informnation ...')
    print_line(70, "*")
    list_2 = following_list_gen(username)
    file = open(username + "_following.log", "w")
    print(str(len(list_2)) + " Following --> " + username + "_following.log")
    print_line(70, "*")
    file.write("\n".join(list_2))
    file.close()
    return (list_1,list_2)

def dif(list_1,list_2):
    '''
    This function generate dif files
    :param list_1:follower list
    :param list_2: following list
    :type list_1:list
    :type list_2:list
    :return: None
    '''
    file = open(username + "_dif1.log", "w")
    dif_list = list(set(list_2) - set(list_1))
    print(str(len(dif_list)) + " Following - Not Follower --> " + username + "_dif1.log")
    print_line(70, "*")
    file.write("\n".join(dif_list))
    file.close()
    file = open(username + "_dif2.log", "w")
    dif_list = list(set(list_1) - set(list_2))
    print(str(len(dif_list)) + " Follower - Not Following --> " + username + "_dif2.log")
    print_line(70, "*")
    file.write("\n".join(dif_list))
    file.close()
if __name__=="__main__":
    time_1=time.perf_counter()
    username=input("Please Enter Your Github Username : ")
    (list_1,list_2)=follow(username)
    dif(list_1,list_2)
    time_2=time.perf_counter()
    print("Data Generated In "+str(time_2-time_1)+" sec")
    print("Log Files Are Ready --> " + os.getcwd())
    gc.collect()












