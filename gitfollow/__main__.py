from .gitfollow import *
import doctest
import sys
if __name__=="__main__":
    try:
        args=sys.argv
        if len(args)>1:
            if args[1].upper()=="TEST":
                doctest.testfile("test.py", verbose=True)
            else:
                print("Bad Input!")
                print("Test (Run doctest)")
                print("Without arg --> Normal Run")
        else:
            while(True):
                run()
                exit_string = input("Exit [E] / Restart[R] ?")
                if exit_string.upper()=="E":
                    break
    except Exception as ex:
        error_log(str(ex))












