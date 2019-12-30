import requests,json,os
e={}
f=[]
g=[]

if os.path.exists("apisub.json"):
	with open("apisub.json","r") as b:
		c=json.load(b)
		c=json.loads(c)
else:
	a=requests.get("http://saral.navgurukul.org/api/courses")
	print (a)
	with open("apisub.json","w+") as b:
		c=json.dump(a.text,b)
		c=json.loads(a.text)
d= (c["availableCourses"])
for i in range(len(d)):
	e[i+1]=d[i]["id"]
	print (i+1,d[i]["name"])
# print (e)
for i in e:
	f.append(i)
	g.append(e[i])
# print (f)
# print (g)
print (" ")
h=int(input("Enter the number to get corresponding id: "))
print (" ")
def api(z):
	for i in range(len(f)):
		if z==f[i]:
			k= str(g[i])
			if os.path.exists(k+".json"):
				with open(k+".json","r") as b:
					m=json.load(b)
					m=json.loads(m)
			else:
				j=requests.get("http://saral.navgurukul.org/api/courses/"+k+"/exercises")
				n= (j.text)
				with open(k+".json","w+") as l:
					m=json.dump(n,l)
					m=json.loads(n)
			q= (m["data"])
			for i in range(len(q)):
				print(q[i]["name"])
			print (" ")
			r=input("Enter 'f' to move forward, 'p' to previous, 's' to be stable: ")
			if r=="f":
				api(z+1)
			elif r=="p":
				api(z-1)
			elif r=="s":
				api(z)
api(h)
