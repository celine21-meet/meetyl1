list1=[2,5,6,9,0]
list2=[2,4,6,8,0]
list3=[]
def common_numbers(list1,list2):
	for x in list1:
		for y in list2:
			if x==y:
				list3.append(x)
	return list3
print(common_numbers(list1,list2))


	




	
	