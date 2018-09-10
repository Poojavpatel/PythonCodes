class a:
    x=5
    def sayhello(self,name):
        print("Hello "+name)

class b:
    y=10
    def saybye(self,name):
        print("Byee "+name)

class c(a,b):
    p=2

c1= c()
print c1.p
c1.sayhello('disha')
c1.saybye('disha')
print c1.x
print c1.y
