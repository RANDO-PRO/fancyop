#-----------------------------------------------------------IMPORTS-------------------------------------------------------------
import mysql.connector
import datetime
import time

#-------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------variables----------------------------------------------------------
all=0
c = ""
m = ""
x = 0
datu = ""
baitB = "back"
baitA = "again"
huff = ['1', '2', '3', '4', '5']

#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------SPECIAL--------------------------------------------------------

def spac():
    print()
    print()
    print()


def spac2():
    print()
    print()

def spac3():
    print()
    
def linecr(mo,rep=1,spa=2,dis=0,cdis="",gap=0,lineremov=0):
    #mo is the character used to make the line 
    #rep is the amount of times you want to repeat the line
    #spa is for space.Basically the default value is 2 so it will print 2 empty lines.Value 1 will print 1 emty line and Value >= 3 will print 3 empty lines.value 0 will print no empty lines 
    #dis is used for displaying text that has been used as options in the main menu.It uses the value of int(x) to figure out the text to be displayed
    #cdis is a custom display option that will display messages
    #gap is to see if you want the custom display to be displayed in the center or near the start.It has been disabled by default
    #dis won't work if cdis has been used.So,default value should be 2 for dis.
    #lineremov is just there if you don't want a line to be printed after the cdis or dis
    
    namingsa=['REGISTERING',"CUSTOMER DETAILS","SEARCH REGESTRATION NUMBER(R_CODE)","MODIFY DATA","SALE","INF FROM SORTED TABLE","HELP INFO","MYSQL CONNECTION"]
    k=rep+dis
    if cdis=="":
        ja=namingsa[(dis-1)]
    else:
        ja=cdis
    if dis!=0 or cdis=="":
        for hoho in range(k):
            if hoho==0 or (hoho==(k-1) and lineremov==0):
                 print(mo*98)
            elif(hoho==dis and cdis==""):
                 print(" "*47+ja)
            elif(cdis!="" and hoho==dis):
                if gap==0:
                     print(ja)
                else:
                    print(" "*47+ja)
    else:           
        for hoho in range(k):
            print(mo*98)
    
    if spa==0:
        pass
    elif spa==1:
        spac3()
    
    elif spa==2:
        spac2()
    elif(spa>=3):
          spac()

def delinf():
    dela = open("SQLINF.txt", "w")
    dela.write("")
    dela.close()


def reader():
  while(True):
    try:
      rara = []
      rop = open("SQLINF.txt", "r")

      for kami in rop:
         kami = kami.strip()
         rara.append(kami)

      rop.close()

      return rara
      
      break
    except Exception as exce:
      if "[Errno 2] No such file or directory: 'SQLINF.txt'"==str(exce):
                          hope = open("SQLINF.txt", "w")
                          hope.write("")
                          hope.close()   
                        
        
      else:
         spac2() 
         print("UNEXPECTED ERROR :",exce)
         spac2()
         endin(1)
         break
         x="bye"


def filinf(L):

   while(True):
       abyss = 0
       try:
          answer = reader()
       except Exception as re:

              if "[Errno 2] No such file or directory: 'SQLINF.txt'" == str(re):
                                   abyss = 1

              else:
                  print("UNEXPECTED ERROR :", re)
                  break
       if abyss == 1:
              hope = open("SQLINF.txt", "w")
              for i in L:

                  
                  hope.write(i+"\n")

              hope.close()
       else:
            
            if answer==[]:
                hope = open("SQLINF.txt", "w")
                for i in L:
                       hope.write(i+"\n")

                hope.close()
            else:
                 break    
           
def sqla():
     while(True): 
      use=input("ENTER USER NAME[DEFAULT-MYSQL-USER:'ROOT'] :")
      spac2()
      if use=="":
            print("FIELD EMPTY!!!!!!!!!!!")
            spac2()
            continue
      else:
          break
     while True: 
        pas=input("ENTER PASSWORD[DEFAULT MYSQL-PSWD:''] :")
        spac2()
        if  pas=="":
            
           print("EMPTY FIELD!!!!!!!!!!!!!!!!!!")
           spac2()
           continue
        else:
            break            
     return [use,pas,"1"]
def mysqlcom():
     
      while(True):
         heki = 0
         
         if reader()==[]:
             infoow = sqla()
         else:
             infoow=reader()
         try:
            global m
            global c
            m = mysql.connector.connect(
                user=infoow[0], password=infoow[1], auth_plugin='mysql_native_password')
            c = m.cursor()
            while(True):
                try:
                     filinf(infoow)
                     c.execute("create database vdata")
                     
                     break
               
                except Exception as e:
                            
                            if "1007 (HY000): Can't create database 'vdata'; database exists"==str(e):
                                                 heki=1 
                                                 break
                                                 
                            else:
                                  spac2()
                                  print("UNEXPECTED ERROR-",e)
                                  spac2()
                                  heki=2

            if heki==0:
                    c.execute("use vdata")
                    try:
                      
                       c.execute("create table registry(R_CODE char(15) primary key,NAME char(50) not null,STATE char(50) not null,D_O_R date not null,I_D char(50) not null,SERIAL_N_O int not null,SLOT int not null);")
                      
                       spac2()
                       print("SUCCESSFULLY CREATED DATABASE!!!!!!!!!!")
                       time.sleep(0.34)
                       spac2()
                       print("USING DATABASE VDATA............")
                       time.sleep(0.36)
                       spac2()
                       
                       print("CREATING TABLE REGISTRY..........")
                       time.sleep(0.38)
                       spac2()
                       print("SUCCESSFULLY CREATED TABLE REGISTRY!!!!!!!!!!!")
                       time.sleep(0.40)
                       spac2()
                       print("USING TABLE REGISTRY")
                       spac2()
                       print("STARTING THE PROGRAM............")
                       spac()
                       break
                    except Exception as ra:
                             print("ERROR :",ra)
                             spac2()
                             break
            elif heki==2:
                all=1                 
            
            else:
                   try:   
                       c.execute("use "+"vdata")
                       time.sleep(0.32)
                       spac2()
                       print("FOUND DATABASE VDATA!!!!!!!!!")
                       time.sleep(0.34)
                       spac2()
                       print("USING DATABASE VDATA................")
                       time.sleep(0.36)
                       spac2()
                       print("USING TABLE REGISTRY...........")
                       time.sleep(0.38)
                       spac2()
                       print("STARTING THE PROGRAM............")
                       spac()
                       break
                 
                   except Exception as ka:
                         spac2()
                         print("ERROR :",ka)
                         spac2()
                         endin(1)
                         break  
         except Exception as erroq:
                  if "module 'mysql.connector' has no attribute 'connect'"==str(erroq):
                      
                      print("MYSQL NOT FOUND ON THE PC!!!!!DOWNLOAD IT FROM--'https://dev.mysql.com/downloads/installer/'")
                      spac2()
                  elif "1045 (28000): Access denied for user '"+infoow[0]+"'@'localhost' (using password: YES)" == str(erroq):
                        print("THE PASSWORD FOR THE USERNAME "+infoow[0]+" IS INCORRECT!!!!!!!PLEASE ENTER AGAIN")
                        spac2()
                        continue
                  
                  else:
                        print("UNEXPECTED ERROR :",str(erroq).upper())
                        spac2()
         break
#================================================================================================================================


#----------------------------------------------------------WELCOME---------------------------------------------------------------
print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
print("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
time.sleep(0.56)
spac2()
linecr("-")

#-------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------CONNECTING TO mysQL-----------------------------------------------------------------
linecr("=",2,2,8)
while(True):
    mysqlcom()
    if(all==1):
        print("unecpected")
        continue
    else:
        break
#rcode-name-state-dor-id-slot-serial
#_______________________________________________________FUNCTION DEFINE______________________________________________________________





def prip(listt):

    a = len(listt)
    dig = 0
    while(a > 0):
         a = a//10
         dig += 1
    
    #stop
    time.sleep(0.666)
    #box
    
    print("", ("_"*13), "_"*13)
    print("|__T.ENTERIES_|"+"____"+str(len(listt))+"_"*(9-dig)+"|")

    #table
    print("", "_"*163)

    print("|_R_CODE___________|_NAME", "_"*45+"_|_STATE", "_"*24 +
          "|_D_O_R________|_I_D________________|_SERIAL_N_O __|_SLOT___|")

    for i in range(len(listt)):

        print("|", listt[i][0], " "*(15-len(listt[i][0])), "|", listt[i][1], " "*(49-len(listt[i][1])), "|", listt[i][2], " "*(28-len(listt[i][2])), "|", listt[i]
              [3], "  |", listt[i][4], " "*(17-len(listt[i][4])), "|", listt[i][5], " "*(11-len(str(listt[i][5]))), "|", listt[i][6], " "*(5-len(str(listt[i][6]))), "|")
        if i == (len(listt)-1):
            print("╹"+"─"*163+"╹")
    spac2()


def infpri(L=[], rp=''):  # r_code,NAME,STATE,D_O_R,I_D,SERIAL_N_O,SLOT
        start = 'SELECT * FROM registry WHERE '
        if rp == 'AND' or rp == 'and':
            rp = ' AND '
        elif rp == 'OR' or rp == 'or':
             rp = ' OR '

        hop = ' LIKE '

        K = ['R_CODE', 'NAME', 'STATE', 'D_O_R', 'I_D', 'SERIAL_N_O', 'SLOT']
        ho = []
        a = 0
        for i in L:
            if(i != ''):
                 ho.append([i, a])
            a += 1
        a = ho

        for he in ho:

                start += K[he[1]]+hop+"'"
                start += he[0]+"'"
                if(he != ho[-1]):
                     start += rp
                else:
                     start += ';'

        c.execute(start)

        pop = c.fetchall()

        return pop


def orderby(something,descending="",pa=0):
    if descending=="":
          c.execute("SELECT * FROM REGISTRY ORDER BY "+something+";")
    else:
        c.execute("SELECT * FROM REGISTRY ORDER BY "+something+" DESC;")
    odata = c.fetchall()
    if(odata ==[]):
        print("NO ENTRY EXISTS!!!!!!!!!!!!!")
        spac2()
    if pa==0:
        prip(odata)
    else:
        return odata

def fnamee():
    fname = input("ENTER FIRST NAME:")
    spac()
    if(fname =="back"):
        return baitB
    elif(fname =="again"):
        return baitA
    elif(fname.isalpha() ==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        spac()
        raise ValueError
    else:

        return fname


def snamee():
    sname = input("ENTER YOUR FAMILY NAME:")
    spac()
    if(sname =="back"):
        return baitB
    elif(sname =="again"):
        return baitA
    elif(sname.isalpha() ==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        spac()
        raise ValueError
    else:
        return sname


def statee():
    state = input("ENTER THE STATE:")
    spac()
    if(state =="back"):
        return baitB
    elif(state =="again"):
        return baitA
    elif(state.isalpha() ==False):
        print("STATE NAME SHOULD NOT BE NUMERIC!!!!!!!")
        spac()
        raise ValueError
    else:
        return state


def datte():
    libra = ['0','1','2','3','4','5','6','7','8','9']
    lib = [5,8]
    while True:
      global datu
      datu = input("ENTER THE DATE OF REGISTRATION[DATE FORMAT- YYYY-MM-DD] :")
      spac()
      datu = datu.strip()

      if(len(datu) ==10):

          hey = 0
          k = 1
          for i in datu:
              if i =='-' and k in lib:
                  pass

              elif i in libra:
                  pass

              else:
                  hey = 1
                  print("ENTER NUMBERS AND CORRECT FORMAT ONLY!!!!!!!!")
                  spac()
                  break
              k += 1
          if hey ==0:
              try:
                 dattte = datetime.date(int(datu[0:4]),int(datu[5:7]),int(datu[8:10]))

                 if dattte >datetime.date.today():
                     print(
                         "THIS DATE DOESN'T EXIST YET! |PLEASE ENTER A VALID DATE!!!")
                     spac()

                 elif dattte <datetime.date(1900,12,31):
                     print("PLEASE ENTER A VALID DATE!!!!!")
                     spac()

                 else:

                     return dattte

                     break

              except Exception as er:

                   if str(er) =="month must be in 1..12":
                                   print("ERROR:MONTH MUST BE BETWEEN 1-12|[IT CAN'T BE-", datu[5:7],"]|!!!!")
                                   spac()

                   elif str(er) =="day is out of range for month":
                                  print("ERROR:THE DAY IS OUT OF RANGE FOR MONTH!!!!!")
                                  spac()
              except KeyboardInterrupt:
                   print("UNEXPECTED ERROR")
                   spac()
                   continue


      else:
          print("CORRECT FORMAT ONLY!!!!!!!!")
          spac()


def slote():
    slot = input("ENTER SLOT NUMBER:")
    slot = slot.lower()
    spac()
    if(slot =="back"):
        return baitB
    elif(slot =="again"):
        return baitA
    elif(slot.isnumeric() ==False):
            print("SLOT NUMBER CAN ONLY BE NUMERIC!!!!!!")
            spac()
            raise AssertionError

    elif(int(slot) <1):
            print("SLOT NUMBER CAN'T BE LESS THAN 0!!!!!")
            spac()
            raise AssertionError
    elif(int(slot) >999):
            print("SLOT NUMBER CAN'T BE MORE THAN 999!!!!!")
            spac()
            raise AssertionError
    else:
        length = len(slot)
        while(length <3):

            slot = "0"+slot
            length = len(slot)

        return slot


def seriale():
    serial = input("ENTER SERIAL NUMBER:")
    spac()
    if(serial =="back"):
        return baitB
    elif(serial =="again"):
        return baitA
    elif(serial.isnumeric() ==False):
        print("SERIAL NUMBER CAN ONLY BE NUMERIC!!!!!!!")
        spac()
        raise AssertionError
    elif(int(serial) >10000):
        print("SERIAL NUMBER CAN'T BE MORE THAN 10000!!!!!!!")
        spac()
        raise AssertionError
    else:
        size = len(serial)
        if(size !=4):
            while(size !=4):
                serial = "0"+serial
                size = len(serial)
        return serial


def monoga(choice):
    pass
    va=["NAME","STATE","D_O_R","SERIAL_N_O","SLOT"]
    
    if len(choice)==1:
        so=va[(int(choice)-1)]
        orderby(so)
    else:
        so=va[(int(choice[0])-1)]
        orderby(so,"DESC")

def endin(a=0):
   if a==0:
      print("QUITTING TO MAIN MENU.........")
      time.sleep(1.6)
      spac2()       
      
   else:
       print("QUITTING THE PROGRAM...........")
       time.sleep(1.72)
       spac()
       linecr("-")
       
def nameing():
    ok='again'
    while(ok =="again"):
    
                try:
                    fname = fnamee()

                    ok = input("press any key ")

                    if(fname =="back"):
                        break

                except AssertionError:
                    continue

                except ValueError:
                    continue

                if(fname =="back"):
                        spac()
                        break

                else:
                     fname = fname.upper()
                     spac2()
            #sname

    ok = "again"
    while(ok =="again"):

                try:
                    sname = snamee()

                    ok = input("press any key ")

                    if(sname =="back"):
                        break

                except AssertionError:
                    continue

                except ValueError:
                    continue


                if(sname =="back"):
                     spac()
                     break

                else:
                    sname = sname.upper()
                    namee = fname+" "+sname
                    spac2()

                if len(namee) >45:
                      namee = namee[0:46]
                 
                return namee 
def stating():
      ok = "again"

      while(ok =="again"):
               try:
                    state = statee()

                    if(state =="back"):
                        break

                    ok = input("press any key to continue ")
               except ValueError:
                     continue


               if(state =="back"): 
                    spac()
                    break
               else:
                   stateee = state.upper()
                   spac2()

               if len(stateee) >22:
                      stateee = stateee[0:23]
               return stateee

def datetester(d='3',m='2',y='2005',vo=''):
      try:
        mday=datetime.date(y,m,d)
        if mday>datetime.date.today():
            err="THE "+vo+" DOESN'T EXIST YET!!!!!!!!!!"
            return err
        elif mday<datetime.date(1900,12,31):
                     err="PLEASE ENTER A VALID DATE!!!!!"
                     return err
        else:
            err=""
            return err
      except Exception as E:
                   if str(E) =="month must be in 1..12":
                                   err="ERROR:MONTH MUST BE BETWEEN 1-12|!!!!!!!!"
                                   return err
                   
                   
      except KeyboardInterrupt:
             err="UNEXPECTED ERROR"
             return err      
                   
def passcheck():
   h=0
   while(True):
        
    porch=input("ENTER PASSWORD :")
    k=reader()
    spac2()
    if porch==k[1]:
        spac2()
        return "y"
        break
    else:
    
        print("INCORRECT PASSWORD!!!!!!!!!!!ENTER AGAIN")
        spac2()
        
        h+=1
        if h>3:
            print("YOU HAVE ENTERED THE WRONG PASSWORD TOO MANY TIMES!!!!!!!!TRY AGAIN LATER")
            spac2()
            return "q"
            break

#_____________________________________________________EXECUTION_of-data_________________________________________________________________



while(x !="bye"):
   try:   
    linecr("-",2,0,8,"MENU",1,1)
    

    print("● 1 REGISTER VEHICLE \n\n● 2 GET CUSTOMER DETAILS(REGISTRATION NO. REQUIRED) \n\n● 3 CHECK REGISTRATION NO.(ID DETAILS REQUIRED) \n\n● 4 MODIFY \n\n● 5 SALE OF CARS \n\n● 6 SORT \n\n● 7 HELP \n"+("_"*98)+"\n")
    x=input("CHOOSE[ENTER 'BYE' TO EXIT] :")
    time.sleep(0.44)
    spac2()
    
    
    x=x.upper()
    if(x =="1"):
        save = ""
        linecr("=",2,2,int(x))    
        while(save !="back"):
            
            ok='again'
            
            print("IMPORTANT COMMANDS")

            linecr("-",2,2,int(x),"●ENTER 'back' AT ANY POINT TO QUIT TO MAIN MENU\n\n●ENTER 'again' AT ANY POINT TO ENTER AGAIN")

            #name

            name=nameing()
            
            #state

            state=stating()
            #slot

            ok = "again"

            while(ok =="again"):

                try:

                    slot = slote()

                    slot2 = int(slot)
                    spac3()
                    ok = input("press any key to continue")
                    
                except ValueError:

                    print("ERROR:AVOID USE OF SPECIAL CHARACTER!!!!!!!!")
                    spac()
                    continue

                except AssertionError:

                    continue


            spac2()
            #serial

            ok = "again"

            while(ok =="again"):

                try:

                    serial = seriale()


                    ok = input("press any key to continue ")

                except ValueError:

                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")

                    continue

                except AssertionError:

                    continue

            
            else:
                spac2()

            #date

            ok = "again"

            while(ok =="again"):



                    date = datte()

                    ok = input("press any key to continue ")
                    time.sleep(0.57)
                    spac2()
            #id

            ok = "again"

            while(ok =="again"):

                try:

                    ID = input("ENTER ID NUMBER(ADHAAR CARD NO./VOTER ID CARD NO.) :")
                    spac()
                    if(ID =="back"):
                        endin()
                        break


                    elif ID.isnumeric() ==False:
                                 print("THE ADHAAR CARD NUMBER IS FALSE!!!![IT CAN ONLY BE NUMBERIC]")
                                 spac2()
                    elif len(ID) ==12 or len(ID)==10:
                                  decider = infpri(["","","","",ID,"",""],"and")
                                  if decider ==[]:
                                      ok = input("press any key to continue ")
                                  else:
                                       print("AN ID SIMILAR TO THIS ALREADY EXISTS!!!!!!PLEASE CHECK IF REGISTRATION HAS ALREADY BE DONE OR ENTER A CORRECT ID!!!!!!!!!!!!!!!!!!!")
                                       spac2()
                                       prip(decider)
                    else:
                        print(
                            "THE NUMBER ENTERED IS INCORRECT....ADHAAR CARD-12(DIGITS)|VOTERID-10(DIGITS)")
                        spac2()
                except ValueError:
                    print("OOPS! ERROR!TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")

                    continue

                except AssertionError:

                    continue




            if(ID =="back"):
                spac()
                break
            else:
                spac2()

            print("="*95)

            print("STATE:", state,"\nNAME:",name,"\nSLOT NO.:",slot,"\nSERIAL NO.:",serial,"\nDATE:",date,"\nID NO.:",ID,"\nCHECK ALL THE INFORMATION!!!!!!!")
            spac3()
            time.sleep(0.23)
            linecr("+",2,2,int(x),"1.ENTER 'reenter' TO ENTER AGAIN \n2. ENTER 'back' TO QUIT TO MAIN MENU")
            linecr("=")
            time.sleep(0.67)
            while(True):

                save = input("DO YOU WANT TO SAVE THE DATA??[y/n/yes/no] :")
                spac2()
                save = save.lower()

                if(save =="yes" or save=="no" or save=='y' or save=='n' or save=="back" or save=="reenter"):
                    time.sleep(0.12)
                    spac2()
                    break

                else:

                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!")
                    spac2()

            try:
                if(save =="yes" or save=='y'):

                    #rcode-name-state-dor-id-slot-serial


                          code = (state[0]+state[2]+slot+chr(64+int(datu[5:7])) + serial+datu[0:4])
                          checker = infpri([code,"","","","","",""],'and')



                          c.execute("INSERT INTO registry VALUES(%s,%s,%s,%s,%s,%s,%s);", (code,name,state,date,ID,serial,slot))

                          m.commit()
                          time.sleep(0.15)
                          print("REGISTRATION CODE IS:", code)
                          print()
                          press = input("press any key to continue")
                          spac2()
                          time.sleep(0.22)
                          print("REGISTRATION COMPLETE!!!!!!!!!!")
                          spac2()
                          endin()
                          break

                elif(save =="back"):
                       endin()
                       break
                elif(save =="reenter"):
                        linecr("-")
                        continue

                elif(save =="no" or save=='n'):
                           print("CANCELLED!!!!!!!!")
                           spac2()
                           endin()
                           break

            except Exception as hmmm:

                         print("UNEXPECTED ERROR:", hmmm)
                         spac2()
                         print("THERE ALREADY EXISTS A REGISTRATION WITH THE SAME INFO!!!!IF YOU ARE TRYING TO CHANGE THE NAME THEN GO TO MODIFY DATA OR ELSE RE-ENTER CORRECT DATA!!!!!!!!!!!!!!!!!!!!")
                         spac2()
                         prip(checker)
                         time.sleep(0.15)
                         print("CANCELLED")
                         spac2()
                         endin()
                         break
            break


    elif(x =="2"):
      done="y"
      linecr("=",2,2,int(x))
      if orderby("NAME","",1)==[]:
          
          spac2
          endin()
      else:
      
        while(done !="no"):
            
            search = input("REGISTRATION CODE :")
            spac2()
            if(search ==""):

                print("EMPTY FIELD!!!!!!!!")
                spac2()
                continue

            elif(search =="back"):
                endin()
                break
            
            else:
                  
                  check = input("press any key to continue")
                  spac2()
                  check = check.lower()

                  if(check =="again"):
                                    
                             continue
                  
                  record=infpri([search,"","","","","","",""])
                  
                  if(record ==[]):

                              print("NO SUCH REGISTRATION CODE EXISTS!!!PLEASE ENTER A VALID NUMBER")
                              spac2()

                  else:
                      name = record[0][1]

                      slot = record[0][5]

                      serial = record[0][6]

                      state = record[0][2]

                      ID = record[0][4]

                      date = record[0][3]

                      print("="*95)
                      print("NAME:", name,"\nSLOT:",slot,"\nSERIAL:",serial,"\nSTATE:",state,"\nID NUMBER:",ID,"\nDATE OF REGISTRATION:",date)
                      print("="*95)
                      spac2()
            while(True):

                done = input("DO YOU WISH TO CONTINUE???[yes/no/y/n] :")
                done=done.lower()
                spac2()
                if(done =="yes" or done=='y'):
                    
                    break
                elif(done=="no" or done=='n'):
                    endin()
                    done='no'
                    break
                else:
                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!")
                    spac2()

    elif(x =="3"):
      final='y'
      linecr("=",2,2,int(x))
      if orderby("NAME","",1)==[]:
          
          spac2
          endin()
      else:
        
        while(final !="no"):
            
            details = input("ID NUMBER :")
            spac2()
            if(details ==""):

                print("EMPTY FIELD!!!!!!!!!!!!")
                spac2()
                continue

            elif(details =="back"):
                   endin()
                   break

            check = input("press any key to continue :")

            check = check.lower()
            spac2()
            if(check =="again"):
                     continue
            rc=infpri(["","","","",details,"",""])
            
            if(rc ==[]):

                print("NO REGISTRATION NUMBER IS LINKED WITH THAT ID NUMBER!!!ENTER A VALID ID NUMBER")
                spac2()
                continue
            else:
                 aka="REGISTRATION CODE : "+rc[0][0]
                 linecr("=",2,2,int(x),aka,0)
                 
                 while(True):
                     final = input("DO YOU WISH TO CONTINUE???[yes/no/y/n]")
                     final=final.lower()
                     spac2()
                     if(final =="yes" or final=="y"):
                              break
                     elif(final=='no' or final=='n'):
                           final='no'
                           spac2()
                           endin()
                           break
                     else:
                         print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!")
                         spac2()
                         continue

    
    elif(x =="4"):
      ok = ""
      linecr("=",2,2,int(x))
      if orderby("NAME","",1)==[]:
              
              spac2
              endin()
      else:
       
        while(ok !='n'):
           try: 
               linecr("=",2,2,int(x),"● 1 NAME \n\n● 2 ERASE THE WHOLE DATABASE \n\n● 3 DELET AN ENTRY \n\n● 4 DEFAULT RESET")
                                                         
               update = input("CHOOSE :")
               spac2()
               check='again'
                  
               if update=='1' or update=='3':
                 while(True):
                   if x!=2 or x!=4:  
                     rcode = input("REGISTRATION CODE :")
                     spac2()
                     if len(rcode)==14:
                        if rcode.isnumeric()==False and rcode.isalpha()==False: 
                           c.execute("select * from registry where R_CODE=%s", (rcode,) )
                           checkdata = c.fetchall()
                           if(checkdata ==[]):
                               print("NO SUCH CODE EXISTS!!!!!!!!!!!!!!!!!!!!!!")
                               spac2()
                               continue
                           else:
                          
                              while True: 
                                   
                                   if(update =="1"):
                                       while(check=='again'):  
                                             new_name = nameing()
                                             print("NAME :",new_name)
                                             spac3()
                                             check = input("press any key to continue :")
                                             spac2()  
                                             if check!='again' and check!='back':
                                                c.execute("update registry set NAME='"+new_name+"' where R_CODE='"+rcode+"';")
                                                m.commit()
                                                print("NAME CHANGE COMPLETED!!!!!!!!!!!!!!!!!!!!")
                                                spac2()
                                                endin()
                                                ok='n'
                                                break
                                             elif check=='back':
                                                    endin()
                                                    break
                                             else:
                                                 continue
                                   
                                   
                                          
                                        
                                   
                                    
                                   elif update=='3':
                                         p2=passcheck()
                                         if p2=='y':
                                             lc=input("press any key to continue [n/no--cancel] :")
                                             lc=lc.lower()
                                             spac2()
                                             print("ENTRY :")
                                             prip(infpri([rcode,"","","","","",""]))
                                             
                                             if lc!='n' and lc!='no':
                                                  
                                                  print("DELETING ENTRY WITH R_CODE :",rcode+"..........") 
                                                  spac2()
                                                  time.sleep(0.21)
                                
                                                  c.execute("DELETE FROM registry WHERE R_CODE=%s;",(rcode,))
                                                  m.commit()
                                                  print("SUCCESSFULLY DELETED ENTRY!!!!!!!!!!!!!!!")
                                                  spac2()
                                                  endin()
                                                  break                                             
                                             else:
                                                 print("CANCELLED!!!!!!!!!!!!!!!")
                                                 spac2()
                                                 endin()
                                                 break
                                         else:
                                             endin()
                                             break
                                         
                                         
                                                          
                                   
                                   break
                    
                     elif(rcode=='back'):
                                endin()
                                ok='n'
                                break
                    
                     elif len(rcode)!=14:
                          print("REGISTRATION CODE HAS ONLY 14 CHARACTERS!!!!!!!!!!!!!!")                       
                          
                          spac2()
                          continue
            
                     else:
                       print("REGISTRATION CODE CONTAINS BOTH NUMBERS AND ALPHABETS!!!!!!!!!!!!!!!")  
                       
                       continue
                 
                 
                     break
                    
               elif update=='4' or update=='2':
                         if update=='4':
                                         p3=passcheck()
                                         if p3=='y':
                                             lc=input("press any key to continue (n/no--cancel) :")
                                             lc=lc.lower()
                                             spac2()
                                             if lc!='n' and lc!='no':
                                                try:  
                                                  
                                                  
                                                  print("ERASING USER SETTING..........")
                                                  time.sleep(0.23)
                                                  delinf()
                                                  x='bye'
                                                  spac2()
                                                  print("SUCCESSFUL!!!!!!!!!!!")
                                                  spac2()
                                                  endin(1)
                                                  break
                                                except Exception as kjs:
                                                            print("UNEXPECTED ERROR :",str(kjs).upper())
                                                            spac2()
                                                            endin()
                                                            break
                                             else:
                                                 print("QUITTING!!!!!!!!!!!!!")
                                                 spac2()
                                                 endin()
                                                 break
                                         else:
                                                                                         
                                             endin()
                                             break                 
                        
                         if update=='2':
                                    p1=passcheck()
                                    if p1=='y': 
                                             
                                             while(True):
                                                     
                                                     try:
                                                        lc=input("press any key to continue (n/no--cancel) :")
                                                        lc=lc.lower()
                                                        spac2()
                                                        if lc!='n' and lc!='no':  
                                                            c.execute("DROP TABLE registry;")
                                                            m.commit()
                                                            print("DROPPING TABLE..........")
                                                            spac2()
                                                            time.sleep(0.21)
                                                            print("DROPPED TABLE REGISTRY!!!!!!!!!")
                                                            spac2()
                                                            time.sleep(0.21)
                                                            print("CLEARED DATABASE vdata!!!!!!!!!!!!!")
                                                            spac2()
                                                            c.execute("create table registry(R_CODE char(15) primary key,NAME char(50) not null,STATE char(50) not null,D_O_R date not null,I_D char(50) not null,SERIAL_N_O int not null,SLOT int not null);")
                                                            endin()
                                                            break
                                                        else:
                                                             print("CANCELLED!!!!!!!!!!!!")
                                                             spac2()
                                                             endin()
                                                             break
                                                     
                                                     except Exception as kj:
                                                            print("UNEXPECTED ERROR :",str(kj).upper())
                                                            spac2()
                                                            endin()
                                                            break
                  
                                    else:
                                        endin()
                                        break
                   
               
               
               
               
               elif update=='back':
                          endin()
                          break
               
               else:
                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!")
                    spac2()
                    continue
                                                   
               break                  
                             
               
               
               
                     
                     
           except Exception as jojo:
                  print("UNEXPECTED ERROR:",jojo)
                  spac2()
           ok = 'n'
    
    
    elif(x =="5"):
      linecr("=",2,2,int(x))
      sale=""
      if orderby("NAME","",1)==[]:
          
          spac2
          endin()
      else:
      
        while(sale !="back"):

            sale=input("FILTER BY: \n\n● 1 MONTH  \n\n● 2 YEAR \n\n● 3 MONTH&YEAR \n\nCHOOSE[BACK-QUIT TO MENU] :")
            
            spac2()
            
            try:
                sale=sale.lower()
                if(sale =="1"):
                    bat='y'
                    while(bat !="no"):

                     
                        salemonth = input("MONTH :")
                        spac2()
                        if(salemonth ==""):

                            print("EMPTY FIELD!!!!!!!!!!!")
                            spac2()
                            continue
                        elif(salemonth.isnumeric()==False):
                                  print("MONTH CAN ONLY BE NUMERIC!!!!!!!!!!!!")
                                  spac2()
                                  continue
                        elif len(salemonth) > 2:
                            print("INCORRECT FORMAT")
                            spac2()
                            continue
                            
                        else:
                               resr=datetester(3,int(salemonth),2004,"MONTH")
                               if resr == "":
                                    salemonth = salemonth.zfill(2)   
                                    slm = "%"+"-"+salemonth+"-"+"%"
                                    c.execute("select count(*) from registry where D_O_R like %s;", (slm,))
                                    car = c.fetchall()
                                    if(car[0][0] ==0):
                                         print("ZERO SALE IN THIS MONTH!!!!!!!!!")
                                         spac2()
                                    else:
                                          print("SALE THIS MONTH- ", car[0][0])
                                          c.execute("select * from registry group by D_O_R having D_O_R like %s", (slm,))
                                          dcar = c.fetchall()
                                          spac2()
                                          prip(dcar)

                               else:
                                   print("E-",resr)
                                   spac2()
                                   continue                            

                        while(True):

                            bat = input("DO YOU WISH TO CONTINUE????[yes/no/y/n]")
                            bat=bat.lower()
                            spac2()
                            if(bat =="yes" or bat=="y"):
                                      bat='no'
                                      sale='again'
                                      break
                            elif(bat=='no' or bat=='n'):
                                    bat='no'
                                    sale='back'
                                    
                                    endin()
                                    break
                                
                            else:
                                 print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!")
                                 spac2()
                                 
                                 

                elif(sale =="2"):

                  
                    cat=""
                    while(cat !="no"):

                        saleyear = input("YEAR :")
                        spac2()
                        if saleyear=="":
                                 print("EMPTY FIELD!!!!!!!!!!!")
                                 spac2()
                        elif saleyear.isnumeric()==False:
                            print("YEAR CAN ONLY BE NUMERIC!!!!!!!!!!!!")
                            spac2()
                            continue
                        elif len(saleyear)!=4:
                            print("INCORRECT FORMAT!!!!!!!!!!")
                            spac2()
                            continue
                        else:
                            rese=datetester(3,2,int(saleyear),"YEAR")
                            
                            if rese=="":
                                   sly = saleyear+"-"+"%"    
                            
                                   c.execute("select count(*) from registry where D_O_R like %s;", (sly,))
                            
                                   car = c.fetchall()
                            
                                   if car[0][0]==0:
                                          print("ZERO SALE IN THIS YEAR")
                                          spac2()
                                   else:
                                        print("SALE IN THIS YEAR :",car[0][0])
                                 
                                        c.execute("select * from registry group by name having D_O_R like '"+saleyear+"-"+"%';")
                                        dcar = c.fetchall()
                                        spac2()
                                        prip(dcar)
                                
                            else:
                                print("E-",rese)
                                spac2()
                                continue
                            
                            while(True):

                                    cat = input("DO YOU WISH TO CONTINUE????[yes/no/y/n]")
                                    cat=cat.lower()
                                    spac2()
                                    if(cat =="yes" or cat=="y"):
                                                  cat='no'
                                                  sale='again'
                                                  break
                                    elif(cat=='no' or cat=='n'):
                                                   cat='no'
                                                   sale='back'
                                                   endin()
                                                   break
                                    else:
                                        print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!!")
                                        spac2()
                                         

                elif(sale =="3"):
                    rat = ""
                    while(rat!="no"):

                        saleyear = input("YEAR :")
                        spac2()
                        salemonth = input("MONTH :")
                        spac2()
                        if saleyear=="" or salemonth=="":
                             print("EMPTY FIELD!!!!!!!!!!!!!!!!!!!")
                             spac2()
                             continue
                        elif(len(saleyear)!=4 or len(salemonth)>2):
                            print("INCORRECT FORMAT!!!!!!!!!!!!!!!!")
                            spac2()
                            continue
                        elif saleyear.isnumeric()==False or salemonth.isnumeric()==False:
                            print("YEAR CAN ONLY BE NUMERIC!!!!!!!!!!!!")
                            spac2()
                            continue
                        else:
                            resa=datetester(3,int(salemonth),int(saleyear),"YEAR")
                            if resa=="":
                                 salemonth = salemonth.zfill(2)
                                 slym = saleyear+"-"+salemonth+"-"+"%"

                                 c.execute("select count(*) from registry where D_O_R like %s;", (slym,))

                                 car = c.fetchall() 
                                 if(car[0][0] ==0):
                                          print("ZERO SALE IN THIS YEAR!!!!!!!!!!!!!!!!")
                                 else:
                                     c.execute("select * from registry group by name having D_O_R like '"+slym+"';")
                                     dcar = c.fetchall()
                                     spac2()
                                     prip(dcar)
                            else:
                                print("E-",resa)
                                spac2()    
                                continue 

                            while(True):

                                     rat = input("DO YOU WISH TO CONTINUE????[yes/no/y/n]")
                                     
                                     rat=rat.lower()
                                     spac2()
                                     
                                     if(rat =="yes" or rat=="y"):
                                                    rat='no'
                                                    sale='again'
                                                    break
                                     
                                     elif rat=='no' or rat=='n':
                                             rat='no'
                                             sale='back'
                                             endin()
                                             break
                                     else:
                                         print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!!!!")
                                         spac2()
                                         
                        
                elif(sale =="back"):
                    endin()
                    break

                elif(sale =="again"):
                    continue

            except Exception as hoooo:
                    print("UNEXPECTED ERROR:",hoooo)
            


    elif(x=='6'):
      ok='y'
      linecr("=", 2, 2, int(x))    
      if orderby("NAME","",1)==[]:
          
          spac2
          endin()
      else:
      
        while(ok!='n'):
            try:
                print("SORT BY: \n\n● 1 NAME \n\n● 2 STATE \n\n● 3 DATE \n\n● 4 SERIAL NUMBER \n\n● 5 SLOT \n"+("-"*96),"\n\n●[ENTER 'BACK' TO EXIT TO MAIN MENU]\n●[ADD 'D' TO THE END OF THE OPTION FOR DESCENDING SORT]","\n\n"+("-"*96))
                sork=input("CHOOSE :")
                spac2()
                sork=sork.lower()
                if(sork =="back"):
                    spac2()
                    endin()
                    break
                  
                
                elif len(sork)<3 and sork in huff or (sork[0] in huff and sork[1]=='d'):
                                              monoga(sork)
                
                else:
                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!")
                    spac2()
                    linecr("-")
                    continue
                    
                while(True):

                            ok = input("DO YOU WISH TO CONTINUE??(y/n/yes/no) :")
                            ok=ok.lower()
                            spac2()
                            
                            if(ok =="y" or ok=="yes"):
                                linecr("-")    
                                break

                            elif(ok=='n' or ok=='no'):
                                        ok='n'
                                        endin()    
                                        break
                            else:
                                print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!")
                                spac2()
                                
                                

            except Exception as kaka:
                if str(kaka)=="":
                      spac2()
                      time.sleep(0.8)
                      endin()
                      break
                else:  
                     print("ERROR:",kaka)
                time.sleep(0.48)
                spac2()
                linecr("-")
                continue
    
    elif(x =="7"):
        
        linecr("-", 2, 2, int(x))
        
        
        linecr("=", 2, 2, int(
            x), "FOR HELP CONTACT US ON \n\n●EMAIL: namekharuko@gmail.com \n\n●CUSTOMER CARE: 110-83-72-369")
        time.sleep(0.67)
        
        
    elif x=='BYE':
        endin(1)
        break
    else:
        
        linecr("-",2,2,9,"PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!!")

        continue
  
   except Exception as lasex:
    
        print("UNEXPECTED ERROR :",lasex)
        endin(1)
        break
print("BYE!!HAVE A NICE DAY :]")



#__________________________________________________________________________________________________________________________________
