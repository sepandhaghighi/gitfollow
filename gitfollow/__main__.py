from .gitfollow import *
import os
if __name__=="__main__":
    time_1 = time.perf_counter()
    username = input("Please Enter Your Github Username : ")
    (list_1, list_2) = follow(username)
    dif(list_1, list_2)
    time_2 = time.perf_counter()
    print("Data Generated In " + str(time_2 - time_1) + " sec")
    print("Log Files Are Ready --> " + os.getcwd())
    gc.collect()










