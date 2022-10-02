#Adding user order to the queue
import threading
import time
from QueueClass import Queue
Order_Queue = Queue()
start = time.perf_counter()

class ShopFunctions:

    def __init__(self):
        self.q = Queue()
        self.x = None
        self.y = None
    
    def AddOrder(self,order):
        self.q.enQueue(order)

    def DisplayOrders(self):
        self.q.displayQueue()
    
    def ShowPrice(self,order):
        self.tprice = order[4]
        print(f"\nThe Final Price is: {self.tprice}\nPlease pay at the Checkout Thankyou!")
        self.ChangeStatus(order)    

    def ChangeStatus(self,order):
        order[3] = 'complete'
        

    def Interior(self):
        print("Cleaning Up Car Interior...")
        time.sleep(3)
        print("Done Cleaning Interior.")
    def Exterior(self):
        print("Washing The Exterior...")
        time.sleep(2)
        print("Done Washing Exterior")

    def Full(self):
        self.Interior()
        self.Exterior()

    def Oil_Change(self):
        print("Changing Oil...")
        time.sleep(2)
        print("Finished Oil Change")

    def Tire_Maintenance(self):
        print("Tire Maintenance occuring...")
        time.sleep(1)
        print("Finished Tire Maintenance")

    def Full_Car_Check(self):
        print("Full Car Maintenance in Progress...")
        time.sleep(4)
        print("Finishing Car maintenance")

    def Custom_Issues(self):
        print("Custom Order...")
        time.sleep(2)
        print("Finished Custom Order")

    def Tinted_Windows(self):
        print("Custom Window Customization..")
        time.sleep(3)
        print("Finished Customization")

    def Custom_Rims(self):
        print("Custom Rims Customization..")
        time.sleep(3)
        print("Finished Customization")
        
    def Custom_Exhaust(self):
        print("Custom Exhaust Customization..")
        time.sleep(3)
        print("Finished Customization")

    def separateName(self,order):
        func = order[2]
        result = eval('self.' + func + "()")

    def ManageFunction(self,Orderx,Ordery):
        if Orderx[0] != Ordery[0]:
            print("Execute Multithread")
            t1 = threading.Thread(target=self.separateName,args=(Orderx,))
            t2 = threading.Thread(target=self.separateName,args=(Ordery,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            self.separateName(self.x)
            self.separateName(self.y)
    def RunOrder(self):
        #check if there is an order in the queue
        self.x = self.q.deQueue()
        if self.x == -999:
            print ("No Orders")
        else:
            self.y = self.q.deQueue()
            if self.y == -999:
                self.separateName(self.x)
                self.ShowPrice(self.x)
            else:
                self.ManageFunction(self.x,self.y)
            
        #if there is an order then, Expand it,
        #now copy the function for it into the appropriate function call
        #run function,
        #once it is completed, run the appropriate payment
        #now do this again for the next element in the queue



#with concurrent.futures.ThreadPoolExecutor() as executor:
#    f1 = executor.submit(RunOrder,Order_Queue.deQueue())
#    f2 = executor.submit(RunOrder,Order_Queue.deQueue())
#    print(f1.result())
#    print(f2.result())
#
#end = time.perf_counter()
#t = round(end - start,2)
#print(f"Total Time: {t}")