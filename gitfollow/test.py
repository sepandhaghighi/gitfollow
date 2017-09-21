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
>>> repo_lists=repo_list("sarminh",page_number=0,counter=0)
>>> star_lists=star_list("sarminh",page_number=0,counter=0)
>>> following_lists=following_list_gen("sarminh",page_number=0,counter=0)
>>> follower_lists=follower_list_gen("sarminh",page_number=0,counter=0)
>>> list_maker("sarminh")
Collecting Follower Information ...
**********************************************************************
0 Followers --> sarminh_follower.log
**********************************************************************
Collecting Following Informnation ...
**********************************************************************
1 Following --> sarminh_following.log
**********************************************************************
Collecting Stars Informnation ...
**********************************************************************
0 Stars --> sarminh_stars.log
**********************************************************************
Collecting Repos Informnation ...
**********************************************************************
0 Repos --> sarminh_repos.log
**********************************************************************
([], ['sepandhaghighi'])
>>> internet(host="8.8.8.8", port=53, timeout=3)
True
>>> seed(2)
>>> create_random_sleep(index=1,min_time=1,max_time=3)
1
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
>>> follow("sarminh","password_test",["id_1","id_2"])
Traceback (most recent call last):
        ...
SystemExit
>>> orgs=org_list_gen("sarminh")
>>> cov.stop()
>>> cov.save()

'''