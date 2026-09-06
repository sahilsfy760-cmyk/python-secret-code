import random
import string

all_chr = string.ascii_letters + string.digits







ch=input("What whould like to do code or decode: ")

#==================================
# code for converting code language
#==================================

coded_str=""
take_str=""

match ch.lower():
    
    case "code":
 
        eng=input("Enter your sentence:")
        
        for index,chr in enumerate(eng):

             if not chr.isspace():
                 take_str+=chr
  
             if chr.isspace() or index==len(eng)-1:
                 if len(take_str) in (1, 2):
                    coded_str+=take_str[::-1]+" "
                    take_str=""
                    
                 elif len(take_str)>2:
                     result1="".join(random.choices(all_chr, k=3))
                     result2="".join(random.choices(all_chr,k=3))
                     first_chr=take_str[0]
                     coded_str+=result1+take_str[1:]+first_chr+result2+" "
                     take_str=""
        print(coded_str)

#==================================
# code for converting code language
#==================================

    case "decode":
         decoded_str=""
         coded=input("Enter your  code sentence:")
         
         for index,chr in enumerate(coded):
              if not chr.isspace():
                 take_str+=chr
                 
              if chr.isspace() or index==len(coded)-1:
                 
                 if len(take_str) in (1, 2):
                    decoded_str+=take_str[::-1]+" "
                    take_str="" 
        
                
                 elif len(take_str)>2:
                     rmv_chr=take_str[3:-3]
                     first=rmv_chr[-1]
                     decoded_str+=first+rmv_chr[:-1]+" "
                     take_str="" 
         print(decoded_str)     
                            




  
