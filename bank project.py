import pymysql as sql

conn=sql.connect(host="localhost",user="root",password="12345",database="bank_demo")
cur=conn.cursor()




def New_Account():
    accno = int(input("Enter Account Number : "))
    name = input("Enter Name : ")
    password = input("Enter Password : ")
    city = input("Enter City Name : ")
    amount = int(input("Enter Amount : "))

    q = "insert into bank(acc_no,name,password,city,amount) values('%d','%s','%s','%s','%d')"%(accno,name,password,city,amount)
    r =cur.execute(q)
    if(r>0):
        print("Account Open Successfully : ")
    else:
        print("Account Not Open : ")
    conn.commit()



def Balance():
    accno =int(input("Enter Account Number : "))
    q = "select amount from bank where acc_no='%d'"%(accno)
    cur.execute(q)

    for data in cur.fetchall():
        print(data[0])
    conn.commit()

def main():
    print("Welcome In Anudip Banking Application")
    while True:
        opt = int(input("Choose Options...\n1. NEW ACCOUNT\n2. Balance ENQUIRY\n3. Exit\n"))

        if opt is 1:
            New_Account()
        elif opt is 2:
            Balance ()
        
        else:
            print("Bye ....")
            break;
    conn.close()


main()
