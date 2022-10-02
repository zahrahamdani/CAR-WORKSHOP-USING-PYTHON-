
import threading
import time
import random
import sys
from Order import ShopFunctions


#car_wash_option = ("Full","Interior","Exterior","Tires")
#car_wash_optionprice = (800,400,500,100)
order_flags = ('none','inprocess','skipped','processing','complete')
#Make a database of all possible orders

class OrderProgram:

    OrderList_CarWash = [('Full',800),('Interior',400),('Exterior',500),('Polish',100),('NoPolish',0)]
    OrderList_WorkShop = [('Oil_Change',100),('Tire_Maintenance' , 50),('Full_Car_Check', 1000), ('Custom_Issues',0)]
    OrderList_CarCustom = [('Tinted_Windows',2000),('Custom_Rims',1500),('Custom_Exhaust',1300)]
    OrderType = ('CarWash','WorkShop','Customization')
    def __init__(self):
        self.srNum = 0
        self.orderName = None
        self.orderTag = order_flags[0]
        self.orderPrice = None
        self.modifier = None
        self.totalMoney = 0
        self.orderingtype = None

    def createOrderCarWash(self,orderIndex):
        self.orderingtype = self.OrderType[0]
        self.srNum += 1
        self.orderName = self.OrderList_CarWash[orderIndex][0]
        self.orderTag = order_flags[1]
        self.orderPrice = self.OrderList_CarWash[orderIndex][1]

    def createOrderWorkShop(self,orderIndex):
        self.orderingtype = self.OrderType[1]
        self.srNum += 1
        self.orderName = self.OrderList_WorkShop[orderIndex][0]
        self.orderTag = order_flags[1]
        self.orderPrice = self.OrderList_WorkShop[orderIndex][1]

    def createOrderCustomization(self,orderIndex):
        self.orderingtype = self.OrderType[2]
        self.srNum += 1
        self.orderName = self.OrderList_CarCustom[orderIndex][0]
        self.orderTag = order_flags[1]
        self.orderPrice = self.OrderList_CarCustom[orderIndex][1]

    def createOrder(self,orderIndex,order_type):
        if self.OrderType[order_type] == 'CarWash':
            self.createOrderCarWash(orderIndex)
        elif self.OrderType[order_type] == 'WorkShop':
            self.createOrderWorkShop(orderIndex)
        elif self.OrderType[order_type] == 'Customization':
            self.createOrderCustomization(orderIndex)
        return

    #maybe make a both order option
    def printOrder(self):
        print("\nYour Order Summary:")
        print(f"Order No.{self.srNum}\nOrdering Service: {self.orderName}\nOrder Status:{self.orderTag}\nOrder Price: {self.orderPrice}")
        if self.orderingtype == 'CarWash':
            self.totalMoney = self.orderPrice + self.modifier[1]
            print(f"Extras: {self.modifier}")
        else: 
            self.totalMoney = self.orderPrice
        print("Total Payable Amount:", self.totalMoney)
        print(f"Please move towards the {self.orderingtype} and wait for your order number")
        return [self.orderingtype,self.srNum,self.orderName,self.orderTag,self.totalMoney]
    #maybe make an edit order
    def randOrder(self):
            x = random.randint(0,2)
            y = random.randint(0,2)
            self.createOrder(x,y)
            self.modifier = self.OrderList_CarWash[3]
            return self.printOrder()


class Menu():
    def __init__(self):
        self.order = OrderProgram()
        self.sf = ShopFunctions()
        self.time_slots = ['1. 13:00', '2. 14:00', '3. 15:00', '4. 16:00', '5. 17:00', '6. 18:00','7. 19:00','8. 20:00']
    #-----------------------------------
    def Extras(self):
        _ = ('Y','N')
        print("Do you want to add Shiner/Polish? for 100rs")
        choice = input("Press Y or N to choose: ")
        choice = choice.upper()
        if choice == _[0]:
            print ("Adding Polish for 100rs")
            self.order.modifier = self.order.OrderList_CarWash[3]
        elif choice == _[1]:
            print ("Not Adding Polish")
            self.order.modifier = self.order.OrderList_CarWash[4]
            return
        else:
            print("User entered invalid value")
            self.Extras()
        return

    def Appointment(self):
        
        print("These are the Time Slots for Appointment:\nYou can pick any time from this list")
        for x in range(len(self.time_slots)):
            print(self.time_slots[x])
        appointment_choice = input("Enter the alphabet to select that particular time slot: ")
        usr_appointment = self.time_slots[int(appointment_choice)-1] 
        self.time_slots.remove(self.time_slots[int(appointment_choice) - 1])
        print ("You have selected appointment for ",usr_appointment )
        print("Slots left: ", self.time_slots)
        s = input("\nSelect Order:\n1. Car Wash\t\t2. Car WorkShop")
        if s == '1':
            self.CarWash()
        elif s == '2':
            self.CarWorkShop()

        #user will select an appointment. we delete it from the list
        #keep the counter running and if the time passes the appointment and user
        #does not show up then order is marked skipped and next order is executed



    def CarWash(self):
        print("[+]Car Wash: ","\n\t1. Full - 800rs\n\t2. Interior - 400rs\n\t3. Exterior - 500rs")
        choice = input("Enter Your Choice: ")
        choice = int(choice)
        if choice == 1:
            self.order.createOrder(0,0)
        elif choice == 2:
            self.order.createOrder(1,0)
        elif choice == 3:
            self.order.createOrder(2,0)
        else: 
            "\nUser Entered Wrong Value\n"
            self.CarWash()
        self.Extras()
        #self.order.printOrder()
        
    def CarWorkShop(self):
        choice = input("\nPress 1 to Enter Car WorkShop.\nPress 2 for Customization Shop\n")
        if choice == '1':
            print("Car Workshop:\n1. Oil Change 100rs\n2. Tires - 50rs\n3. Full Checkup - 1000rs\n4. Other Problems - Price Varies")
            choice2 = input("Enter your Choice: ")
            if choice2 == '1':
                self.order.createOrder(0,1)
            elif choice2 == '2':
                self.order.createOrder(1,1)
            elif choice2 == '3':
                self.order.createOrder(2,1)
            elif choice2 == '4':
                self.order.createOrder(3,1)
        elif choice == '2':
            print("\nCar Customization:\n1. Customize Windows - 2000rs\n2. Customize Tires - 1500rs\n3. Custom Exhaust - 1300rs")
            choice2 = input("Enter your Choice: ")
            if choice2 == '1':
                self.order.createOrderCustomization(0)
            elif choice2 == '2':
                self.order.createOrderCustomization(1)
            elif choice2 == '3':
                self.order.createOrderCustomization(2)
        else:
            print("Wrong Choice. Please choose again\n")
            self.CarWorkShop()
        #self.order.printOrder()

    def MainMenu(self):
        t = time.asctime()
        print(t)
        choice = '1'
        while choice != '0':
            print('\n[*]===|WELCOME TO THE CAR SHOP|===[*]\n')
            print("\n[+]Main Menu\t\t\t\t\t\n[+]Please Select An Option\t\t\t\n\n1. Car Wash\t\t2. Car Workshop\t\t3. Reserve Appointment")
            choice = input("4. Random Orders.\t5. Delete Order.\n0. Print list of Orders\nEnter Your Choice:")
            if choice == '1' :
                self.CarWash()
            elif choice == '2' :
                self.CarWorkShop()
            elif choice == '3':
                self.Appointment()
            elif choice == '4':
                order = self.order.randOrder()
                self.sf.AddOrder(order)
            elif choice == '5':
                choice2 = input("Enter OrderNo. You want to Delete from queue: ")
                choice2 = int(choice2)
                self.sf.q.delOrder(choice2)
                self.sf.q.displayQueue()
            elif choice == '0':
                print("\n\t[.]List of Orders Being Processed:\n")
                self.RunningOrders()
            

    def RunningOrders(self):
        self.sf.DisplayOrders()
        while 1:
            if self.sf.q.front != None:
                self.sf.RunOrder()
            else:
                "\nNo More Orders"
                break

m = Menu()
m.MainMenu()
