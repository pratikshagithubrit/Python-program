from sys import *


def Script_task(no):
    if((no%2)==0):
        print("even number")
    else:
        print("odd number")
def main():
    print("_________marvellous infosystem automation______")
    print("automation script started with name :",argv[0])

    if(len(argv)!=2):      #hayvrun decide hot ke apan aply output madey kiti argument deychy by default one arg delyla asto
        print("error:insufficient arguments")
        print("use -h for help and use -u for usage of the script")
        exit()
        

    if((argv[1]=="-h") or (argv[1] == "-H")):
        print("help:this script is used in perform_________")
        exit()

    elif((argv[1] == "-u") or (argv[1]=="-U")):
        print("usage:provide____number of argument as")
        print("first argument as:___")
        print("second argument as:___")
        exit()

    else:
        Script_task(int(argv[1]))
        
        


if __name__ == "__main__":
    main()


