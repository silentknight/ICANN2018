#/usr/bin/python
import os
import random

def main():
	dirPath = "../data/"

	try:
		for root, dirs, files in os.walk(dirPath):
			files.sort()
			for name in files:
				print name

			# f = open(os.path.join(dirPath, files[0]),"r")
			# newData += f.readlines()
			# f.close()

			# f = open(os.path.join(dirPath, files[1]),"r")
			# newData += f.readlines()
			# f.close()

			# f = open(os.path.join(dirPath, files[2]),"r")
			# newData += f.readlines()
			# f.close()

			# final_data = list(set(newData))
			# random.shuffle(final_data)

			# final_data = ''.join(final_data)

			# f = open(os.path.join(dirPath, nameParts[0]+"_"+nameParts[2]+".txt"),"w")
			# f.write(final_data)
			# f.close()

	except TypeError as e:
 		print(e)


if __name__ == '__main__':
	main()

# 	dirPath = "data/SP"

# 	try:
# 		for root, dirs, files in os.walk(dirPath):
# 			files.sort()
# 			for name in files:
# 				nameParts = name.split('.')
# 				if nameParts[1] == "foma":
# 					nameHead = nameParts[0].split('-')
# 					filename = '../model_data/'+nameHead[0]+'_'+nameHead[3]+'_'+nameHead[2]+'.txt'
					
# 					name = os.path.join(root, name)

# 					if os.path.exists(filename):
# 						append_write = 'a'
# 					else:
# 						append_write = 'w'

# 					readText = open(name,"r")
# 					data = readText.readlines()
# 					readText.close()

# 					final_data = []
# 					for line in data:
# 						if line[0] == '[':
# 							part = line.split()
# 							final_data.append(part[1]+'\n')

# 					final_data = list(set(final_data))
# 					random.shuffle(final_data)
# 					final_data = ''.join(final_data)

# 					print(name)
# 					writeText = open(filename,append_write)
# 					writeText.write(final_data)
# 					writeText.close()
					
# 	except TypeError as e:
# 		print(e)

# if __name__ == '__main__':
# 	main()