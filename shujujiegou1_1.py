from collections import deque

def search(lines,pattern,history=5):
	previous_lines =deque(maxlen=history)
	for li in lines:
		if pattern in li:
			previous_lines.append(li)    #交换顺序结果丢失一条  12条
			yield li , previous_lines    #理解yield原理

			

if __name__ =="__main__":

	with open("D:\python\cookbook\\python.txt") as f:
		for line,prevlines in search(f,"python",5):
			for pline in prevlines:
				print(pline,end="")


			#print(line,end="")  #
			print('-'*20)
