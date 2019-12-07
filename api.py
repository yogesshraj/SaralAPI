# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses","r")
# # print (a.text)
# e={}
# with open("apisub.json","w") as b:
# 	# c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=c["availableCourses"]
# 	for i in range(len(d)):
# 		f=i+1,d[i]["id"]
# 		e[i+1]=d[i]["id"]
# print(e)


# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# f={}
# g=[]
# h=[]
# with open("apisub.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=(c["availableCourses"])
# 	for i in range(len(d)):
# 		e=(i+1,d[i]["id"])
# 		f[i+1]=d[i]["id"]
# # print (f)
# for j in f:
# 	g.append(j)
# 	h.append(f[j])
# # print (g)
# # print (h)
# a=int(input("Enter the number: "))
# for i in range(len(g)):
# 	if a==g[i]:
# 		print (h[i])



# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# # print (a)
# f={}
# g=[]
# h=[]
# with open("apisub.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=(c["availableCourses"])
# 	for i in range(len(d)):
# 		e=(i+1,d[i]["id"])
# 		f[i+1]=d[i]["id"]
# # print (f)
# for j in f:
# 	g.append(j)
# 	h.append(f[j])
# # print (g)
# # print (h)
# k=int(input("enter the number to get id "))
# for i in range(len(g)):
# 	if k==g[i]:
# 		x=(str(h[i]))
# 		z=requests.get("http://saral.navgurukul.org/api/courses/"+x+"/exercises")
# 		print (z.text)

# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print (a)
# f={}
# g=[]
# h=[]
# with open("apisub.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=c["availableCourses"]
# 	for i in range(len(d)):
# 		e= (i+1,d[i]["id"])
# 		f[i+1]=d[i]["id"]
# # print (f)
# for j in f:
# 	g.append(j)
# 	h.append(f[j])
# # print (g)
# # print (h)
# l=int(input("Enter the number to find the corresponding id: "))
# for i in range(len(g)):
# 	if l==g[i]:
# 		y= (str(h[i]))
# 		z=requests.get("http://saral.navgurukul.org/api/courses/"+y+"/exercises")
# 		# print (z.text)
# 		with open("apisub.json","w") as b:
# 			c=json.dump(z.text,b)
# 			c=json.loads(z.text)
# 			zx= (c["data"])
# 			for i in range(len(zx)):
# 				print (zx[i]["name"])

# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print (a)
# e={}
# f=[]
# g=[]
# with open("apisub.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=c["availableCourses"]
# 	for i in range(len(d)):
# 		print (i+1,d[i]["name"])

# 		e[i+1]=d[i]["id"]
# # print (e)
# print (" ")
# for j in e:
# 	f.append(j)
# 	g.append(e[j])
# # print (f)
# # print (g)
# k=int(input("Enter the number to get the corresponding id: "))
# print (" ")
# for i in range(len(f)):
# 	if k==f[i]:
# 		m= (str(g[i]))
# 		n=requests.get("http://saral.navgurukul.org/api/courses/"+m+"/exercises")
# 		# print (n.text)
# 		with open("apisub.json","w") as o:
# 			p=json.dump(n.text,o)
# 			p=json.loads(n.text)
# 			q=p["data"]
# 			for i in range(len(q)):
# 				print(q[i]["name"])
# 			r=input("Enter 'f' to move forward. 'p' to move previous. 'a' to be stable...")
# 			if r=="f":
# 				print ()


# import requests,json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print (a)
# with open("apisub.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	d=c["availableCourses"]
# 	e=int(input("Enter the number: "))
# 	f=[1]
# 	def api(e):
# 		for i in range(len(d)):
# 			g=d[i]["id"]
# 			f.append(g)
# 		# print (f)
# 		print (f[e])
# 		n=requests.get("http://saral.navgurukul.org/api/courses/"+str(f[e])+"/exercises")
# 		# print (n.text)
# 		o=json.loads(n.text)
# 		p= (o["data"])
# 		for i in range(len(p)):
# 			print (p[i]["name"])
# 		q=input("Enter 'f' to forward. 'p' to previous. 'm' to same...")
# 		if q=="f":
# 			api(e+1)
# 		elif q=="p":
# 			api(e-1)
# 		elif q=="m":
#
	# api(e)
# 	api(e)


# import requests,json,os
# e={}
# f=[]
# g=[]
# # if os.path.exists("apisub.json"):
# # 	with open("apisub.json","r") as b:
# # 		c=json.load(b)
# # 		c=json.loads(c)
#
#
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print (a)
# with open("apisub.json","w+") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
#
#
# d=c["availableCourses"]
# for i in range(len(d)):
# 	print (i+1,d[i]["name"])
#
# 	e[i+1]=d[i]["id"]
# print (e)
# print (" ")
# for j in e:
# 	f.append(j)
# 	g.append(e[j])
# print (f)
# print (g)
# e=int(input("Enter the number to get the corresponding id: "))
# print (" ")
# for i in range(len(f)):
# 	if e==f[i]:
# 		m= (str(g[i]))
# 		n=requests.get("http://saral.navgurukul.org/api/courses/"+m+"/exercises")
# 		# print (n.text)
# 		def api(e):
# 			with open("apisub.json","w") as o:
# 				p=json.dump(n.text,o)
# 				p=json.loads(n.text)
# 				q=p["data"]
# 				for i in range(len(q)):
# 					print(q[i]["name"])
# 				r=input("E

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
