#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


import csv


# In[8]:


### System Login Assignment(29/11/22)


def register():
    db = open('D:\\database.txt','r')
    Username = input('Create Username: ')
    Password = int(input('Create Password: '))
    Password1 =int(input('Re-Enter the Password'))

    def spl_char():
        special_characters = re.compile('[~!@#$%^&*()<>?/\|}{: ]' and '[\w]')
        if re.search(Password) != (spl_char):
            print('The Password should contain alteast one digit,special character,upper case and lower case , Restart')
            register()
        else:
            pass

        if  Password!=Password1:
            print("Password doesn't match, Restart")
            register()
        else:
            pass

        if len(Password)<5:
            print('Password too short,Restart')
            register()
        else:
            pass
        
    if len(Password)>16:
                print('Password too long,Restart')
                register()

    elif Username in db:
            print('Username already exists , Restart')
            register()
            
    else:
            db = open('D:\\database.txt',mode='a')
            db.write(Username+','+Password+'\n')
            print('Registration Success..!')

    def forget_Pwd():
            db = open('D:\\database.txt','r')
            Username = input('Enter the Username: ')
            if db == Username:
                print('Your Account Verified,Create New Password')
                register()
            else:
                print('Invalid Username')
                home()


    def access():
                db = open('D:\\database.txt','r')
                Username = input('Enter your Username: ')
                Password = int(input('Enter your Password: '))

                if not len(Username or Password)<1:
                    db=open('D:\\database.txt',mode='a')
                    db.write('Username',',','Password')

                try:
                    if db[Username]:
                        try:
                            if Password == db[Username]:
                                print('Login Success')
                            else:
                                print('Username or Password Incorrect')
                        except:
                            print('Inncorrect Username or Password')
                        else:
                            print('Username or Password  does not exist')

                except:
                    print('Username or Password does not exist ')
                else:
                    print('Enter a Valid Input ')

    def home(option):
            option = input('Login | Sign up | Forgot Password')
            if option == 'Login':
                    access()
            elif option == 'Sign up':
                     register()
            elif option == 'Forgot Password':
                 forget_Pwd()
            else:
                print('Please Select an Option')
    
    home()
    



# In[ ]:




