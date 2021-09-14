def sorter(a):
	n = len(a)
	swapped = True
	start = 0
	end = n-1
	while (swapped==True):
		swapped = False
		for i in range (start, end):
			if (a[i] > a[i+1]) :
				a[i], a[i+1]= a[i+1], a[i]
				swapped=True

		if (swapped==False):
			break
		swapped = False
		end = end-1
		for i in range(end-1, start-1,-1):
			if (a[i] > a[i+1]):
				a[i], a[i+1] = a[i+1], a[i]
				swapped = True
		start = start+1

n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
    
sorter(ele)
print("Sorted array is:")
for i in range(len(ele)):
	print ("%d" %a[i]),
