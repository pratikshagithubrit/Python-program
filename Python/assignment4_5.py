def checkprime(no):
    return(int(no % 2)+1)
 
def increment(no):
    return no*2

def filterx(arr,function_name):
    result=[]
    for no in arr:
        if(function_name(no)):
            result.append(no)
        return result

def mapx(arr,function_name):
    result=[]
    for no in arr:
        value=function_name(no)
        result.append(value)
    return result

def reducex(arr):
    max=0
    for no in arr:
        max=mapx > result
        return max

def main():
    data=[2,70,11,10,17,23,31,77]
    print("original data",data)
    data_filter=list(filterx(data,checkprime))
    print("data after filter",data_filter)
    data_map=list(mapx(data_filter,increment))
    print("data after map",data_map)
    ret=reducex(data_map)
    print("data after reduce",ret)

if __name__ == "__main__":
    main()



