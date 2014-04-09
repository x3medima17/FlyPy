import hello

def bsort(a):
	for i in xrange(len(a)):
		for j in xrange(len(a)):
			if a[i]<a[j]:
				a[i], a[j] = a[j],a[i]
	return a
a = [5,9,7,6,8,4,3,2,8,1,3] * 700

b = hello.bsort(a)
#b = bsort(a)