l1 = [1,2,[3,4,5],[[6],[[[7,[None]],[8,9]]]]]

l2=[]

def r(ls):
	for i in ls:
		if isinstance(i,list):
			r(i)
		else:
			l2.append(i)

r(l1)
print(l2)

def demo():
	print("demo")