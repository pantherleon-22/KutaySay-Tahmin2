#!/usr/bin/env python
# coding: utf-8

# In[42]:


#deneme 3
import random
kelime_Listesi = ["kinder" "alle" ,"kinder","werfen" ,"grosse" ,"steine"]
işlevsiz_Kelime_karma = random.choice(kelime_Listesi)
harf_Listesi =  ['k', 'i', 'n', 'd', 'e', 'r', 'a', 'l', 'l', 'e', 'k', 'i', 'n', 'd', 'e', 'r', 'w', 'e', 'r', 'f', 'e', 'n', 'g', 'r', 'o', 's', 's', 'e', 's', 't', 'e', 'i', 'n', 'e']
doğru_Tahmin = random.choice(harf_Listesi)

can = 10

def seçim ():
    
    kullanıcı_Seçim = input("Sadece bir harf giriniz: ") 


while can > 0:
    seçim()
    

    if kullanıcı_Seçim == doğru_Tahmin:
       
        
        print("Tebrikler, doğru bildiniz!")
        print("Can değeriniz:", can)
        doğru_Tahmin = random.choice(harf_Listesi)
        
        
        break

    else:
        print("Ne yazık ki, yanıtınız doğru değil.")
        
        can -= 1
        print("Can değeriniz:", can)
        print("doğru tahmin",{doğru_Tahmin})
        
        doğru_Tahmin = random.choice(harf_Listesi)
        
        

        if can == 0:
            print(f"Kaybettin! Doğru tahmin: {doğru_Tahmin}")
            break


# In[ ]:




