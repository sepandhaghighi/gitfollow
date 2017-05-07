import requests
import sys
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
    new_session=requests.session()
    new_session.cookies.clear()
    raw_html=new_session.get(url)
    return raw_html.text


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

if __name__=="__main__":
    follower_name="sepandhaghighi"
    list_1=follower_list_gen(follower_name)
    print(list_1)











