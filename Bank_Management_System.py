import os
import mysql.connector as sc
import datetime as dt

#Function to check availibity of a roll no. 
def checkacc(acc):
    con=sc.connect(host='localhost',user='root',passwd='12345',database='Bank')
    cur=con.cursor()
    cur.execute("Select count(*) from sbi where acc_no={} ".format(acc))
    data=cur.fetchall()
    d=data[0][0]
    con.close()
    return d

   

#Function to open bank account
def open_acc():
    os.system('cls')
    ch='y'
    while ch=='y' or ch=='Y':
        con=sc.connect(host='localhost',database='bank',user='root',password='12345')  
        cur=con.cursor()
        try:
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input("    Enter Account No. \t\t\t: "))
            accno=int("100220"+str(accno))
            while checkacc(accno):
                print("    Entered Account No. already Exits ")
                accno=int(input("    Enter Account No. \t\t\t: "))
                accno=int("100220"+str(accno))
                
            name=input("    Enter Customer Name\t\t\t: ")
            nname=input("    Enter Nominee Name\t\t\t: ")
            dob=input("    Enter Date of birth (yyyy-mm-dd)\t: ")
            balance=float(input("    Enter Opening Balance\t\t: "))
            mob=input("    Enter Mobile no. \t\t\t: ")
            ifsc="SBIN0002020"
            df=dt.date.today()
            if df.month<10:
                opdate=str(df.year)+"-0"+str(df.month)+"-"+str(df.day)
            else:
                opdate=str(df.year)+"-"+str(df.month)+"-"+str(df.day)
            cur.execute("insert into sbi(acc_no,name,open_date,nominee,ifsc,dob,balance,mob) values({},'{}','{}','{}','{}','{}',{},'{}')".format(accno,name,opdate,nname,ifsc,dob,balance,mob))
            con.commit()
            print('************************************************************')
            print("\t\tAccount Opened Succesfully")
            print('************************************************************')
            ch=input("\tDo you want to open another account?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Account opening.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    
        



#Function to deposit money               
def deposit():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for deposit :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for deposit  :- '))
                accno=int("100220"+str(accno))
            amount=float(input('    Enter the Amount :- '))
            cur.execute("update sbi set balance=balance+{} where acc_no={}".format(amount,accno))
            con.commit()
            print('************************************************************')
            print("\t\tAmmount Succesfully Deposited")
            print('************************************************************')
            ch=input("\tDo you want to deposit more amount?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during depositing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
        

#Function to withdraw money               
def withdraw():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for Withdraw :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for Withdraw  :- '))
                accno=int("100220"+str(accno))
            amount=float(input('    Enter the Amount :- '))
            cur.execute("update sbi set balance=balance-{} where acc_no={}".format(amount,accno))
            con.commit()
            print('************************************************************')
            print("\t\tAmmount Succesfully withdrawn")
            print('************************************************************')
            ch=input("\tDo you want to withdraw more amount?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during withdraw.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")    
    

#Function to view balance  
def enquiry():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for Balance Enquiry :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for Balance Enquiry  :- '))
                accno=int("100220"+str(accno))
            cur.execute("Select name,balance from sbi where acc_no={}".format(accno))
            data=cur.fetchone()
            os.system('cls')
            print('************************************************************')
            print('*                     Balance Enquiry                      *')
            print('************************************************************')
            print('                 Account No.       : ',accno)
            print('                 Name              : ',data[0])
            print('                 Balance           : ',data[1])
            print('************************************************************')
            ch=input("\tDo you want to View another record?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during enquiry.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    


#Function to view customer details 
def view():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for Customer Details :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for Customer Details  :- '))
                accno=int("100220"+str(accno))
            cur.execute("Select * from sbi where acc_no={}".format(accno))
            data=cur.fetchone()
            os.system('cls')
            print('************************************************************')
            print('*                     Customer Details                     *')
            print('************************************************************')
            print('                 Account No.      : ',data[0])
            print('                 Name             : ',data[1])
            print('                 Acc. Active from : ',data[2])
            print('                 Nominee Name     : ',data[3])
            print('                 IFSC             : ',data[4])
            print('                 Date of Birth    : ',data[5])
            print('                 Balance          : ',data[6])
            print('                 Mobile           : ',data[7])
            print('************************************************************')
            ch=input("\tDo you want to View another record?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    
 

#Function to view list of customer 
def list_all():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            cur.execute("Select acc_no,name from sbi ")
            data=cur.fetchall()
            os.system('cls')
            print('************************************************************')
            print('*                     List of Customers                    *')
            print('************************************************************')
            print('\t\t   Acc No.\t  Name')
            print('------------------------------------------------------------')
            print('\t\t   ',end="")
            for row in data:
                for d in row:
                    print(d,end='\t  ')
                print()
                if not row==data[-1]:
                    print('\t\t   ',end="")
            print('************************************************************')
            ch=input()
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during Viewing.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")

#Function to modify account details
def modify():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for Updating Details :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for Updating Details  :- '))
                accno=int("100220"+str(accno))
            print('************************************************************')
            print('*                                                          *')
            print('*                 1. Name                                  *')
            print('*                 2. Nominee                               *')
            print('*                 3. Date of Birth                         *')
            print('*                 4. Mobile No.                            *')
            print('*                                                          *')
            print('************************************************************')
            opt=int(input('                  Enter Option :- '))
            print('************************************************************')
            if opt==1:
                name=input("\t\tEnter new Name  :  ")
                cur.execute("update sbi set name='{}' where acc_no={}".format(name,accno))
            elif opt==2:
                nname=input("\t\tEnter new Nominee Name  :  ")
                cur.execute("update sbi set nominee='{}' where acc_no={}".format(nname,accno))
            elif opt==3:
                dob=input("\tEnter new Date of Birth (yyyy-mm-dd)  :  ")
                cur.execute("update sbi set dob='{}' where acc_no={}".format(dob,accno))
            elif opt==4:
                mob=input("\t\tEnter new Mobile No.  :  ")
                cur.execute("update sbi set mob='{}' where acc_no={}".format(mob,accno))
     
            con.commit()
            print('************************************************************')
            print("\t\tDetails Succesfully Updated")
            print('************************************************************')
            ch=input("\tDo you want to Update another record?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during updating.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
        


#Function to close a account
def close_acc():
    ch='y'
    while ch=='y' or ch=='Y':
        try:
            con=sc.connect(host='localhost',user='root',password='12345',database='bank')
            cur=con.cursor()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            accno=int(input('    Enter the Account no. for closure :- '))
            accno=int("100220"+str(accno))
            while checkacc(accno)==0:
                print("    Entered Account no. Not Exits ")
                accno=int(input('    Enter correct Account no. for closure  :- '))
                accno=int("100220"+str(accno))
            cur.execute("delete from sbi where acc_no={}".format(accno))
            con.commit()
            os.system('cls')
            print('************************************************************')
            print('*                 Bank Management System                   *')
            print('************************************************************')
            print('*                                                          *')
            print('*             Accounted Deleted Successfully               *')
            print('*                                                          *')
            print('************************************************************')
            ch=input("\tDo you want to delete another account?(y/n)")
            con.close()
        except:
            print('************************************************************')
            print("\t\tError!!!... during deleting account.")
            print('************************************************************')
            ch=input("\tDo you want to try with another data?(y/n)")
    



#Main

ch=1

while ch!=0 :
    os.system('cls')
    print('************************************************************')
    print('*                 Bank Management System                   *')
    print('************************************************************')
    print('*                                                          *')
    print('*                 1. Open Bank Account                     *')
    print('*                 2. Deposit Amount                        *')
    print('*                 3. Withdraw Amount                       *')
    print('*                 4. Balance Enquiry                       *')
    print('*                 5. View Customer Details                 *')
    print('*                 6. View List of Customer                 *')
    print('*                 7. Modify Account Details                *')
    print('*                 8. Close an Account                      *')
    print('*                 0. Exit                                  *')
    print('*                                                          *')
    print('************************************************************')
    ch=int(input('                  Enter Option :- '))

    if ch==1:
        open_acc()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        enquiry()
    elif ch==5:
        view()
    elif ch==6:
        list_all()
    elif ch==7:
        modify()
    elif ch==8:
        close_acc()
