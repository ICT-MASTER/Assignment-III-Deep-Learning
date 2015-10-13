import pickle
 
 
def print_if_iter(obj, depth):
	if hasattr(obj, '__iter__'):
		print('\t'*depth,type(obj), ':',len(obj))
		if len(obj) < 5:
			for child in obj:
				print_if_iter(child, depth+1)
		else:
			print_if_iter(obj[0],depth+1)
	else:
		print('\t'*depth,type(obj),':')

def loop_through(root):
	print(type(root), ':',len(root))
	for i,obj in enumerate(root):
		print_if_iter(obj,1)

 
if __name__ == '__main__':
	f = open('test.pikk', 'r')
	p = pickle.load(f)
	loop_through(p)