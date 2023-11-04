
#!C:/Users/HP/AppData/Local/Programs/Python/Python38
print()


import cgi
import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="Pls_mention your user name", password="Pls mention your pass")
mycursor=mydb.cursor()


start=input("<h1>First Time Login for this device Y/N\n:-></h1>")
if start in "Yy":
    mycursor.execute("CREATE DATABASE BOOK")
    mycursor.execute("USE  BOOK")
    mycursor.execute("Create Table Book_Record (Bookname varchar(20)PRIMARY KEY,Author varchar(20),Quantity int,Price int)")
    mycursor.execute("Create Table purchaselog (CUSTOMERNAME varchar(30),Bookname varchar(20),Quantity int)")
    mydb.commit()
else:
    mycursor.execute("USE  BOOK")
g=1
while g>0 :
        
        
        print("\n\n")
        def MainMenu():
            choice=input("\t\t\tWelcome to Heisenburg Book Store \n \n \n Please select operation \n 1. Administrator \n 2. Customer  \n :-> ")
            return(choice)
        mchoice=MainMenu()

        def view_administrator ():
            adinput= input('Please Select Operation : \n 1. New Book Record \n 2. Modify Book Record \n 3. Purchase Log \n 4. Search Book \n :-> ' )
            return(adinput)
        def viewcustomer():
            global name    
            name=input("Enter Your Name Please:")
            
            print(
        '''+-----------+--------------+----------+-------+----------+-------+----------+---
        \t\t     Hello''',name,'''\n  \t\t\tWelcome to our Book store                     
+-----------+--------------+----------+-------+----------+-------+----------+---''')

        def newbookadd():
            L=[]
            Bookname=input("Enter Book name :-> ")
            L.append(Bookname)
            Author=input("Enter Author Name :-> ")
            L.append(Author)
            Quantity=int(input("Enter Quantity :-> "))
            L.append(Quantity)
            Price=int(input('Enter Price : ->'))
            L.append(Price)
            Book=tuple(L)
            sql="""insert into Book_Record values(%s,%s,%s,%s)"""
            mycursor.execute(sql,Book)
            mydb.commit()
            choice = input("Do You want to add new record? (Y/N)")
            if choice in "Yy":
                    newbookadd()
            else:
                print("\n\n\t\t\tThanks Come back soon")
                intake=input("Would You like to go back to main menu \n :->")
                if intake in 'Yy':
                                  pass
                else:
                                  global g
                                  g=0
        def search():
            global bookname1    
            bookname1=input("Enter the name of the book :->\n")
            tuple1=(bookname1,)
            sql=("""SELECT * from Book_Record WHERE Bookname = (%s)""")
            mycursor.execute(sql,tuple1)
            results=mycursor.fetchall()
            sql5= """select count(*) from Book_Record where Bookname=%s"""
            mycursor.execute(sql5,tuple1)
            results1=mycursor.fetchall()
            for k in results1:

               if k[0]==0:
                  print("This book is not available\nWould you like to see the avilable books?\n Y or N")
                  ans=input()
                  if ans in "Yy" :
                      sqlhehe=("""SELECT BOOKNAME FROM BOOK_RECORD""")
                      mycursor.execute(sqlhehe)
                      resulthehe=mycursor.fetchall()
                      for l in resulthehe:
                          print (l)
                      search()    
                  else:
                      search()
               else:
    
                   if mchoice=='1':
                      for row in results:
                           print("\nBook Name= ", row[0], )
                           print("Author Name = ", row[1])
                           print("Quantity Available = ", row[2])
                           print("Price = ",row[3])
                      choice = input("Do You want to search again? (Y/N)")
                      if choice in'Yy':
                          search()


                      else:
                          print("\t\t\tThanks Come back soon\n\n ")
                          intake=input("Would You like to go back to main menu \n :->")
                          if intake in 'Yy':
                                  pass
                          else:
                                  global g
                                  g=0
                                  
                                  
                                
                            

                   else:
                      print("\t\t\tDetails of the book \n\n\n")
                      for row in results:
                          print("Book Name= ", row[0], )
                          print("Author Name = ", row[1])
                          print("Price = ",row[3])







            mydb.commit()                          
                 
        def purchasedetails():
                l = []
                l.append(name)
                l.append(bookname1)
                Quantity = int(input("Enter the Quantity of the book :->"))
                l.append(Quantity)
                booktup=(bookname1,)
                val1="""select Quantity from Book_Record where Bookname=%s"""
                mycursor.execute(val1,booktup)
                results=mycursor.fetchall()

                for i in results:
                   if i[0] >= Quantity:
                        sql="""insert into purchaselog values(%s,%s,%s)"""
                        detail=tuple(l)
                        print(detail)
                        mycursor.execute(sql,detail)
                        mydb.commit()
                        x=(i[0]-Quantity)
                        tuple3=(x,bookname1)
                        sql1=("Update Book_Record set Quantity=%s WHERE Bookname=%s ")
                        mycursor.execute(sql1,tuple3)
                        mydb.commit()

                        print('Your Order Has Been Placed :))')
                        intake=input("Would You like to go back to main menu \n :->")
                        if intake in 'Yy':
                                  pass
                        else:
                                  global g
                                  g=0
                                  



                   else:
                        print("\n\n\t\t!!!!!!!Quantity Not Available!!!!!!!\t\t")
                        print("\n\n\t\tAvailable Quantity =",i[0])
                        print("\n\nPlease Retype Your Details With New Quantity :)")
                        purchasedetails()
                mydb.commit()



       
        def purchasememo():
            choice=input("Do You want to purchase this book? (Y/N)")
            if choice in "Yy":
                purchasedetails()



            else:
                choice1 = input("Do You want to search again? (Y/N)")
                if choice1 in 'Yy':
                    search()
                    purchasememo()
                else :
                        print("\n\n\t\t\tThanks for visiting. Please visit us again\n\n")
                        intake=input("Would You like to go back to main menu \n :->")
                        if intake in 'Yy':
                                  pass
                        else:
                                  global g
                                  g=0



        def modification():
            
            ch=input("What Do you want to modify \n 1.Price \n 2. Quantity \n :->")
            if ch=='1':
                 bookval=input("Enter he name of the book to be modified :->")
                 val1=int(input("Enter the new Price"))
                 tuple1=(val1,bookval)
                 sql=("Update Book_Record set Price=%s WHERE Bookname=%s ")
                 mycursor.execute(sql,tuple1)
                 mydb.commit()
                 xyz=input("Do You Want to modify again (Y/N) \n:->")
                 if xyz in 'Yy':
                         modification()
                 else:
                        intake=input("Would You like to go back to main menu \n :->")
                        if intake in 'Yy':
                                  pass
                        else:
                                  global g
                                  g=0
                                  
                         


            else :
                 bookva2=input("Enter he name of the book to be modified :->")
                 val2=int(input("Enter the new QUANTITY:->"))
                 tuple2=(val2,bookva2)
                 sq2=("Update Book_Record set Quantity=%s WHERE Bookname=%s ")
                 mycursor.execute(sq2,tuple2)
                 mydb.commit()
                 xyzx=input("Do You Want to modify again (Y/N) \n:->")
                 if xyzx in 'Yy':
                         modification()
                           





        #Administration code
        if mchoice == "1":
            adchoice=view_administrator()


            if adchoice=="1" :
                newbookadd()

            if adchoice=="2":
                modification()

            if adchoice=="3":
                sql1="Select * From purchaselog"
                mycursor.execute(sql1)
                records = mycursor.fetchall()
                print("Customer name , Book Name , Quantity \n")
                for i in records:
                  print(i,end=",")
                  print('\n')
                intake=input("Would You like to go back to main menu \n :->")
                if intake in 'Yy':
                                  pass
                else:
                                  
                                  g=0
                
                
                mydb.commit()
            if adchoice=="4":
                search()
        # Customer code
        else :
            viewcustomer()

            search()
            purchasememo()

