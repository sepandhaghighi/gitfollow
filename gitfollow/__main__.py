from .gitfollow import *
import os
import gc
if __name__=="__main__":
    try:
        password=""
        time_1=time.perf_counter()
        username=input("Please Enter Your Github Username : ")
        (list_1,list_2)=list_maker(username)
        dif_lists=dif(list_1,list_2,username)
        print(dif_lists)
        time_2=time.perf_counter()
        dif_time=str(time_2-time_1)
        print("Data Generated In "+time_convert(dif_time)+" sec")
        print("Log Files Are Ready --> " + os.getcwd())
        input_data=input("Unfollow Non-follower?Yes[y],No[n] ")
        if input_data.upper()=="Y":
            password=input("Please Enter Password : ")
            print("Processing ... ")
            unfollow(username,password,dif_lists[0])
        input_data = input("Follow Non-following?Yes[y],No[n] ")
        if input_data.upper()=="Y":
            if len(password)<1:
                password=input("Please Enter Password : ")
            print("Processing ... ")
            follow(username,password,dif_lists[0])
        gc.collect()
    except Exception as ex:
        error_log(str(ex))












