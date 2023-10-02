import psutil

def processdisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)

        except(psutil.NoSuchprocess,psutil.AccessDenied,pustil.Zombieprocess):
            pass 

    return listprocess

def main():
    print("marvellous infosystem:python automation and machine learning")

    print("process monitor")

    listprocess=processdisplay()

    for elem in listprocess:
        print(elem)


if __name__ == "__main__":
    main()




