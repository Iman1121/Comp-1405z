
def addend(list, dict, value):
	list.append(value)
	if(value in dict):
		dict[value] += 1
	else:
		dict.update({value:1})
	return None
	
def removestart(list,dict):
	if len(list) == 0:
		return None
	x = list.pop(0)
	dict[x] -= 1
	if(dict[x] == 0):
		del dict[x]
	return x
	
def containslinear(list, value):
	return value in list
	
def containshash(dict, value):
	if(value in dict):
		if(dict[value] != 0):
			return True
	return False

