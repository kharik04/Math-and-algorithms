############################# Symbolic expression parser ######################################
#Author: Khariton Gorbunov
#The script evaluates expressions, it will convert a string to a number, for example
#"(sin(1.5)/cos(6))^1.5-3*9" will become -25.9
###############################################################################################
import math
def power(expression):
	exp1=[]
	i=0

	while i < len(expression):
		if(expression[i]=="^"):
			exp1.pop()
			exp1.append(expression[i-1]**expression[i+1])
			i=i+1
		else:
				exp1.append(expression[i])
		i=i+1
	return (exp1)

def divide(exp1):
	exp2=[]
	i=0
	while i < len(exp1):
		if(exp1[i]=="/"):
			exp2.pop()
			exp2.append(exp1[i-1]/exp1[i+1])
			i=i+1
		else:
				exp2.append(exp1[i])
		i=i+1
	return (exp2)

def multiply(exp2):
	exp3=[]
	i=0
	while i < len(exp2):
		if(exp2[i]=="*"):
			exp3.pop()
			exp3.append(exp2[i-1]*exp2[i+1])
			i=i+1
		else:
				exp3.append(exp2[i])
		i=i+1
	return(exp3)

def subtract(exp3):
	exp4=[]
	i=0
	while i < len(exp3):
		if(exp3[i]=="-"):
			exp4.pop()
			exp4.append(exp3[i-1]-exp3[i+1])
			i=i+1
		else:
				exp4.append(exp3[i])
		i=i+1
	return(exp4)

def add(exp4):
	exp5=[]
	i=0
	while i < len(exp4):
		if(exp4[i]=="+"):
			exp5.pop()
			exp5.append(exp4[i-1]+exp4[i+1])
			i=i+1
		else:
				exp5.append(exp4[i])
		i=i+1
	return(exp5)
def trig(li):
	output=[]
	i=0

	while i < len(li):
		if(li[i]=="c" and li[i+1]=="o" and li[i+2]=="s"):
			output.append(math.cos(li[i+3]))
			i=i+3
		elif(li[i]=="s" and li[i+1]=="i" and li[i+2]=="n"):
			output.append(math.sin(li[i+3]))
			i=i+3
		elif(li[i]=="t" and li[i+1]=="a" and li[i+2]=="n"):
			output.append(math.tan(li[i+3]))
			i=i+3

		else:
				output.append(li[i])
		i=i+1
	return (output)	



def algebra1(b):

	isnumber=0
	currentnumber=""
	expression=[]
	exp1=[]
	exp2=[]
	exp3=[]
	exp4=[]
	exp5=[]
	a=[]
	i=0
	b="0"+b
	while i< len(b):
		if((b[i]=="+"and b[i+1]=="-") or (b[i]=="-"and b[i+1]=="+")):
			a.append("-")
			i=i+1
		else:
			a.append(b[i])
		i=i+1


	for i in range (0,len(a)):
		if(a[i]=="0" or a[i]=="1" or a[i]=="2" or a[i]=="3" or a[i]=="4" or a[i]=="5" or a[i]=="6" or a[i]=="7" or a[i]=="8" or a[i]=="9" or a[i]=="."):
			isnumber=1;
			currentnumber+=a[i]
		else:
			if(isnumber==1):
				isnumber=0
				expression.append(float(currentnumber));
				currentnumber=""
			expression.append(a[i])
		if(isnumber==1 and i==len(a)-1):
			expression.append(float(currentnumber))
		

	#exponent
	i=0
	while i < len(expression):
		if(expression[i]=="^"):
			exp1.pop()
			exp1.append(expression[i-1]**expression[i+1])
			i=i+1
		else:
				exp1.append(expression[i])
		i=i+1
	#div
	i=0
	while i < len(exp1):
		if(exp1[i]=="/"):
			exp2.pop()
			exp2.append(exp1[i-1]/exp1[i+1])
			i=i+1
		else:
				exp2.append(exp1[i])
		i=i+1
	#mult
	i=0
	while i < len(exp2):
		if(exp2[i]=="*"):
			exp3.pop()
			exp3.append(exp2[i-1]*exp2[i+1])
			i=i+1
		else:
				exp3.append(exp2[i])
		i=i+1
	#-
	i=0
	while i < len(exp3):
		if(exp3[i]=="-"):
			exp4.pop()
			exp4.append(exp3[i-1]-exp3[i+1])
			i=i+1
		else:
				exp4.append(exp3[i])
		i=i+1

	#+
	i=0
	while i < len(exp4):
		if(exp4[i]=="+"):
			exp5.pop()
			exp5.append(exp4[i-1]+exp4[i+1])
			i=i+1
		else:
				exp5.append(exp4[i])
		i=i+1


	return(str(exp5[0]))

def algebra(b):

	isnumber=0
	currentnumber=""
	expression=[]
	exp1=[]
	exp2=[]
	exp3=[]
	exp4=[]
	exp5=[]
	a=[]
	i=0
	b="0+"+b
	while i< len(b):
		if((b[i]=="+"and b[i+1]=="-") or (b[i]=="-"and b[i+1]=="+")):
			a.append("-")
			i=i+1
		else:
			a.append(b[i])
		i=i+1


	for i in range (0,len(a)):
		if(a[i]=="0" or a[i]=="1" or a[i]=="2" or a[i]=="3" or a[i]=="4" or a[i]=="5" or a[i]=="6" or a[i]=="7" or a[i]=="8" or a[i]=="9" or a[i]=="."):
			isnumber=1;
			currentnumber+=a[i]
		elif(a[i]=="+" or a[i]=="-" or a[i]=="*" or a[i]=="/" or a[i]=="^" or a[i]=="(" or a[i]==")"):
			if(isnumber==1):
				isnumber=0
				expression.append(float(currentnumber));
				currentnumber=""
			expression.append(a[i])
		else:
			if(isnumber==1):
				isnumber=0
				expression.append(float(currentnumber));
				currentnumber=""
			expression.append(a[i])

		if(isnumber==1 and i==len(a)-1):
			expression.append(float(currentnumber))

	val=add(subtract(multiply(divide(power(trig(expression))))))
	return(str(val[0]))

def findparent(b):
	c=[]
	d=[]
	startindex=0
	stopindex=0
	for i in range (0,len(b)):
		if (b[i]=="("):
			startindex=i
		if(b[i]==")"):
			stopindex=i
			for k in range (startindex+1,stopindex):
				c.append(b[k])
			break
	stringexp = ''.join(c)
	for i in range (0,startindex):
		d.append(b[i])
	d.append(algebra(stringexp))
	for i in range (stopindex+1,len(b)):
		d.append(b[i])



	return(d)

expression="(sin(1.5)/cos(6))^1.5-3*9"
mylist = expression
pnr=0;
for i in range (0,len(mylist)):
	if(mylist[i]=="("):
		pnr+=1
for i in range(0,pnr):
	mylist=''.join(findparent(mylist))

answer=algebra(mylist)
print("Answer:")
print(expression+"="+str(answer))