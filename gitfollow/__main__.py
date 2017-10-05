from .gitfollow import *
import doctest
import sys
def start_loop():
    while (True):
        run()
        exit_string = input("Exit [E] / Restart[R] ?")
        if exit_string.upper() == "E":
            break
if __name__=="__main__":
    try:
        args=sys.argv
        if len(args)>1:
            if args[1].upper()=="TEST":
                doctest.testfile("test.py", verbose=True)
            elif args[1].upper()=="RUN":
                start_loop()
            elif args[1].upper()=="HELP":
                help_func()
            else:
                print("Bad Input!")
                help_func()
        else:
            start_loop()
    except Exception as ex:
        error_log(str(ex))












