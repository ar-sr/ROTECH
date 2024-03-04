text=input("Enter The Text:")
result_list=[0]*26
# print(result_list)


for  alphabet in text:
    result_list[ord(alphabet)-97]=result_list[ord(alphabet)-97]+1
print(result_list)


# ascii_values=97
# index=0


# for alphabet in text:
#     ascii_value=97
#     while (ascii_value):
#         # to loop inside asccii values 
        
        
#         if alphabet==chr(ascii_value):
#             result_list[index]=result_list[index]+1
#             # ascii_value-97 = index position
#             # eg: index of b= ascii_value of b(98)-97=2
#             break
            
#         ascii_value=ascii_value+1
        
        
# print(result_list)

    
    

    
    # print (char)
    # if text(0)=="a":
    #     result_list[0]=result_list[0]+1
    # if text(0)=="b":
    #     result_list[1]=result_list[1]+1
    # if text(0)=="c":
    #     result_list[2]=result_list[2]+1
    # if text(0)=="d":
    #     result_list[3]=result_list[3]+1
        
        
        


# print(f"a:{result_list[0]}")
# print(f"b:{result_list[1]}")
# print(f"c:{result_list[2]}")
# print(f"d:{result_list[3]}")
    
        
        
        