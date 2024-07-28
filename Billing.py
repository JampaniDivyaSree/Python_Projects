class shop:
    def shirts(self):
        shirts={1:["checks",300],2:["plain",400]}
        n=int(input("select your choice:" ))
        count=int(input("enter the count:"))
        print("cost:",shirts.get(n)[1]*count)


    def grocerry(self):
        items={1:["spices",500],2:["some",600]}
        print(items)
        n=int(input("select your choice:" ))
        count=int(input("enter the count:"))
        print("cost:",items.get(n)[1]*count)
        
s=shop()
select=int(input("enter your choice(1.shirts,2.grocerry):"))
if select==1:
    s.shirts()
else:
    s.grocerry()
        