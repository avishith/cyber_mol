
front1=" => "
front2=". what is "
end=" ?"
index=1


key = ["firewall","phishing Attack","RAT","RAT","internet","VPN","APN","DDos Attack","Carding","Tail os","Dark net","vires","kali Linux","hosting","server","database","ip address","clints & servers","git hub","RDP","anti-vires",]

qus = []
c=5
d=12
m=10
y="2020"
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
print(i)
 