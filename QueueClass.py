


class Node:
	def __init__(self):
		self.data = None
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None

	def delOrder(self,order):
		temp = self.front
		
		if self.front.data[1] == order:
			self.deQueue()
			#self.front != self.front
			#self.front.next
			#temp =temp.next;
			temp.next = self.front

		while temp.data != self.rear.data:
			#print("tempdata is: ", temp.data, "\nrear is: ",self.rear.data);
			if temp.next.data[1] == order :
				temp.next = temp.next.next
				break
			elif order != temp.data and temp.next.next == self.rear:
				print("Item not found in the list.")
				break
			else:
				temp = temp.next
		
		#self.front = None
		#self.rear.link = self.front
		#temp.next = self.front.next.next
		
	def enQueue(q, value):
		temp = Node()
		temp.data = value
		if q.front == None:
			q.front = temp
		else:
			q.rear.next = temp

		q.rear = temp
		q.rear.next = q.front

# Function to delete element from
# Circular Queue
	def deQueue(q):
		if (q.front == None):
			#print("Queue is empty")
			return -999

		# If this is the last node to be deleted
		value = None # Value to be dequeued
		if (q.front == q.rear):
			value = q.front.data
			q.front = None
			q.rear = None
		else: # There are more than one nodes
			temp = q.front
			value = temp.data
			q.front = q.front.next
			q.rear.next = q.front

		return value
	def displayQueue(q):
		temp = q.front
		print("Elements in Circular Queue are: ",end = " ")
		while (temp.next != q.front):
			print(temp.data, end = " ")
			temp = temp.next
		print(temp.data)

# Q = Queue()
# Q.enQueue(1)
# Q.enQueue(2)
# Q.enQueue(3)
# Q.enQueue(4)
# Q.displayQueue()
# Q.delOrder(2)
# Q.displayQueue()