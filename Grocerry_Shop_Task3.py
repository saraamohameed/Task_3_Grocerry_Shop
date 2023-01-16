Shop_Items  = {  "id. product": 'Cost For Kg',
				 "1.  banana": [5],
                 "2.  apple":  [20],
				 "3.  orange": [4],
				 "4.  kiwi":   [10]}

Bought_Items = {"id. product": 'Cost',}

#  Function For Show Items In The Shop		
def Show_Shop_Items():			
		print(" #" * 30)
		for Item, value in Shop_Items.items():
			print(f"{Item} ==>   {value}")
		print(" #" * 30)

def Show_Bought_Items():			
		print(" #" * 30)
		for Item, value in Bought_Items.items():
			print(f"{Item} ==>   {value}")
		print(" #" * 30)

#  Function For Add Items In The Shop			
def Add_Item():	
			
	print("#" * 30)
	Id_New_Item = int (input("Enter The Id For The New Item you want to Add: "))
	New_Item = input("Enter the New Item you want to Add: ")	
	
	print(f"'{Id_New_Item}.  {New_Item}'")
	
	if (f'{Id_New_Item}.  {New_Item}') in Shop_Items:
		print(" Product Already in The Shop Items ")
	else :
		Cost_New_Item = int(input("Enter The Cost For The New Item you want to Add: "))
		Shop_Items.update({f"{Id_New_Item}.  {New_Item}": [Cost_New_Item]})
		Show_Shop_Items()


#  Function For Change cost  For Items In The Shop				
def Change_cost():			
		print("#" * 30)
		Item_Id_For_Cange_Cost= int(input("Enter The Id For Product You Want To Change It's Cost:"))
		Item_Name_For_Cange_Cost= input("Enter The Name For Product You Want To Change It's Cost:")
		
		print(Shop_Items[(f'{Item_Id_For_Cange_Cost}.  {Item_Name_For_Cange_Cost}')])
		
		if (f'{Item_Id_For_Cange_Cost}.  {Item_Name_For_Cange_Cost}') in Shop_Items:
			print("Enter The New Cost You Want TO Change To :")
			New_Cost=int(input())
			Shop_Items[(f'{Item_Id_For_Cange_Cost}.  {Item_Name_For_Cange_Cost}')]=[New_Cost]
			print(Shop_Items[(f'{Item_Id_For_Cange_Cost}.  {Item_Name_For_Cange_Cost}')])
			Show_Shop_Items()
			
		else :
			print(" Product Not Found in The Shop Items ")
		

#  Function For Delete Item  From Items In The Shop	
def Delete_Item():	
		print("#" * 30)	
		Item_Id_To_Delet= int(input("Enter The Id For Product You Want To Delet:"))
		Item_Name_To_Delet= input("Enter The Name For Product You Want To Delet:")
		
		if (f'{Item_Id_To_Delet}.  {Item_Name_To_Delet}') in Shop_Items:
		
			del Shop_Items[(f'{Item_Id_To_Delet}.  {Item_Name_To_Delet}')]
			Show_Shop_Items()
		
		else :
			print(" Product Not Found in The Shop Items ")


			
#  Function For Buy products From Items In The Shop	
def Buy_Items():
    
			print("#" * 30)
			print("Our Items")
			Show_Shop_Items()
			Number_items = int(input("Please Enter The Number Of The Item You Need:"))
			while Number_items!=0 :
				Buy_Item_Id = int(input("Please Enter The ID Of The Item You Need:"))
				Buy_Item = input("Please Choose The Item You Need:")
				if (f'{Buy_Item_Id}.  {Buy_Item}') in Shop_Items:
					print("Your Choose Available ")
					Quantity = int(input("Please Enter The Quantity You Need in Kg :"))
					Bought_Items.update({f"{Buy_Item_Id}.  {Buy_Item}": Quantity*Shop_Items[(f'{Buy_Item_Id}.  {Buy_Item}')][0]})
					Show_Bought_Items()	
					Number_items--
				else :
					print("Your Choose Unavailable ")
	
				
		
		
		
#  Function For Print Bill 	
def Print_Bill():				
		print("#" * 30)
		print("****  Bill Summary  ***** ")
		Show_Bought_Items()
		for Item, value in Bought_Items.items():
			
		print (f"The Total Cost:{value}")
		print("***********Thank You********")
		print("Hope to see you back soon!")
		print("#" * 30)

		
		
		
# # IF You Select Mode For  owner		
# Owner password =176
#  If you are ITI Shop Owner You Can:
# - Add new products - Show Products - Add Cost  - Change cost	
	
def ITI_OWNER():
	owner_name = input(" Please Enter Your name : ")
	print(f"Hello {owner_name.strip().capitalize()}")
	password = int(input(" Enter Your password : "))
	Try = 1
	while Try<3:
			if password == 176:
				print("	\n ## Owner Operation ## \n ")	
				Owner_Operation= int(input("1.press 1 for show products\n2.press 2 for Add product\n3.press 3 for change cost\n4.press 4 for delete product\n0.press 0 for Exit\n "))
				
				if Owner_Operation== 1:
					print(" \n ## Products in Grocery Shop ##\n ")
					Show_Shop_Items()
						
				elif Owner_Operation== 2:
					print(" \n ## Add Product ##\n ")
					Add_Item()
						
				elif Owner_Operation== 3:
					print(" \n ## Change cost ##\n ")
					Change_cost()

				elif Owner_Operation== 4:
					print(" \n ##  Delete product ##\n ")
					Delete_Item()
						
				elif Owner_Operation== 0:
					print(" Exit operation")
					exit()
				
			if password != 176:
				print(" Wrong Password try again ")
				password = int(input(" Enter Your password : "))
				Try+=1
						
	
# # IF You Select Mode For Customer 
#You Can:  show products- Buy products - print bill
def Customer():			
			
			Customer_name = input("Please Enter your Name :")
			print(f"Hello {Customer_name.strip().capitalize()}")
			print("	\n Customer Operation \n ")
			Customer_Operation= int(input("1.press 1 for show products\n2.press 2 for Buy products\n3.press 3 for Print Bill\n0.press 0 for Exit\n "))
			if Customer_Operation== 1:
				print("   Products in Grocery Shop\n ")
				Show_Shop_Items()
							
			elif Customer_Operation== 2:
				print(" Buy products ")
				Buy_Items()
							
			elif Customer_Operation== 3:
				print(" Print Bill ")
				Print_Bill()
							
			elif Customer_Operation== 0:
				print(" Exit operation")
				exit()


         # #Main Program 
	# # Select Mode For  owner press 1 , for customer press two , to exist press 0 
while True:
	try:
		ch = int(input("1.press 1 for Owner Mode\n2.press 2 for User Mode\n0.press 0 for Exit\n "))
	except ValueError:
		print("\nERROR: Choose only digits from the given option")
		continue
	else:
		if ch == 1:
			#owner mode
			print("\n You Now in owner mode ")			
			ITI_OWNER()
		elif ch == 2:
			# customer mode
			print("\n You Now in customer mode ")	
			Customer()
			# Exit mode
		elif ch == 0:
			print("   Exit operation")
			exit()
			
			