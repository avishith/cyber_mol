
front1=" => "
front2=". what is "
end=" ?"
index=1


key = ["firewall","phishing Attack","RAT","RAT","internet","VPN","APN","DDos Attack","Carding","Tail os","Dark net","vires","kali Linux","hosting","server","database","ip address",
"clints & servers","git hub","RDP","anti-vires","Vulnerability","http","https","SSL","URL","Keystroke logging","Metasploit","NMAP","BIN","NETFLIX","nord VPN"," CC Generator","block chain","cryptocurrency","google SEO","anonymous in hacking","SQL","SQL injections","steganography","Man In The Middle Attacks "]

qus = []
c=5
d=12
m=10
y="2020"
print(" \n 1.view  all qustions \n 2.view quistions datewise \n 3. find with date")
want=input("\n =>enter your choise :- ")
if want=="2":
    for i in key: 
        if i not in qus:
            if(c%5==0):
                print("")
                print(str(d)+'/'+str(m)+'/'+str(y))
                print("")
                d=d+1
            
            qus.append(i)
            Q = front1+str(index) + front2 + i + end
            print(Q)
            index=index+1 
            c=c+1
if want=="3":
    count=1
    c=1
    day=int(input(' =>which Date(example:12) :-'))
    print(str(day)+'/'+str(m)+'/'+str(y))
    for i in key:
        if i not in qus:
            if day==d:
                qus.append(i)
                Q = front1+str(index) + front2 + i + end
                print(Q)
                index=index+1
                
                if count==5:
                    break
                count=count+1
            else:
                qus.append(i)
                if(c%5==0):
                    d=d+1
                c=c+1
if want=="1":
    print("\n")
    for i in key: 
        if i not in qus:
            
            qus.append(i)
            Q = front1+str(index) + front2 + i + end
            print(Q)
            index=index+1 
        
                
                
           
# for i in key: 
#     if i not in qus:
#         if(c%5==0):
#             print("")
#             print(str(d)+'/'+str(m)+'/'+str(y))
#             print("")
#             d=d+1
        
#         qus.append(i)
#         Q = front1+str(index) + front2 + i + end
#         print(Q)
#         index=index+1 
#         c=c+1

 