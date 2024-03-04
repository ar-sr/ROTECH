file_handler=open("content.txt",'+r')
text=file_handler.read()



# text=input("enter the text:")
# text=text.lower()
# method chaining

result_dict={}

for ascii_value in range(97,(97+26)):
    result_dict[chr(ascii_value)]=0



for alphabet in text:
    if(alphabet.isalpha()):
        result_dict[alphabet]=result_dict[alphabet]+1   
    
print(result_dict)
    
    

