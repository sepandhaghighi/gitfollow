'''
>>> import coverage
>>> from gitfollow import *
>>> from random import seed
>>> import os
>>> cov = coverage.Coverage()
>>> cov.start()
>>> zero_insert("22")
'22'
>>> zero_insert("320")
'320'
>>> zero_insert("2")
'02'
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert("15000")
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> url_maker_following("sepand",2)
'https://github.com/sepand?page=2&tab=following'
>>> url_maker_repo("sepand",2)
'https://github.com/sepand?page=2&tab=repositories'
>>> url_maker_follower("sepand",2)
'https://github.com/sepand?page=2&tab=followers'
>>> url_maker_star("sepand",2)
'https://github.com/sepand?page=2&tab=stars'
>>> data=get_html("http://github.com/sepandhaghighi?page=2&tab=follower")
>>> repo_lists=repo_list("sepandhaghighi",page_number=0,counter=0)
>>> star_lists=star_list("sarminh",page_number=0,counter=0)
>>> following_lists=following_list_gen("sarminh",page_number=0,counter=0)
>>> follower_lists=follower_list_gen("sarminh",page_number=0,counter=0)
>>> list_maker("sarminh",['1','2','3'])
Collecting Follower Information ...
**********************************************************************
2 Followers --> sarminh_follower.log
**********************************************************************
Collecting Following Information ...
**********************************************************************
2 Following --> sarminh_following.log
**********************************************************************
Collecting Stars Information ...
**********************************************************************
3 Stars --> sarminh_stars.log
**********************************************************************
Collecting Repos Information ...
**********************************************************************
0 Repos --> sarminh_repos.log
**********************************************************************
Collecting Organizations Information ...
**********************************************************************
0 Organizations --> sarminh_orgs.log
**********************************************************************
(['kasraaskari', 'sepandhaghighi'], ['kasraaskari', 'sepandhaghighi'])
>>> internet(host="8.8.8.8", port=53, timeout=3)
True
>>> seed(2)
>>> create_random_sleep(index=1,min_time=1,max_time=3)
1
>>> gitfollow.DEBUG=True
>>> seed(2)
>>> create_random_sleep(index=0)
Wait 5 sec for first search . . .
**********************************************************************
5
>>> gitfollow.DEBUG=False
>>> print_line(number=30,char="-")
------------------------------
>>> dif(["test1","test2","test3"],["test2","test3","test5","test6"],"test")
2 Following - Not Follower --> test_NotFollower.log
**********************************************************************
1 Follower - Not Following --> test_NotFollowing.log
**********************************************************************
[['test5', 'test6'], ['test1']]
>>> error_log("log_test")
>>> file=open(os.path.join("log","error_log.txt"),"r")
>>> data=file.read()
>>> data.find("log_test")
31
>>> unfollow("sarminh","password_test",["id_1","id_2"])
[Error] Authentication Error
False
>>> follow("sarminh","password_test",["id_1","id_2"])
[Error] Authentication Error
False
>>> orgs=org_list_gen("sarminh")
>>> repo_extract(2222,'ssss')
>>> star_extract(2222)
>>> user_list_gen(22222,'salam')
>>> data=get_html('https://github.com/asdasdqweqweqweqweqwe?page=0&tab=followers')
Traceback (most recent call last):
        ...
SystemExit
>>> dif(1212,121221,"sasa")
[Error] dif function faild
>>> run(func_1=test_function_1,func_2=test_function_2,func_3=test_function_3)
>>> help_func()
<BLANKLINE>
 .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |  _________   | || |   _____      | || |   ______     | |
| | |_   ||   _| | || | |_   ___  |  | || |  |_   _|     | || |  |_   __ \   | |
| |   | |__| |   | || |   | |_  \_|  | || |    | |       | || |    | |__) |  | |
| |   |  __  |   | || |   |  _|  _   | || |    | |   _   | || |    |  ___/   | |
| |  _| |  | |_  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |_      | |
| | |____||____| | || | |_________|  | || |  |________|  | || |  |_____|     | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'
<BLANKLINE>
By Sepand Haghighi
<BLANKLINE>
python -m gitfollow
- run  (run gitfollow)
<BLANKLINE>
- test (run tests)
<BLANKLINE>
- help (help page)
<BLANKLINE>
>>> cov.stop()
>>> cov.save()

'''