#!/usr/bin/python3.7


def deco(fun):
	def wrap(*args,**kargs):
		print("before")
		newtest=fun(*args,**kargs)
		print("after")
		return newtest
	return wrap

@deco
def test(num):
	print("this is decorate")
	return num+1

if __name__=="__main__":
	k=test(22)
	print(k)




	
