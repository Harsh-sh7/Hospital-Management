import datetime
import random as rd
import mysql.connector as sqltor

# Connecting to MySQL database
con = sqltor.connect(host="localhost", user="root", password="password")
cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS CHMS")
cur.execute("USE CHMS")

# Creating the table for patient details
cur.execute("CREATE TABLE IF NOT EXISTS appt"
            "(idno CHAR(12) PRIMARY KEY,"
            "name CHAR(20),"
            "age INT(10),"
            "gender CHAR(1),"
            "phone CHAR(10),"
            "bg CHAR(3))")

# Inspirational Quotes
tht1 = ''' BEAUTIFUL THINGS HAPPEN WHEN YOU DISTANCE YOURSELF FROM NEGATIVITY '''
tht2 = ''' DREAMS ARE NOT WHAT YOU SEE WHEN YOU SLEEP, DREAMS ARE THOSE WHICH DON'T LET YOU SLEEP '''
tht3 = ''' YOU ONLY LIVE ONCE. BUT IF YOU DO IT RIGHT, ONCE IS ENOUGH '''
tht4 = ''' THE EXPERT IN ANYTHING WAS ONCE A BEGINNER '''
tht5 = ''' NOT ALL STORMS COME TO DISRUPT YOUR LIFE, SOME COME TO CLEAR YOUR PATH '''
tht6 = ''' LISTEN TO EVERYONE AND LEARN FROM EVERYONE, BECAUSE NOBODY KNOWS EVERYTHING BUT EVERYONE KNOWS SOMETHING '''
tht7 = ''' ONE KIND WORD CAN CHANGE SOMEONE'S ENTIRE DAY '''
tht8 = ''' GOOD MANNERS AND KINDNESS ARE ALWAYS IN FASHION '''

# Inspirational Quote List
th = (tht1, tht2, tht3, tht4, tht5, tht6, tht7, tht8)

# Printing greeting message
print("""  
  
               ___       ___   ___            ___     _____ ___       ___  _____ _____
     |      | |    |    |   | |   | |\    /| |          |  |   |     |   |   |     |   |   |
     |  /\  | |__  |    |   | |   | | \  / | |__        |  |   |     |       |     |   |___|
     | /  \ | |    |    |   | |   | |  \/  | |          |  |   |     |       |     |       |
     |/    \| |___ |___ |___| |___| |      | |___       |  |___|     |___| __|__   |    ___|
   _________________________________________________  __________    _________________________
                         
                            ___   ___   ___  _____  _____  ____    
                     |   | |   | |     |   |   |      |   |    |  |
                     |___| |   | |___  |___|   |      |   |____|  |
                     |   | |   |     | |       |      |   |    |  |
                     |   | |___|  ___| |     __|__    |   |    |  |____
                    ____________________________________________________                
          """)

d = datetime.date.today()
t = datetime.datetime.now()
print(" ")
print(" ")
print("        DATE:-", d.strftime("%A, %d %B %Y"))
print(" ")
print("        TIME:-", t.strftime("%H:%M:%S"))
print("")
print('')
choice = rd.choice(th)
print(choice)

while True:
    print(""" 
      
    
        
         _____________                  _____________                  ____________
        |             |                |             |                |            |
        | 1. PATIENT  |                | 2. DOCTOR   |                |  3. EXIT   |
        |_____________|                |_____________|                |____________|
        
         
        
        """)
    e = input("||  ENTER YOUR CHOICE  ||\n>>")
    
    if e == "1":
        def dat():
            while True:
                idn = input("Adhaar no.:")
                if len(idn) == 12:
                    break
                else:
                    print(" ~!~!~!~~ 12 digits required ~~!~!~!~")
               
            name = input("Patient name:")
            while True:
                age = int(input("Age:"))
                if type(age) != int:
                    print("~!~!~!~~ digits required ~~!~!~!~")
                else:
                    break

        
            while True:
                gen = input("Gender M/F:")
                if gen == ("M") or gen == ("F"):
                    break
                else:
                    print("~!~!~!~~ M\F only ~~!~!~!~")
        
            while True:
                ph = input("Phone no.:")
                if len(ph) == 10:
                    break
                else:
                    print("~!~!~!~~10 digits required~~!~!~!~")
            while True:
                bg = input("""Blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):-""")
                if bg == ("A+") or bg == ("B+") or bg == ("O+") or bg == ("AB+") or bg == ("A-") or bg == ("B-") or bg == ("O-") or bg == ("AB-"):
                    break
                else:
                    print("~!~!~!~~ Enter valid value ~~!~!~!~")
            cur.execute("INSERT INTO appt(idno, name, age, gender, phone, bg) VALUES(%s, %s, %s, %s, %s, %s)", (idn, name, age, gen, ph, bg,))
            con.commit()
            print(" ")
            print("""   
               ________________________        
              |                        |
              |YOU HAVE BEEN REGISTERED| 
              |________________________|     
                 """)
              
            print("""
             _____________________________ 
            |                             |
            |Your details are as follows:-|
            |_____________________________| 
            
            """)
            cur.execute("SELECT * FROM appt WHERE idno=(%s);", (idn,))
            d = cur.fetchall()
            for i in d:
                print("""     Adhaar no.:-""", i[0])
                print('''     Name:-''', i[1])
                print('''     Age:-''', i[2])
                print('''     Gender:-''', i[3])
                print('''     Phone:-''', i[4])
                print('''     Bloodgroup:-''', i[5])
            return("")

        def name():
            adr = int(input('ENTER YOUR ADHAAR NO:'))
            cur.execute('SELECT * FROM appt WHERE idno=(%s)', (adr,))
            dat = cur.fetchall()
            if len(dat) != 1:
                print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            else:
                print('')
                print('''
                ------------------------    
                | YOUR OLD DETAILS ARE |
                ------------------------
                ''')
                for i in dat:
                    print("Adhaar no.:-", i[0])
                    print('Name:-', i[1])
                    print('Age:-', i[2])
                    print('Gender:-', i[3])
                    print('Phone:-', i[4])
                    print('Bloodgroup:-', i[5])
                n = input('ENTER NEW NAME:-')
                cur.execute('UPDATE appt SET name=(%s) WHERE idno=(%s);', (n, adr,))
                con.commit()
                cur.execute('SELECT * FROM appt WHERE idno=(%s)', (adr,))
                dat = cur.fetchall()
                for row in dat:
                    print('')
                    print('''
               ------------------------      
               | YOUR NEW DETAILS ARE  |
               ------------------------      
                    ''')
                    print("Adhaar no.:-", row[0])
                    print('Name:-', row[1])
                    print('Age:-', row[2])
                    print('Gender:-', row[3])
                    print('Phone:-', row[4])
                    print('Bloodgroup:-', row[5])
                con.commit()
            return("")

        def age():
            adr = int(input('ENTER YOUR ADHAAR NO:'))
            cur.execute('SELECT * FROM appt WHERE idno=(%s)', (adr,))
            dat = cur.fetchall()
            if len(dat) != 1:
                print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            else:
                print('')
                print('''
                ------------------------    
                | YOUR OLD DETAILS ARE |
                ------------------------
                ''')
                for i in dat:
                    print("Adhaar no.:-", i[0])
                    print('Name:-', i[1])
                    print('Age:-', i[2])
                    print('Gender:-', i[3])
                    print('Phone:-', i[4])
                    print('Bloodgroup:-', i[5])
                n = input('ENTER NEW AGE:-')
                cur.execute('UPDATE appt SET age=(%s) WHERE idno=(%s);', (n, adr,))
                con.commit()
                cur.execute('SELECT * FROM appt WHERE idno=(%s)', (adr,))
                dat = cur.fetchall()
                for row in dat:
                    print('')
                    print('''
               ------------------------      
               | YOUR NEW DETAILS ARE  |
               ------------------------      
                    ''')
                    print("Adhaar no.:-", row[0])
                    print('Name:-', row[1])
                    print('Age:-', row[2])
                    print('Gender:-', row[3])
                    print('Phone:-', row[4])
                    print('Bloodgroup:-', row[5])
                con.commit()
            return("")

        # (Similarly for gender, phone, bloodgroup update functions)

    elif e == "2":
        # (Doctor functionality omitted for brevity)
        pass

    elif e == "3":
        print("Exiting...")
        break

con.close()
