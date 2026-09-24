def bs(arr,te):
    l=len(arr)
    low=0
    high=l-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==te:
            print("element found")
            return
        elif arr[mid]<te:
            low=mid+1
        else:
            high=mid-1
    print("element not found")
lis=[]
n=int(input("enter the size of the array :\t"))
for i in range(n):
    ele=int(input())
    lis.append(ele)
te=int(input("eneter the target element :\t"))
arr=sorted(lis)
bs(arr,te)























# import numpy as np
# def bs(arr,te):
#     l=len(arr)
#     low=0
#     high=l-1
#     while low <= high:
#         mid=(low+high)//2
#         if arr[mid]==te:
#             print("element found")
#             return
#         elif arr[mid]<te:
#             low=mid+1
#         else:
#             high=mid-1
#     print("element not found")
# lis=[]
# n=int(input("enter the size of the array :\t"))
# for i in range(n):
#     ele=int(input())
#     lis.append(ele)
# te=int(input("eneter the target element :\t"))
# slis=sorted(lis)
# arr=np.array(slis)
# bs(arr,te)