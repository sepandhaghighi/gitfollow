# -*- coding: utf-8 -*-
import requests
import sys
import socket
import os
import datetime
from functools import reduce
import time
from random import randint
import sys
from art import tprint
DEBUG=False
import gc

def help_func():
    tprint("help")
    print("By Sepand Haghighi\n")
    print("python -m gitfollow")
    print("- run  (run gitfollow)\n")
    print("- test (run tests)\n")
    print("- help (help page)\n")
def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string

def time_convert(input_string):
    '''
    This function convert input_string from uptime from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=float(input_string)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"

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

def url_maker_repo(Name,page_number):
    '''
    This function return github repo page url
    :param Name: Username
    :param page_number: page nubmer of repos page
    :type Name:str
    :type Page:int
    :return: github repos url as string
    '''
    return "https://github.com/"+Name+"?page="+str(page_number)+"&tab=repositories"
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
def url_maker_star(Name,page_number):
    '''
    This function return github stars page url
    :param Name: username
    :param page_number: page number of stars
    :type Name :str
    :type page_number:int
    :return: github star url as string
    '''
    return "https://github.com/"+Name+"?page="+str(page_number)+"&tab=stars"
def repo_extract(input_string,username):
    '''
    This function extract repo from raw_html
    :param input_string: raw input html
    :param user_name: user_name
    :type input_string:str
    :type user_name:str
    :return: repo_list as list
    '''
    try:
        user_list=[]
        index=0
        shift=len(username)+1
        while(index!=-1):
            index=input_string.find('src="/'+username,index+shift,len(input_string))
            length=input_string[index:].find('graphs/')
            star_repo=input_string[index+5:index+length]
            if star_repo.find("<svg")==-1 and len(star_repo)!=0:
                user_list.append(star_repo)
        return user_list
    except Exception as ex:
        pass

def star_extract(input_string):
    '''
    This function extract stared repo from raw_html
    :param input_string: raw input html
    :param follower_name: follower_name
    :type input_string:str
    :type follower_name:str
    :return: user_list as list
    '''
    user_list=[]
    index=0
    try:
        while(index!=-1):
            index=input_string.find('<a class="muted-link mr-3',index+33,len(input_string))
            length=input_string[index+33:].find('stargazers">\n')
            star_repo=input_string[index+34:index+33+length]
            if star_repo.find("<svg")==-1 and len(star_repo)!=0:
                user_list.append(star_repo)
        return user_list
    except Exception as ex:
        pass
def org_list_gen(name):
    url=url_maker_follower(name,1)
    raw_data=get_html(url)
    org_index = raw_data.find("col-9 float-left pl-2")
    org_data = raw_data[:org_index]
    index=0
    org_list=[]
    while (index != -1):
        index = org_data.find('alt="@', index + 6, len(org_data))
        length = org_data[index + 6:].find('"')
        org_name = org_data[index + 6:index + 6 + length]
        if org_name != name:
            org_list.append(org_name)
    return org_list[:-1]
def user_list_gen(input_string,follower_name):
    '''
    This function extract usernames from raw_html
    :param input_string: raw input html
    :param follower_name: follower_name
    :type input_string:str
    :type follower_name:str
    :return: user_list as list
    '''
    try:
        user_list = []
        index = 0
        org_index=input_string.find("col-9 float-left pl-2")
        repo_data=input_string[org_index:]
        while(index!=-1):
            index=repo_data.find('alt="@',index+6,len(input_string))
            length=repo_data[index+6:].find('"')
            user_name=repo_data[index+6:index+6+length]
            if user_name!=follower_name:
                user_list.append(user_name)
        return user_list[:-1]
    except Exception as ex:
        pass
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
        pass


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
def follower_list_gen(follower_name,page_number=0,counter=0):
    '''
    This function generate follower_list
    :param follower_name: username
    :type follower_name:str
    :return: username follower list
    '''
    try:
        follower_list = []
        while (True):
            page_number += 1
            follower_url = url_maker_follower(follower_name, page_number)
            follower_html = get_html(follower_url)
            if end_check(follower_html) == True:
                break
            temp_list = user_list_gen(follower_html,follower_name)
            follower_list.extend(temp_list)
        return follower_list
    except Exception as ex:
        if counter>3:
            sys.exit()
        error_log("Error In Page "+str(page_number)+" Follower Page")
        follower_list_gen(follower_name,page_number,counter+1)
def repo_list(username,page_number=0,counter=0):
    '''
    This function return stared_repo list
    :param username: username
    :type username:str
    :return: stared repo as list
    '''
    try:
        repo_list_temp=[]
        while (True):
            page_number += 1
            repo_url = url_maker_repo(username, page_number)
            repo_html = get_html(repo_url)
            temp_list = repo_extract(repo_html,username)
            if len(temp_list)==0:
                break
            repo_list_temp.extend(temp_list)
        return repo_list_temp
    except Exception as ex:
        if counter>3:
            sys.exit()
        error_log("Error In Page " + str(page_number) + " Repos Page")
        repo_list(username,page_number,counter+1)
def star_list(username,page_number=0,counter=0):
    '''
    This function return stared_repo list
    :param username: username
    :type username:str
    :return: stared repo as list
    '''
    try:
        star_list_temp=[]
        while (True):
            page_number += 1
            star_url = url_maker_star(username, page_number)
            star_html = get_html(star_url)
            temp_list = star_extract(star_html)
            if len(temp_list)==0:
                break
            star_list_temp.extend(temp_list)
        return star_list_temp
    except Exception as ex:
        if counter>3:
            sys.exit()
        error_log("Error In Page " + str(page_number) + " Stars Page")
        star_list(username,page_number,counter+1)

def following_list_gen(follower_name,page_number=0,counter=0):
    '''
    This function generate following list
    :param follower_name: username
    :type follower_name:str
    :return: username following list
    '''
    try:
        following_list = []
        while (True):
            page_number+=1
            following_url = url_maker_following(follower_name, page_number)
            following_html = get_html(following_url)
            if end_check(following_html) == True:
                break
            temp_list = user_list_gen(following_html,follower_name)
            following_list.extend(temp_list)
        return following_list
    except Exception as ex:
        if counter>3:
            sys.exit()
        error_log("Error In Page " + str(page_number) + " Following Page")
        following_list_gen(follower_name,page_number,counter+1)

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

def internet(host="8.8.8.8", port=53, timeout=10):
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


def list_maker(username,keyword=["1"]):
    '''
    This function create following and follower list
    :param username: username
    :type username:str
    :return: (list_1,list_2) as tuple
    '''
    try:
        print("Collecting Follower Information ...")
        print_line(70, "*")
        list_1 = follower_list_gen(username)
        file = open(username + "_follower.log", "w")
        print(str(len(list_1)) + " Followers --> " + username + "_follower.log")
        print_line(70, "*")
        file.write("\n".join(list_1))
        file.close()
        print('Collecting Following Information ...')
        print_line(70, "*")
        list_2 = following_list_gen(username)
        file = open(username + "_following.log", "w")
        print(str(len(list_2)) + " Following --> " + username + "_following.log")
        print_line(70, "*")
        file.write("\n".join(list_2))
        file.close()
        if "1" in keyword:
            print('Collecting Stars Information ...')
            print_line(70, "*")
            stars=star_list(username)
            file = open(username + "_stars.log", "w")
            print(str(len(stars)) + " Stars --> " + username + "_stars.log")
            print_line(70, "*")
            file.write("\n".join(stars))
            file.close()
        if "2" in keyword:
            print('Collecting Repos Information ...')
            print_line(70, "*")
            repos = repo_list(username)
            file = open(username + "_repos.log", "w")
            print(str(len(repos)) + " Repos --> " + username + "_repos.log")
            print_line(70, "*")
            file.write("\n".join(repos))
            file.close()
        if "3" in keyword:
            print('Collecting Organizations Information ...')
            print_line(70, "*")
            orgs = org_list_gen(username)
            file = open(username + "_orgs.log", "w")
            print(str(len(orgs)) + " Organizations --> " + username + "_orgs.log")
            print_line(70, "*")
            file.write("\n".join(orgs))
            file.close()
        return (sorted(list_1),sorted(list_2))
    except Exception as ex:
        error_log(str(ex))

def dif(list_1,list_2,username):
    '''
    This function generate dif files
    :param list_1:follower list
    :param list_2: following list
    :type list_1:list
    :type list_2:list
    :return: None
    '''
    try:
        file = open(username + "_NotFollower.log", "w")
        dif_list_1 = list(set(list_2) - set(list_1))
        print(str(len(dif_list_1)) + " Following - Not Follower --> " + username + "_NotFollower.log")
        print_line(70, "*")
        file.write("\n".join(dif_list_1))
        file.close()
        file = open(username + "_NotFollowing.log", "w")
        dif_list_2 = list(set(list_1) - set(list_2))
        print(str(len(dif_list_2)) + " Follower - Not Following --> " + username + "_NotFollowing.log")
        print_line(70, "*")
        file.write("\n".join(dif_list_2))
        file.close()
        return [sorted(dif_list_1),sorted(dif_list_2)]
    except Exception as ex:
        print("[Error] dif function faild")
def unfollow(username,password,id_list):
    for user in id_list:
        response=requests.delete("https://api.github.com/user/following/" + user, auth=(username, password))
        status_code=int(response.status_code)
        if status_code!=204:
            if status_code==401:
                print("[Error] Authentication Error")
                return False
            elif status_code==403:
                print("[Error] Maximum number of login attempts exceeded")
                sys.exit()
            else:
                print("[Error] in " + user + " unfollow!")
        else:
            print(user+" Unfollowed")
        time.sleep(3)
    return True
def follow(username,password,id_list):
    for user in id_list:
        response = requests.put("https://api.github.com/user/following/" + user, auth=(username, password))
        status_code = int(response.status_code)
        if status_code!=204:
            if status_code==401:
                print("[Error] Authentication Error")
                return False
            elif status_code==403:
                print("[Error] Maximum number of login attempts exceeded")
                sys.exit()
            else:
                print("[Error] in "+user+" follow!")
        else:
            print(user+" Followed")
        time.sleep(3)
    return True
def get_input(func_1=input,func_2=input):
    tprint("git\nfollow")
    username = func_1("Please Enter Your Github Username : ")
    keys=func_2("1- Collecting Stars Information\n2- Collecting Repos Information\n3- Collecting Organizations Information (Enter Number Seperated By , )")
    keys=keys.split(",")
    return [username,keys]
def run(func_1=input,func_2=input,func_3=input):
    password = ""
    auth=False
    time_1 = time.perf_counter()
    [username,keys]=get_input(func_1=func_1,func_2=func_2)
    (list_1, list_2) = list_maker(username,keys)
    dif_lists = dif(list_1, list_2, username)
    time_2 = time.perf_counter()
    dif_time = str(time_2 - time_1)
    print("Data Generated In " + time_convert(dif_time) + " sec")
    print("Log Files Are Ready --> " + os.getcwd())
    if len(dif_lists[0])>0:
        input_data = func_3("Unfollow Non-follower?Yes[y],No[n] ")
        if input_data.upper() == "Y":
            while(auth==False):
                password = func_2("Please Enter Password : ")
                print("Processing ... ")
                auth=unfollow(username, password, dif_lists[0])
    if len(dif_lists[1])>0:
        input_data = func_3("Follow Non-following?Yes[y],No[n] ")
        if input_data.upper() == "Y":
            if auth==True:
                print("Processing ... ")
                auth= follow(username, password, dif_lists[1])
            while(auth==False):
                password = func_2("Please Enter Password : ")
                print("Processing ... ")
                auth=follow(username, password, dif_lists[1])
    gc.collect()

def test_function_1(a):
    return 'sarminh'
def test_function_2(a):
    return "1,2,3"
def test_function_3(a):
    return "y"












