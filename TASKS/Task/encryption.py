file_handler=open("demo.txt",'+r')
# file_handler.write("As of October, Python  is the stable release, and  and  are the only versions with active (as opposed to just security) support. Notable changes in include increased program execution speed and improved error reporting.")
text=file_handler.read()
print(text)





# # print(text)
# # text="germany"

for alp in text:
     res=chr(ord(alp)+2) 
     encrypted= ''.join(res)
     print(encrypted,end="")


# for alphabet in text:
#     if(alphabet.isalpha()):
#         text[alphabet]=text[alphabet]+1   


     