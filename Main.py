import tkinter as tk
from tkinter import ttk
import sys
import numpy
import random
import sv_ttk
from PIL import Image as IMG
from PIL import ImageTk

UserInfo = numpy.load('db.npy',allow_pickle='True').item()

def exit():
    numpy.save('db.npy',UserInfo)
    sys.exit()

def about():
    CustomMessageBox(title='About',message='This App is created By Pyaae Sone Htoo.')

class CustomMessageBox(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.title(title)
        message_label = ttk.Label(self, text=message)
        message_label.pack(padx=20, pady=10)
        ok_button = ttk.Button(self, text='OK', command=self.destroy)
        ok_button.pack(pady=10)
        self.resizable(False,False)
        self.geometry("+%d+%d" % (self.winfo_screenwidth() // 2 - self.winfo_reqwidth() // 2,self.winfo_screenheight() // 2 - self.winfo_reqheight() // 2))

class Welcome_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Welcome From Mini Games\n       Login Or Database',font=('Times New Roman',20,'bold'))
        self.label1.grid(row=0,column=0,padx=5,pady=100,columnspan=2)
        self.button1 = ttk.Button(self,text='Login',width=25,command=self.login)
        self.button1.grid(row=1,column=0,padx=10,pady=10,ipady=10)
        self.button2 = ttk.Button(self,text='Database',width=25,command=self.db_button)
        self.button2.grid(row=1,column=1,padx=10,pady=10,ipady=10)

    def db_button(self):
        Welcome_Frame.destroy(self)
        DB_loginFrame(app)

    def login(self):
        Welcome_Frame.destroy(self)
        Login_Frame(app)

class Login_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Login',font=('Times New Roman',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=5,pady=50)
        self.label2 = ttk.Label(self,text='User ID')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.input1 = ttk.Entry(self,width=30,justify='center')
        self.input1.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='Password')
        self.label3.grid(row=2,column=0,padx=5,pady=5)
        self.input2 = ttk.Entry(self,width=30,justify='center',show='*')
        self.input2.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='LogIn',width=10,command=self.login)
        self.button1.grid(row=3,column=2,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Forget?',width=10,command=self.forget)
        self.button2.grid(row=4,column=1,padx=5,pady=5)
        self.button3 = ttk.Button(self,text='Change?',width=10,command=self.changepwd)
        self.button3.grid(row=4,column=2,padx=5,pady=5)
        self.button4 = ttk.Button(self,text='Back',width=7,command=self.back)
        self.button4.grid(row=5,column=0,padx=5,pady=100)

    def back(self):
        Login_Frame.destroy(self)
        Welcome_Frame(app)

    def forget(self):
        CustomMessageBox(title='Forget?',message='Contact to your administrator \nto get password.')

    def changepwd(self):
        Login_Frame.destroy(self)
        ChangePwd_Frame(app)

    def login(self):
        global UserID
        UserID = self.input1.get()
        pwd = self.input2.get()
        if UserID in UserInfo:
            if pwd == UserInfo[UserID]['pwd']:
                Login_Frame.destroy(self)
                Main_Frame(app)
            else:
                CustomMessageBox(title='Error!!',message='Wrong Password!')
                Login_Frame.destroy(self)
                Login_Frame(app)
        else:
            CustomMessageBox(title='Error!!',message='User ID not found!')
            Login_Frame.destroy(self)
            Login_Frame(app)

class Main_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Welcome From Mini Games',font=('Times New Roman',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=6,padx=5,pady=20)
        self.label2 = ttk.Label(self,text='User ID :')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='{}'.format(UserID),foreground='red')
        self.label3.grid(row=1,column=1,padx=5,pady=5)
        self.label6 = ttk.Label(self,text='         ')
        self.label6.grid(row=1,column=2,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='Point :')
        self.label4.grid(row=1,column=3,padx=5,pady=5)
        self.label5 = ttk.Label(self,text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))),foreground='red')
        self.label5.grid(row=1,column=4,padx=5,pady=5)
        self.label7 = ttk.Label(self, text='        ')
        self.label7.grid(row=1, column=5, padx=5, pady=5)
        self.button1 = ttk.Button(self,text='Coin Flip',width=20,command=self.coinflip)
        self.button1.grid(row=2,column=0,columnspan=3,padx=10,pady=20,ipady=20)
        self.button2 = ttk.Button(self,text='Guess Game',width=20,command=self.guessgame)
        self.button2.grid(row=2,column=3,columnspan=3,padx=10,pady=20,ipady=20)
        self.button3 = ttk.Button(self,text='Roll Dices',width=20,command=self.rolldic)
        self.button3.grid(row=3,column=0,columnspan=3,padx=10,pady=20,ipady=20)
        self.button4 = ttk.Button(self,text='Rock, Paper, Scissors',width=20,command=self.rcp)
        self.button4.grid(row=3,column=3,columnspan=3,padx=10,pady=20,ipady=20)
        self.button5 = ttk.Button(self, text='Memorize', width=20,command=self.memorize)
        self.button5.grid(row=4, column=0, columnspan=3, padx=10, pady=20, ipady=20)
        self.button6 = ttk.Button(self, text='Card Flip', width=20,command=self.cardflip)
        self.button6.grid(row=4, column=3, columnspan=3, padx=10, pady=20, ipady=20)
        self.button7 = ttk.Button(self,text='Back',width=7,command=self.back)
        self.button7.grid(row=5,column=0,columnspan=2,padx=5,pady=100)

    def memorize(self):
        Main_Frame.destroy(self)
        Memorize_Frame(app)

    def cardflip(self):
        Main_Frame.destroy(self)
        CardFlip_Frame(app)

    def back(self):
        Main_Frame.destroy(self)
        Login_Frame(app)

    def coinflip(self):
        Main_Frame.destroy(self)
        CoinFlip_Frame(app)

    def guessgame(self):
        Main_Frame.destroy(self)
        GuessGame_Frame(app)

    def rolldic(self):
        Main_Frame.destroy(self)
        RollDice_Frame(app)

    def rcp(self):
        Main_Frame.destroy(self)
        Rock_Scissor_Paper(app)

class CoinFlip_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.choicevar = tk.StringVar()
        self.choiceval = ['Head', 'Tail']
        self.ans = random.choice(self.choiceval)
        if self.ans == 'Head':
            self.i = IMG.open('1001.png')
            self.i1 = self.i.resize((110,110))
            self.img = ImageTk.PhotoImage(self.i1)
        else:
            self.i = IMG.open('1002.png')
            self.i1 = self.i.resize((110,110))
            self.img = ImageTk.PhotoImage(self.i1)
        self.label1 = ttk.Label(self, text='Welcome From Coin Flip Games', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        self.label2 = ttk.Label(self, text='User ID :')
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.label3 = ttk.Label(self, text='{}'.format(UserID), foreground='red')
        self.label3.grid(row=1, column=1, padx=5, pady=5)
        self.label6 = ttk.Label(self, text='         ')
        self.label6.grid(row=1, column=2, padx=5, pady=5)
        self.label4 = ttk.Label(self, text='Point :')
        self.label4.grid(row=1, column=3, padx=5, pady=5)
        self.label5 = ttk.Label(self, text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))), foreground='red')
        self.label5.grid(row=1, column=4, padx=5, pady=5)
        self.label7 = ttk.Label(self, text='        ')
        self.label7.grid(row=1, column=5, padx=5, pady=5)
        self.label8 = ttk.Label(self,text='Choose')
        self.label8.grid(row=2,column=0,padx=5,pady=5,columnspan=3)
        self.choice = ttk.Combobox(self,textvariable=self.choicevar,values=self.choiceval,state='readonly')
        self.choice.grid(row=2,column=3,columnspan=2,padx=5,pady=5,sticky='ew')
        self.choice.set(self.choiceval[0])
        self.label9 = ttk.Label(self,text='Enter Amount To Bet')
        self.label9.grid(row=3,column=0,padx=5,pady=5,columnspan=3)
        self.input1 = ttk.Entry(self,justify='center',width=15)
        self.input1.grid(row=3,column=3,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Bet',width=7,command=self.betBut)
        self.button1.grid(row=4,column=2,columnspan=2,padx=5,pady=5)
        self.label10 = ttk.Label(self,text='The answer is "{}".'.format(self.ans),font=('Arial',18))
        self.label11 = ttk.Label(self,image=self.img)
        self.label12 = ttk.Label(self,text='Your answer is correct.')
        self.label13 = ttk.Label(self,text='Sorry, you choose wrong.')
        self.label14 = ttk.Label(self,text='Do you want to play again?')
        self.button2 = ttk.Button(self,text='Yes',width=7,command=self.yes)
        self.button3 = ttk.Button(self,text='No',width=7,command=self.back)
        self.button4 = ttk.Button(self,text='About Game',width=10,command=self.about)
        self.button4.grid(row=20,column=5,padx=5,pady=80)
        self.button5 = ttk.Button(self,text='Back',width=7,command=self.back)
        self.button5.grid(row=20,column=0,padx=5,pady=80)

    def betBut(self):
        self.choice.config(state='disable')
        self.input1.config(state='disable')
        self.button1.config(state='disable')
        point = self.input1.get()
        userchoice = self.choicevar.get()
        try:
            point = round(float(point), 2)
            if 0 >= point or point > UserInfo[UserID]['point']:
                CustomMessageBox(title='Error!',message='bet Amount should not be over {} or 0 and below 0.'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))))
                CoinFlip_Frame.destroy(self)
                CoinFlip_Frame(app)
            else:
                self.label10.grid(row=5, column=0, columnspan=6, padx=5, pady=5)
                self.label11.grid(row=6, column=0, columnspan=6, padx=5, pady=30)
                if userchoice == self.ans:
                    self.label12.grid(row=7,column=0,columnspan=6,padx=5,pady=5)
                    self.label14.grid(row=8,column=0,columnspan=6,padx=5,pady=5)
                    self.button2.grid(row=9,column=2,padx=5,pady=5)
                    self.button3.grid(row=9,column=3,padx=5,pady=5)
                    UserInfo[UserID]['point'] = UserInfo[UserID]['point'] +(point * 2)
                else:
                    self.label13.grid(row=7,column=0,columnspan=6,padx=5,pady=5)
                    self.label14.grid(row=8, column=0, columnspan=6, padx=5, pady=5)
                    self.button2.grid(row=9, column=2, padx=5, pady=5)
                    self.button3.grid(row=9, column=3, padx=5, pady=5)
                    UserInfo[UserID]['point'] = UserInfo[UserID]['point'] - point
        except ValueError:
            CustomMessageBox(title='Error!',message='Bet Point should be a valid number.')
            CoinFlip_Frame.destroy(self)
            CoinFlip_Frame(app)

    def yes(self):
        CoinFlip_Frame.destroy(self)
        CoinFlip_Frame(app)

    def back(self):
        CoinFlip_Frame.destroy(self)
        Main_Frame(app)

    def about(self):
        CustomMessageBox(title='About Coin Flip Game',message='You can choose "Head" or "Tail".\nApp will automatically generate and \nshow answer. \nIf you win, you will get double point.')

class GuessGame_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.choicevar = tk.StringVar()
        self.randomchoice = random.randint(1,10)
        self.choice = ['1','2','3','4','5','6','7','8','9','10']
        self.label1 = ttk.Label(self, text='Welcome From Guess Games', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        self.label2 = ttk.Label(self, text='User ID :')
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.label3 = ttk.Label(self, text='{}'.format(UserID), foreground='red')
        self.label3.grid(row=1, column=1, padx=5, pady=5)
        self.label6 = ttk.Label(self, text='         ')
        self.label6.grid(row=1, column=2, padx=5, pady=5)
        self.label4 = ttk.Label(self, text='Point :')
        self.label4.grid(row=1, column=3, padx=5, pady=5)
        self.label5 = ttk.Label(self, text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))), foreground='red')
        self.label5.grid(row=1, column=4, padx=5, pady=5)
        self.label7 = ttk.Label(self, text='        ')
        self.label7.grid(row=1, column=5, padx=5, pady=5)
        self.label8 = ttk.Label(self,text='Choose the Number : ')
        self.label8.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
        self.choiceval = ttk.Combobox(self,textvariable=self.choicevar,values=self.choice,state='readonly')
        self.choiceval.grid(row=2,column=3,sticky ='ew',padx=5,pady=5,columnspan=2)
        self.choiceval.set(self.choice[0])
        self.button1 = ttk.Button(self,text='Choice',width=7,command=self.btnchoice)
        self.button1.grid(row=2,column=5,padx=5,pady=5)
        self.label9 = ttk.Label(self,text='Amount')
        self.input1 = ttk.Entry(self,width=16,justify='center')
        self.button2 = ttk.Button(self,text='Bet',width=7,command=self.bet)
        self.label10 = ttk.Label(self,text='The Random Number is ',font=('Arial',16,'bold'))
        self.label11 = ttk.Label(self,text='{}'.format(self.randomchoice),font=('Arial',140,'bold'))
        self.label12 = ttk.Label(self,text='Congratulation You Win.')
        self.label13 = ttk.Label(self,text='Sorry, You make wrong choice.')
        self.label14 = ttk.Label(self, text='Do you want to play again?')
        self.button3 = ttk.Button(self, text='Yes', width=7, command=self.yes)
        self.button4 = ttk.Button(self, text='No', width=7, command=self.back)
        self.button10 = ttk.Button(self, text='About Game', width=10, command=self.about)
        self.button10.grid(row=20, column=5, padx=5, pady=100)
        self.button11 = ttk.Button(self, text='Back', width=7, command=self.back)
        self.button11.grid(row=20, column=0, padx=5, pady=100)

    def back(self):
        GuessGame_Frame.destroy(self)
        Main_Frame(app)

    def about(self):
        CustomMessageBox(title='About Coin Flip Game',message='You can choose any number between 1 to 10.\nIf you can guess the correct number of app choice,\nYou will win and get 10 times points.')

    def btnchoice(self):
        self.button1.config(state='disable')
        self.choiceval.config(state='disable')
        self.label9.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
        self.input1.grid(row=3,column=3,columnspan=2,padx=5,pady=5)
        self.button2.grid(row=3,column=5,padx=5,pady=5)

    def bet(self):
        self.input1.config(state='disable')
        self.button2.config(state='disable')
        betamt = self.input1.get()
        try:
            betamt = round(float(betamt), 2)
            if betamt <= 0 or betamt > UserInfo[UserID]['point']:
                CustomMessageBox(title='Error!!',message='Bet amount should not be 0 or less than 0 and\nshould not be greater than {}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))))
                GuessGame_Frame.destroy(self)
                GuessGame_Frame(app)
            else:
                self.label10.grid(row=4,column=0,columnspan=6,padx=5,pady=5)
                self.label11.grid(row=5,column=0,columnspan=6,padx=5,pady=5)
                if str(self.choicevar.get()) == str(self.randomchoice):
                    self.label12.grid(row=6,column=0,columnspan=6,padx=5,pady=5)
                    UserInfo[UserID]['point'] = UserInfo[UserID]['point'] + round(betamt * 10, 2)
                    self.label14.grid(row=7,column=0,columnspan=6,padx=5,pady=5)
                    self.button3.grid(row=8,column=2,padx=5,pady=5)
                    self.button4.grid(row=8,column=3,padx=5,pady=5)
                else:
                    self.label13.grid(row=6,column=0,columnspan=6,padx=5,pady=5)
                    UserInfo[UserID]['point'] = UserInfo[UserID]['point'] - round(betamt, 2)
                    self.label14.grid(row=7, column=0, columnspan=6, padx=5, pady=5)
                    self.button3.grid(row=8, column=2, padx=5, pady=5)
                    self.button4.grid(row=8, column=3, padx=5, pady=5)
        except ValueError:
            CustomMessageBox(title='Error!!',message='Bet Amount should be a valid number')
            GuessGame_Frame.destroy(self)
            GuessGame_Frame(app)

    def yes(self):
        GuessGame_Frame.destroy(self)
        GuessGame_Frame(app)

class RollDice_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.ans = self.dice1 + self.dice2
        if self.dice1 == 1:
            self.i = IMG.open('3001.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.dice1 == 2:
            self.i = IMG.open('3002.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.dice1 == 3:
            self.i = IMG.open('3003.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.dice1 == 4:
            self.i = IMG.open('3004.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.dice1 == 5:
            self.i = IMG.open('3005.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.dice1 == 6:
            self.i = IMG.open('3006.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        if self.dice2 == 1:
            self.i = IMG.open('3001.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        elif self.dice2 == 2:
            self.i = IMG.open('3002.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        elif self.dice2 == 3:
            self.i = IMG.open('3003.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        elif self.dice2 == 4:
            self.i = IMG.open('3004.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        elif self.dice2 == 5:
            self.i = IMG.open('3005.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        elif self.dice2 == 6:
            self.i = IMG.open('3006.png')
            self.i1 = self.i.resize((110,110))
            self.img2 = ImageTk.PhotoImage(self.i1)
        self.label1 = ttk.Label(self, text='Welcome From Roll Dices Game', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        self.label2 = ttk.Label(self, text='User ID :')
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.label3 = ttk.Label(self, text='{}'.format(UserID), foreground='red')
        self.label3.grid(row=1, column=1, padx=5, pady=5)
        self.label6 = ttk.Label(self, text='         ')
        self.label6.grid(row=1, column=2, padx=5, pady=5)
        self.label4 = ttk.Label(self, text='Point :')
        self.label4.grid(row=1, column=3, padx=5, pady=5)
        self.label5 = ttk.Label(self, text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))), foreground='red')
        self.label5.grid(row=1, column=4, padx=5, pady=5)
        self.label7 = ttk.Label(self, text='        ')
        self.label7.grid(row=1, column=5, padx=5, pady=5)
        self.label8 = ttk.Label(self,text='Please Choose odd or even :')
        self.label8.grid(row=2,column=0,padx=5,pady=5,columnspan=3)
        self.choicevar = tk.StringVar()
        self.choiceval = ['Odd', 'Even']
        self.choice = ttk.Combobox(self, textvariable=self.choicevar, values=self.choiceval,state='readonly')
        self.choice.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky='ew')
        self.choice.set(self.choiceval[0])
        self.button1 = ttk.Button(self,text='Confirm',width=12,command=self.confirm)
        self.button1.grid(row=2,column=5,columnspan=6,padx=5,pady=5)
        self.label9 = ttk.Label(self,text='Choice Correct Number :')
        self.choicevarnumber = tk.StringVar()
        self.button2 = ttk.Button(self,text='Confirm',width=12,command=self.confirm2)
        self.label10 = ttk.Label(self,text='Bet Amount')
        self.input1 = ttk.Entry(self,width=15)
        self.button3 = ttk.Button(self,text='Bet',width=7,command=self.bet)
        self.label11 = ttk.Label(self,image=self.img1)
        self.label12 = ttk.Label(self,image=self.img2)
        self.label13 = ttk.Label(self)
        self.label14 = ttk.Label(self,font=('TimeNewRoman 15 bold'),foreground='red')
        self.label15 = ttk.Label(self, text='Do you want to play again?')
        self.button4 = ttk.Button(self, text='Yes', width=7, command=self.yes)
        self.button5 = ttk.Button(self, text='No', width=7, command=self.back)
        self.button10 = ttk.Button(self, text='About Game', width=10, command=self.about)
        self.button10.grid(row=20, column=5, padx=5, pady=100)
        self.button11 = ttk.Button(self, text='Back', width=7, command=self.back)
        self.button11.grid(row=20, column=0, padx=5, pady=100)

    def about(self):
        CustomMessageBox(title='About Roll Dice Game.',message='If you choice correct on even or odd\nyou will get double on bet amount.\nIf you choice on correct number\nyou will get 100 time of bet amount.')

    def back(self):
        RollDice_Frame.destroy(self)
        Main_Frame(app)

    def confirm(self):
        self.choice.config(state='disable')
        self.button1.config(state='disable')
        self.label9.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
        if self.choicevar.get() == "Odd":
            self.odd = ['3', '5', '7', '9', '11']
            self.choicevalnumber = ttk.Combobox(self,textvariable= self.choicevarnumber,values= self.odd,state='readonly')
            self.choicevalnumber.grid(row=3, column=3, sticky='ew', padx=5, pady=5, columnspan=2)
            self.choicevalnumber.set(self.odd[0])
        else:
            self.even = ['2', '4', '6', '8', '10', '12']
            self.choicevalnumber = ttk.Combobox(self,textvariable= self.choicevarnumber,values= self.even,state='readonly')
            self.choicevalnumber.grid(row=3, column=3, sticky='ew', padx=5, pady=5, columnspan=2)
            self.choicevalnumber.set(self.even[0])
        self.button2.grid(row=3,column=5,columnspan=6,padx=5,pady=5)

    def confirm2(self):
        self.choicevalnumber.config(state='disable')
        self.button2.config(state='disable')
        self.label10.grid(row=6,column=0,columnspan=2,padx=5,pady=5)
        self.input1.grid(row=6,column=2,columnspan=2,padx=5,pady=5)
        self.button3.grid(row=6,column=4,columnspan=2,padx=5,pady=5)

    def bet(self):
        usrch = self.choicevarnumber.get()
        betamt = self.input1.get()
        try:
            betamt = round(float(betamt), 2)
            if betamt <= 0 or betamt > UserInfo[UserID]['point']:
                CustomMessageBox(title='Error!!',message='Bet amount should not be 0 or less than 0 and\nshould not be greater than {}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))))
            else:
                self.input1.config(state='disable')
                self.button3.config(state='disable')
                self.label11.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
                self.label12.grid(row=7, column=3, columnspan=3, padx=5, pady=5)
                if self.ans % 2 == 0:
                    self.text1 = 'The answer is "Even".'
                    if self.choicevar.get() == 'Even':
                        self.amount = round(betamt * 2, 2)
                        if usrch == str(self.ans):
                            UserInfo[UserID]['point'] = UserInfo[UserID]['point'] + round(self.amount * 50, 2)
                            self.text3 = 'Congratulation You win for both.'
                        else:
                            UserInfo[UserID]['point'] = UserInfo[UserID]['point'] + self.amount
                            self.text3 = 'Congratulation you win for "Even".\nBut you lose for correct number.'
                    else:
                        self.text3 = 'Sorry,you lose.'
                        UserInfo[UserID]['point'] = UserInfo[UserID]['point'] - round(betamt, 2)
                else:
                    self.text1 = 'The answer is "Odd".'
                    if self.choicevar.get() == 'Odd':
                        self.amount = round(betamt * 2, 2)
                        if usrch == str(self.ans):
                            UserInfo[UserID]['point'] = UserInfo[UserID]['point'] + round(self.amount * 50, 2)
                            self.text3 = 'Congratulation You win for both.'
                        else:
                            UserInfo[UserID]['point'] = UserInfo[UserID]['point'] + self.amount
                            self.text3 = 'Congratulation you win for "Odd".\nBut you lose for correct number.'
                    else:
                        self.text3 = 'Sorry,you lose.'
                        UserInfo[UserID]['point'] = UserInfo[UserID]['point'] - round(betamt, 2)
                self.text2 = 'The correct number is "{}".'.format(self.ans)
                self.label13.grid(row=8, column=0, columnspan=6, padx=5, pady=5)
                self.label13.config(text='{}\n{}'.format(self.text1, self.text2))
                self.label14.grid(row=9,column=0,columnspan=6,padx=5,pady=5)
                self.label14.config(text=self.text3)
            self.label15.grid(row=10,column=0,columnspan=6,padx=5,pady=5)
            self.button4.grid(row=11,column=0,columnspan=3,padx=5,pady=5)
            self.button5.grid(row=11,column=3,columnspan=3,padx=5,pady=5)



        except:
            CustomMessageBox(title='Error',message='Bet amount should be number.')

    def yes(self):
        RollDice_Frame.destroy(self)
        RollDice_Frame(app)

    def back(self):
        RollDice_Frame.destroy(self)
        Main_Frame(app)

class Rock_Scissor_Paper(ttk.Frame):
    def __init__(self,conatiner):
        super().__init__(conatiner)
        self.pack()
        self.C_Guess = random.randint(1,3)
        if self.C_Guess == 1:
            self.i = IMG.open('4001.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.C_Guess == 2:
            self.i = IMG.open('4002.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        elif self.C_Guess == 3:
            self.i = IMG.open('4003.png')
            self.i1 = self.i.resize((110,110))
            self.img1 = ImageTk.PhotoImage(self.i1)
        
        self.label1 = ttk.Label(self, text='Welcome From Rock Scissor Paper', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        self.label2 = ttk.Label(self, text='User ID :')
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.label3 = ttk.Label(self, text='{}'.format(UserID), foreground='red')
        self.label3.grid(row=1, column=1, padx=5, pady=5)
        self.label6 = ttk.Label(self, text='         ')
        self.label6.grid(row=1, column=2, padx=5, pady=5)
        self.label4 = ttk.Label(self, text='Point :')
        self.label4.grid(row=1, column=3, padx=5, pady=5)
        self.label5 = ttk.Label(self, text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))), foreground='red')
        self.label5.grid(row=1, column=4, padx=5, pady=5)
        self.label7 = ttk.Label(self, text='        ')
        self.label7.grid(row=1, column=5, padx=5, pady=5)
        self.label8 = ttk.Label(self,text='Please choose \nRock Scisor or Paper :')
        self.label8.grid(row=2,column=0,columnspan=3,padx=5,pady=5)
        self.choicevar = tk.StringVar()
        self.choiceval = ['Rock', 'Scissor','Paper']
        self.choice = ttk.Combobox(self,textvariable= self.choicevar,values= self.choiceval,state='readonly')
        self.choice.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky='ew')
        self.choice.set(self.choiceval[0])
        self.button1= ttk.Button(self,text='Confirm',width=12,command=self.confirmbtn_1)
        self.button1.grid(row=3,column=0,columnspan=6,padx=5,pady=5)
        self.label9 = ttk.Label(self,text='Bet Amount')
        self.input1 = ttk.Entry(self,width=12)
        self.button2 = ttk.Button(self,text='Confirm',width=12,command=self.confirmbtn_2)
        self.label10 = ttk.Label(self,image=self.img1)
        self.label11 = ttk.Label(self)
        self.label12 = ttk.Label(self,font=('Times New Roman', 30, 'bold'))
        self.label13 = ttk.Label(self, text='Do you want to play again?')
        self.button3 = ttk.Button(self, text='Yes', width=7, command=self.yes)
        self.button4 = ttk.Button(self, text='No', width=7, command=self.back)
        self.button10 = ttk.Button(self, text='About Game', width=10, command=self.about)
        self.button10.grid(row=20, column=5, padx=5, pady=100)
        self.button11 = ttk.Button(self, text='Back', width=7, command=self.back)
        self.button11.grid(row=20, column=0, padx=5, pady=100)

    def about(self):
        CustomMessageBox(title='About Rock Scissor Paper Game',message='If You win you will get Three times of bet amount.\nIf Draw we will refund.')

    def back(self):
        RollDice_Frame.destroy(self)
        Main_Frame(app)
    

        
    def confirmbtn_1(self):
        self.choice.config(state='disable')
        self.button1.grid_forget()
        self.label9.grid(row=4,column=0,columnspan=3,padx=5,pady=5)
        self.input1.grid(row=4,column=3,columnspan=2)
        self.button2.grid(row=5,column=0,columnspan=6,padx=5,pady=5)
        
    def confirmbtn_2(self):
        betamt = self.input1.get()
        try:
            betamt = round(float(betamt), 2)
            if betamt <= 0 or betamt > UserInfo[UserID]['point']:
                CustomMessageBox(title='Error!!',message='Bet amount should not be 0 or less than 0 and\nshould not be greater than {}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))))
            else:
                self.label10.grid(row=6,column=0,columnspan=3,padx=5,pady=5)
                self.label11.grid(row=6,column=3,columnspan=3,padx=5,pady=5)
                self.label12.grid(row=7,column=0,columnspan=6,padx=5,pady=5)
                self.input1.config(state='disable')
                self.button2.grid_forget()
                if self.C_Guess == 1:
                    if self.choicevar.get() == 'Paper':
                        self.i = IMG.open('4004.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='Draw',foreground='yellow')
                    elif self.choicevar.get() == 'Rock':
                        self.i = IMG.open('4005.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Lose',foreground='red')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] - round(betamt, 2)
                    elif self.choicevar.get() == 'Scissor':
                        self.i = IMG.open('4006.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Win',foreground='green')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] + round(betamt * 3, 2)
                elif self.C_Guess == 2:
                    if self.choicevar.get() == 'Paper':
                        self.i = IMG.open('4004.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Win',foreground='green')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] + round(betamt * 3, 2)
                    elif self.choicevar.get() == 'Rock':
                        self.i = IMG.open('4005.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='Draw',foreground='yellow')
                    elif self.choicevar.get() == 'Scissor':
                        self.i = IMG.open('4006.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Lose',foreground='red')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] - round(betamt, 2)
                elif self.C_Guess == 3:
                    if self.choicevar.get() == 'Paper':
                        self.i = IMG.open('4004.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Lose',foreground='red')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] - round(betamt, 2)
                    elif self.choicevar.get() == 'Rock':
                        self.i = IMG.open('4005.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='You Win',foreground='green')
                        UserInfo[UserID]['point']=UserInfo[UserID]['point'] + round(betamt * 3, 2)
                    elif self.choicevar.get() == 'Scissor':
                        self.i = IMG.open('4006.png')
                        self.i1 = self.i.resize((110,110))
                        self.img2 = ImageTk.PhotoImage(self.i1)
                        self.label11.config(image=self.img2)
                        self.label12.config(text='Draw',foreground='yellow')
                self.label13.grid(row=8,column=0,columnspan=6,padx=5,pady=5)
                self.button3.grid(row=9,column=0,columnspan=3,padx=5,pady=5)
                self.button4.grid(row=9,column=3,columnspan=3,padx=5,pady=5)
        except:
            CustomMessageBox(title='Error',message='Bet amount should be number.')
            
    def yes(self):
        Rock_Scissor_Paper.destroy(self)
        Rock_Scissor_Paper(app)

    def back(self):
        Rock_Scissor_Paper.destroy(self)
        Main_Frame(app)



class CardFlip_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack()
        
        self.multipliers = {1: 0.8, 2: 1, 3: 1.5, 4: 2, 5: 4, 6: 8, 7: 10, 8: 20}
        self.betamt = 0
        self.matches_found = 0
        self.wrong_attempts = 0
        self.max_wrongs = 3
        
        self.cards = []
        self.buttons = []
        self.first_flipped = None
        self.second_flipped = None
        self.lock_board = False
        
        self.images = {} # Will store PhotoImage objects so they aren't garbage collected
        self.cover_image = None
        
        self.setup_ui()
        
    def setup_ui(self):
        self.label1 = ttk.Label(self, text='Welcome to Card Flip Game', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        
        ttk.Label(self, text='User ID :').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self, text='{}'.format(UserID), foreground='red').grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self, text='Point :').grid(row=1, column=3, padx=5, pady=5)
        self.point_label = ttk.Label(self, text='{:.2f}'.format(float(UserInfo[UserID]['point'])), foreground='red')
        self.point_label.grid(row=1, column=4, padx=5, pady=5)
        
        self.bet_frame = ttk.Frame(self)
        self.bet_frame.grid(row=2, column=0, columnspan=6, pady=10)
        ttk.Label(self.bet_frame, text='Bet Amount: ').pack(side='left', padx=5)
        self.bet_input = ttk.Entry(self.bet_frame, width=10, justify='center')
        self.bet_input.pack(side='left', padx=5)
        self.start_btn = ttk.Button(self.bet_frame, text='Start Game', command=self.start_game)
        self.start_btn.pack(side='left', padx=5)
        
        self.status_label = ttk.Label(self, text='', font=('Arial', 14, 'bold'))
        self.status_label.grid(row=3, column=0, columnspan=6, pady=5)
        
        self.grid_frame = ttk.Frame(self)
        
        self.action_frame = ttk.Frame(self)
        self.continue_btn = ttk.Button(self.action_frame, text='Continue', command=self.resume_game)
        self.stop_btn = ttk.Button(self.action_frame, text='Stop & Claim', command=self.cash_out)
        
        self.about_btn = ttk.Button(self, text='About Game', command=self.about)
        self.about_btn.grid(row=6, column=3, columnspan=3, pady=20, padx=5)
        self.back_btn = ttk.Button(self, text='Back', command=self.back)
        self.back_btn.grid(row=6, column=0, columnspan=3, pady=20, padx=5)

    def update_points(self):
        self.point_label.config(text='{:.2f}'.format(float(UserInfo[UserID]['point'])))

    def load_images(self):
        # Create a simple colored cover since we don't have a cover image
        try:
            for i in range(1, 9):
                for j in range(2):
                    card_id = f'600{i}-{j}'
                    img = IMG.open(f'{card_id}.png')
                    img = img.resize((50, 90)) # 5x9 scale approx (width=50, height=90)
                    self.images[card_id] = ImageTk.PhotoImage(img)
        except Exception as e:
            CustomMessageBox('Error', f'Could not load card images: {e}')
            return False
        return True

    def start_game(self):
        try:
            amt = round(float(self.bet_input.get()), 2)
        except ValueError:
            CustomMessageBox('Error', 'Please enter a valid number!')
            return
            
        if amt <= 0:
            CustomMessageBox('Error', 'Bet amount must be greater than 0!')
            return
            
        if amt > UserInfo[UserID]['point']:
            CustomMessageBox('Error', 'You do not have enough points for this bet!')
            return
            
        if not self.load_images():
            return
            
        self.betamt = amt
        UserInfo[UserID]['point'] -= self.betamt
        self.update_points()
        
        self.start_btn.config(state='disabled')
        self.bet_input.config(state='disabled')
        self.back_btn.config(state='disabled')
        
        self.matches_found = 0
        self.wrong_attempts = 0
        
        self.status_label.config(text='Memorize the cards!', foreground='blue')
        self.grid_frame.grid(row=4, column=0, columnspan=6, pady=10)
        self.setup_cards()

    def setup_cards(self):
        for btn in self.buttons:
            btn.destroy()
        self.buttons.clear()
        
        self.cards = []
        for i in range(1, 9):
            self.cards.append({'id': f'600{i}-0', 'match_group': i, 'flipped': False})
            self.cards.append({'id': f'600{i}-1', 'match_group': i, 'flipped': False})
            
        random.shuffle(self.cards)
        
        for i, card in enumerate(self.cards):
            # Show the cards initially
            btn = tk.Button(self.grid_frame, image=self.images[card['id']], bg='white', width=50, height=90, 
                            command=lambda idx=i: self.flip_card(idx))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Lock the board during the preview phase
        self.lock_board = True
        
        # After 2 seconds, turn them all back into blocks
        self.after(2000, self.hide_all_cards)

    def hide_all_cards(self):
        for i, btn in enumerate(self.buttons):
            # Change back to gray blocks
            btn.config(image='', bg='gray', width=5, height=5)
            self.cards[i]['flipped'] = False
        
        self.lock_board = False
        self.status_label.config(text=f'Find the matching pairs! Errors left: {self.max_wrongs}', foreground='blue')
            
    def flip_card(self, idx):
        if self.lock_board or self.cards[idx]['flipped']:
            return
            
        self.cards[idx]['flipped'] = True
        card_id = self.cards[idx]['id']
        
        self.buttons[idx].config(image=self.images[card_id], bg='white', width=50, height=90)
        
        if self.first_flipped is None:
            self.first_flipped = idx
        else:
            self.second_flipped = idx
            self.check_match()
            
    def check_match(self):
        idx1 = self.first_flipped
        idx2 = self.second_flipped
        
        if self.cards[idx1]['match_group'] == self.cards[idx2]['match_group']:
            # Match found
            self.matches_found += 1
            self.first_flipped = None
            self.second_flipped = None
            
            if self.matches_found == 8:
                self.game_won()
            else:
                self.status_label.config(text=f'Match! Matches: {self.matches_found}/8. Errors left: {self.max_wrongs - self.wrong_attempts}', foreground='green')
        else:
            # Not a match
            self.lock_board = True
            self.wrong_attempts += 1
            self.status_label.config(text=f'Wrong! Errors left: {self.max_wrongs - self.wrong_attempts}', foreground='red')
            self.after(1000, self.unflip_cards)

    def unflip_cards(self):
        idx1 = self.first_flipped
        idx2 = self.second_flipped
        
        self.cards[idx1]['flipped'] = False
        self.cards[idx2]['flipped'] = False
        
        self.buttons[idx1].config(image='', bg='gray', width=5, height=5)
        self.buttons[idx2].config(image='', bg='gray', width=5, height=5)
        
        self.first_flipped = None
        self.second_flipped = None
        
        if self.wrong_attempts >= self.max_wrongs:
            self.lock_board = True
            self.status_label.config(text='3 Wrongs! Game Over. You lose!', foreground='red')
            self.reset_ui()
        else:
            self.prompt_cash_out_or_continue()
            
    def prompt_cash_out_or_continue(self):
        self.lock_board = True
        
        if self.matches_found == 0:
            # If they haven't matched anything yet, they can only continue playing
            self.status_label.config(text=f'Wrong! {self.wrong_attempts}/3 errors. Continue playing?', foreground='purple')
            self.action_frame.grid(row=5, column=0, columnspan=6, pady=10)
            self.continue_btn.pack(side='left', padx=10)
            self.stop_btn.pack_forget()
        else:
            multiplier = self.multipliers.get(self.matches_found, 1)
            win_amt = round(self.betamt * multiplier, 2)
            self.status_label.config(text=f'Wrong! {self.wrong_attempts}/3 errors. Continue or Cash out {win_amt} pts?', foreground='purple')
            self.action_frame.grid(row=5, column=0, columnspan=6, pady=10)
            self.continue_btn.pack(side='left', padx=10)
            self.stop_btn.pack(side='left', padx=10)

    def resume_game(self):
        self.lock_board = False
        self.action_frame.grid_forget()
        self.status_label.config(text=f'Find the pairs! Errors left: {self.max_wrongs - self.wrong_attempts}', foreground='blue')

    def game_won(self):
        multiplier = self.multipliers.get(8, 20)
        win_amt = round(self.betamt * multiplier, 2)
        UserInfo[UserID]['point'] += win_amt
        self.update_points()
        self.status_label.config(text=f'You found all pairs! You won {win_amt} points!', foreground='green')
        self.reset_ui()

    def cash_out(self):
        multiplier = self.multipliers.get(self.matches_found, 1)
        win_amt = round(self.betamt * multiplier, 2)
        UserInfo[UserID]['point'] += win_amt
        self.update_points()
        
        self.status_label.config(text=f'You cashed out {win_amt} points!', foreground='green')
        self.action_frame.grid_forget()
        self.reset_ui()

    def reset_ui(self):
        numpy.save('db.npy', UserInfo)
        self.start_btn.config(state='normal')
        self.bet_input.config(state='normal')
        self.back_btn.config(state='normal')
        
        # Expose the board slightly for 2 seconds then hide it
        self.after(2000, lambda: self.grid_frame.grid_forget())

    def about(self):
        msg = (
            "Card Flip Game!\n"
            "Find all 8 matching pairs. You have 3 lives (errors).\n"
            "If you make wrong guesses, you can cash out your current progress or continue.\n"
            "Payout Multipliers:\n"
            "1 Match: 0.8x bet\n"
            "2 Matches: 1x bet\n"
            "3 Matches: 1.5x bet\n"
            "4 Matches: 2x bet\n"
            "5 Matches: 4x bet\n"
            "6 Matches: 8x bet\n"
            "7 Matches: 10x bet\n"
            "8 Matches: 20x bet"
        )
        CustomMessageBox('About Card Flip', msg)

    def back(self):
        CardFlip_Frame.destroy(self)
        Main_Frame(app)

class Memorize_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack()
        
        self.multipliers = {1: 0.8, 2: 1, 3: 1.2, 4: 1.5, 5: 2, 6: 3, 7: 5, 8: 10, 9: 100}
        self.sequence_length = 1
        self.sequence = []
        self.player_sequence = []
        self.betamt = 0
        self.buttons = []
        self.playing = False
        
        # Header UI
        self.label1 = ttk.Label(self, text='Welcome to Memorize Game', font=('Times New Roman', 20, 'bold'))
        self.label1.grid(row=0, column=0, columnspan=6, padx=5, pady=20)
        
        ttk.Label(self, text='User ID :').grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self, text='{}'.format(UserID), foreground='red').grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self, text='Point :').grid(row=1, column=3, padx=5, pady=5)
        self.point_label = ttk.Label(self, text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))), foreground='red')
        self.point_label.grid(row=1, column=4, padx=5, pady=5)
        
        # Betting UI
        self.bet_frame = ttk.Frame(self)
        self.bet_frame.grid(row=2, column=0, columnspan=6, pady=10)
        ttk.Label(self.bet_frame, text='Bet Amount: ').pack(side='left', padx=5)
        self.bet_input = ttk.Entry(self.bet_frame, width=10, justify='center')
        self.bet_input.pack(side='left', padx=5)
        self.start_btn = ttk.Button(self.bet_frame, text='Start Game', command=self.start_game)
        self.start_btn.pack(side='left', padx=5)
        
        # Grid Frame
        self.grid_frame = ttk.Frame(self)
        # Don't grid it yet, hide it until bet is placed
        # self.grid_frame.grid(row=3, column=0, columnspan=6, pady=20)
        
        for i in range(9):
            btn = tk.Button(self.grid_frame, width=8, height=4, bg='gray', state='disabled',
                            command=lambda idx=i: self.on_block_click(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Message/Action Frame
        self.msg_frame = ttk.Frame(self)
        self.msg_frame.grid(row=4, column=0, columnspan=6, pady=10)
        self.status_label = ttk.Label(self.msg_frame, text='', font=('Arial', 14, 'bold'))
        self.status_label.pack(pady=5)
        
        self.continue_btn = ttk.Button(self.msg_frame, text='Continue', command=self.next_round)
        self.stop_btn = ttk.Button(self.msg_frame, text='Stop & Claim', command=self.cash_out)
        
        self.back_btn = ttk.Button(self, text='Back', command=self.back)
        self.back_btn.grid(row=5, column=0, pady=20, padx=5)
        
        self.about_btn = ttk.Button(self, text='About Game', command=self.about)
        self.about_btn.grid(row=5, column=3, pady=20, padx=5)

    def update_points(self):
        self.point_label.config(text='{}'.format('{:.2f}'.format(float(UserInfo[UserID]['point']))))

    def start_game(self):
        try:
            amt = round(float(self.bet_input.get()), 2)
        except ValueError:
            CustomMessageBox('Error', 'Please enter a valid number!')
            return
            
        if amt <= 0:
            CustomMessageBox('Error', 'Bet amount must be greater than 0!')
            return
            
        if amt > UserInfo[UserID]['point']:
            CustomMessageBox('Error', 'You do not have enough points for this bet!')
            return
            
        self.betamt = amt
        UserInfo[UserID]['point'] -= self.betamt
        self.update_points()
        
        self.start_btn.config(state='disabled')
        self.bet_input.config(state='disabled')
        self.back_btn.config(state='disabled')
        
        # Show the 9 blocks!
        self.grid_frame.grid(row=3, column=0, columnspan=6, pady=20)
        
        self.sequence_length = 1
        self.next_round_logic()
        
    def next_round(self):
        self.sequence_length += 1
        self.next_round_logic()

    def next_round_logic(self):
        self.continue_btn.pack_forget()
        self.stop_btn.pack_forget()
        self.status_label.config(text=f'Round {self.sequence_length}: Memorize the sequence...', foreground='blue')
        self.sequence = [random.randint(0, 8) for _ in range(self.sequence_length)]
        self.player_sequence = []
        self.playing = False
        
        for btn in self.buttons:
            btn.config(state='disabled', bg='gray')
            
        self.after(500, lambda: self.show_sequence(0))
        
    def show_sequence(self, idx):
        if idx < len(self.sequence):
            block_idx = self.sequence[idx]
            self.buttons[block_idx].config(bg='yellow')
            self.after(1000, lambda: self.hide_block_and_next(block_idx, idx))
        else:
            self.status_label.config(text='Your turn! Click the blocks in order.', foreground='black')
            self.playing = True
            for btn in self.buttons:
                btn.config(state='normal', bg='gray')

    def hide_block_and_next(self, block_idx, sequence_idx):
        self.buttons[block_idx].config(bg='gray')
        self.after(200, lambda: self.show_sequence(sequence_idx + 1))

    def on_block_click(self, idx):
        if not self.playing:
            return
            
        self.player_sequence.append(idx)
        current_step = len(self.player_sequence) - 1
        
        if self.player_sequence[current_step] != self.sequence[current_step]:
            # Wrong!
            self.playing = False
            self.status_label.config(text='Wrong Sequence! You lose.', foreground='red')
            for btn in self.buttons:
                btn.config(state='disabled', bg='gray')
            self.buttons[idx].config(bg='red')
            self.reset_ui()
            return
            
        # Highlight momentarily to show it was clicked
        self.buttons[idx].config(bg='green')
        self.after(200, lambda: self.buttons[idx].config(bg='gray'))
            
        if len(self.player_sequence) == len(self.sequence):
            # Sequence completed correctly
            self.playing = False
            for btn in self.buttons:
                btn.config(state='disabled')
                
            multiplier = self.multipliers.get(self.sequence_length, 100)
            potential_win = round(self.betamt * multiplier, 2)
            
            if self.sequence_length == 9:
                self.status_label.config(text=f'Max Level Reached! You won {potential_win} points!', foreground='green')
                UserInfo[UserID]['point'] += potential_win
                self.update_points()
                self.reset_ui()
            else:
                self.status_label.config(text=f'Correct! Claim {potential_win} pts or Continue?', foreground='green')
                self.continue_btn.pack(side='left', padx=10, pady=10)
                self.stop_btn.pack(side='left', padx=10, pady=10)

    def cash_out(self):
        multiplier = self.multipliers.get(self.sequence_length, 1)
        win_amt = round(self.betamt * multiplier, 2)
        UserInfo[UserID]['point'] += win_amt
        self.update_points()
        self.status_label.config(text=f'You cashed out {win_amt} points!', foreground='green')
        self.continue_btn.pack_forget()
        self.stop_btn.pack_forget()
        self.reset_ui()

    def reset_ui(self):
        numpy.save('db.npy', UserInfo)
        self.start_btn.config(state='normal')
        self.bet_input.config(state='normal')
        self.back_btn.config(state='normal')
        # Hide the blocks again for a new game
        self.grid_frame.grid_forget()
        
    def about(self):
        msg = (
            "Memorize the block sequence!\n"
            "Payout Multipliers:\n"
            "Level 1: 0.8x bet\n"
            "Level 2: 1x bet\n"
            "Level 3: 1.2x bet\n"
            "Level 4: 1.5x bet\n"
            "Level 5: 2x bet\n"
            "Level 6: 3x bet\n"
            "Level 7: 5x bet\n"
            "Level 8: 10x bet\n"
            "Level 9: 100x bet\n"
        )
        CustomMessageBox('About Memorize Game', msg)

    def back(self):
        Memorize_Frame.destroy(self)
        Main_Frame(app)


class ChangePwd_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Change Password',font=('Arial',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=3,padx=10,pady=100)
        self.label2 = ttk.Label(self,text='User ID')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.input1 = ttk.Entry(self,width=30,justify='center')
        self.input1.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='Old Password')
        self.label3.grid(row=2,column=0,padx=5,pady=5)
        self.input2 = ttk.Entry(self,width=30,justify='center',show='*')
        self.input2.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='New Password')
        self.label4.grid(row=3,column=0,padx=5,pady=5)
        self.input3 = ttk.Entry(self,width=30,justify='center',show='*')
        self.input3.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        self.label5 = ttk.Label(self,text='Re Enter')
        self.label5.grid(row=4,column=0,padx=5,pady=5)
        self.input4 = ttk.Entry(self,width=30,justify='center',show='*')
        self.input4.grid(row=4,column=1,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Change Password',width=15,command=self.change)
        self.button1.grid(row=5,column=2,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Back',width=7,command=self.back)
        self.button2.grid(row=6,column=0,padx=5,pady=100)

    def back(self):
        ChangePwd_Frame.destroy(self)
        Login_Frame(app)

    def change(self):
        id = self.input1.get()
        oldpwd = str(self.input2.get())
        new1 = str(self.input3.get())
        new2 = str(self.input4.get())
        if id in UserInfo:
            if oldpwd == UserInfo[id]['pwd']:
                if new1 == new2:
                    UserInfo[id]['pwd']=new1
                    CustomMessageBox(title='Success',message='Password successfully changed.')
                    ChangePwd_Frame.destroy(self)
                    ChangePwd_Frame(app)
                else:
                    CustomMessageBox(title='Error!!',message='New Passwords Must be SAME.')
                    ChangePwd_Frame.destroy(self)
                    ChangePwd_Frame(app)
            else:
                CustomMessageBox(title='Error!!',message='Old Password is Wrong.')
                ChangePwd_Frame.destroy(self)
                ChangePwd_Frame(app)
        else:
            CustomMessageBox(title='Error!!',message='User ID not found.')
            ChangePwd_Frame.destroy(self)
            ChangePwd_Frame(app)

class DB_loginFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Welcome From Database!!',font=('Arial',30,'bold'))
        self.label1.grid(row=0,column=0,padx=10,pady=100,columnspan=3)
        self.label2 = ttk.Label(self,text='Username')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.id = ttk.Entry(self,show='*',justify='center',width=40)
        self.id.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='Password')
        self.label3.grid(row=2,column=0,padx=5,pady=5)
        self.pwd = ttk.Entry(self,show='*',justify='center',width=40)
        self.pwd.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='login',width=20,command=self.login)
        self.button1.grid(row=3,column=2,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Back',width=7,command=self.back)
        self.button2.grid(row=4,column=0,padx=5,pady=100)


    def login(self):
        db_id = self.id.get()
        db_pwd = self.pwd.get()
        if db_id == 'admin':
            if db_pwd == 'nimda':
                DB_loginFrame.destroy(self)
                DataBase_Frame(app)
            else:
                CustomMessageBox(title='Error!!',message='Wrong DataBase Password!')
        else:
            CustomMessageBox(title='Error!!!!',message='Wrong DataBase ID!')

    def back(self):
        DB_loginFrame.destroy(self)
        Welcome_Frame(app)

class DataBase_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.button1 = ttk.Button(self,text='Create New User',width=30,command=self.createUID)
        self.button1.grid(row=0,column=0,padx=10,pady=30,ipady=30)
        self.button2 = ttk.Button(self,text='Recharge Points',width=30,command=self.rechargeBtn)
        self.button2.grid(row=1,column=0,padx=10,pady=30,ipady=30)
        self.button3 = ttk.Button(self,text='Delete UserID',width=30,command=self.deleteUID)
        self.button3.grid(row=2,column=0,padx=10,pady=30,ipady=30)
        self.button4 = ttk.Button(self,text='Show User ID info',width=30,command=self.showuid)
        self.button4.grid(row=3,column=0,padx=10,pady=30,ipady=30)
        self.button5 = ttk.Button(self,text='Back',command=self.back)
        self.button5.grid(row=4,column=0,padx=5,pady=20)

    def createUID(self):
        DataBase_Frame.destroy(self)
        Create_NewUserID_Frame(app)

    def rechargeBtn(self):
        DataBase_Frame.destroy(self)
        RechargePoints_Frame(app)

    def deleteUID(self):
        DataBase_Frame.destroy(self)
        Delete_UserID_Frame(app)

    def showuid(self):
        DataBase_Frame.destroy(self)
        Show_UID_Info_Frame(app)

    def back(self):
        DataBase_Frame.destroy(self)
        Welcome_Frame(app)

class Create_NewUserID_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Create UserID',font=('Arial',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=5,pady=50)
        self.label2 = ttk.Label(self,text='UserID')
        self.label2.grid(row=1,column=0,padx=5,pady=6)
        self.input1 = ttk.Entry(self,width=20,justify='center')
        self.input1.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='Password')
        self.label3.grid(row=2,column=0,padx=5,pady=5)
        self.input2 = ttk.Entry(self,show='*',justify='center',width=20)
        self.input2.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='Point')
        self.label4.grid(row=3,column=0,padx=5,pady=5)
        self.input3 = ttk.Entry(self,justify='center',width=20)
        self.input3.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Create',command=self.create)
        self.button1.grid(row=4,column=2,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Back',command=self.back)
        self.button2.grid(row=5,column=0,padx=5,pady=100)

    def create(self):
        UID = self.input1.get()
        pwd = self.input2.get()
        point = self.input3.get()
        if UID in UserInfo:
            CustomMessageBox(title='Error!!',message='UserID is already Exist.')
        else:
            try:
                int(point)
                UserInfo[UID]={'pwd':pwd,'point':int(point)}
                CustomMessageBox(title='Success',message='UserID : {}\nPassword : {}\nPoint : {}\nCreated!'.format(UID,pwd,point))
            except:
                CustomMessageBox(title='Error Input!!',message='Point Should be integer.')


    def back(self):
        Create_NewUserID_Frame.destroy(self)
        DataBase_Frame(app)

class RechargePoints_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Recharge Points',font=('Arial',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=10,pady=100)
        self.label2 = ttk.Label(self,text='UserID')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.userIdvar = tk.StringVar()
        self.userId = list(UserInfo.keys())
        self.userIdmenu = ttk.Combobox(self,textvariable=self.userIdvar,values=self.userId,state='readonly')
        self.userIdmenu.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
        self.userIdmenu.set(self.userId[0])
        self.label3 = ttk.Label(self,text='Enter Points')
        self.label3.grid(row=2,column=0,padx=5,pady=5)
        self.point = ttk.Entry(self,justify='center',width=20)
        self.point.grid(row=2,column=1,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Add Point',width=30,command=self.addPwtBtn)
        self.button1.grid(row=3,column=0,columnspan=2,padx=5,pady=5,ipady=5)
        self.button2 = ttk.Button(self,text='Back',command=self.back)
        self.button2.grid(row=4,column=0,padx=5,pady=100)


    def addPwtBtn(self):
        userId = self.userIdvar.get()
        addpoint = self.point.get()
        point = UserInfo[userId]['point']
        try:
            int(addpoint)
            if int(addpoint) < 0 or len(addpoint) > 18:
                CustomMessageBox(title='Error!!',message='Point should be positive or less than 18 digit.')
            else:
                x = point + int(addpoint)
                UserInfo[userId]['point'] = x
                CustomMessageBox(title='Successful',message='{} points add to UserID :{}\nTotal point is {}'.format(addpoint,userId,x))
        except:
            CustomMessageBox(title='Error!!',message='Points Should Be Number')
            RechargePoints_Frame.destroy(self)
            RechargePoints_Frame(app)

    def back(self):
        RechargePoints_Frame.destroy(self)
        DataBase_Frame(app)

class Delete_UserID_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Delete UserID',font=('Arial',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=10,pady=50)
        self.label2 = ttk.Label(self,text='Choose User ID')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.userIdvar = tk.StringVar()
        self.userId = list(UserInfo.keys())
        self.userIdmenu = ttk.Combobox(self,textvariable= self.userIdvar,values= self.userId,state='readonly')
        self.userIdmenu.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
        self.userIdmenu.set(self.userId[0])
        self.button1 = ttk.Button(self,text='Delete User',width=30,command=self.deleteUID)
        self.button1.grid(row=2,column=1,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Back',command=self.back)
        self.button2.grid(row=3,column=0,padx=5,pady=100)

    def back(self):
        Delete_UserID_Frame.destroy(self)
        DataBase_Frame(app)

    def deleteUID(self):
        id = self.userIdvar.get()
        del UserInfo[id]
        CustomMessageBox(title='Success',message='User ID : "{}" is \nsuccessfully Deleted'.format(id))
        Delete_UserID_Frame.destroy(self)
        Delete_UserID_Frame(app)

class Show_UID_Info_Frame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Show User Info',font=('Arial',20,'bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=10,pady=100)
        self.label2 = ttk.Label(self,text='User ID')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.userIdvar = tk.StringVar()
        self.userId = list(UserInfo.keys())
        self.userIdmenu = ttk.Combobox(self,textvariable= self.userIdvar,values= self.userId,state='readonly')
        self.userIdmenu.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        self.userIdmenu.set(self.userId[0])
        self.button1 = ttk.Button(self,text='Show Info',width=20,command=self.showid)
        self.button1.grid(row=2,column=1,padx=5,pady=5)
        self.button2 = ttk.Button(self, text='Back',width=7,command=self.back)
        self.button2.grid(row=3,column=0,padx=5,pady=100)

    def showid(self):
        id = self.userIdvar.get()
        CustomMessageBox(title='Info!!',message='User ID : {}\nPassword : {}\nPoint : {}'.format(id,UserInfo[id]['pwd'],UserInfo[id]['point']))

    def back(self):
        Show_UID_Info_Frame.destroy(self)
        DataBase_Frame(app)

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.create_menu()
        self.protocol("WM_DELETE_WINDOW", self.save_user_info_and_exit)
        Welcome_Frame(self)

    def configure_window(self):
        self.geometry('500x700')
        self.resizable(False, False)
        self.title('Mini Game')

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar)
        theme = tk.Menu(menubar)
        menubar.add_cascade(label='File', menu=file_menu, underline=0)
        menubar.add_cascade(label='Theme',menu=theme,underline=0)
        file_menu.add_command(label='About', command=self.show_about)
        file_menu.add_command(label='Exit', command=self.save_user_info_and_exit)
        theme.add_command(label='Sun Valley Light',command=self.sv_light_theme)
        theme.add_command(label='Sun Valley Dark',command=self.sv_dark_theme)
        theme.add_command(label='Clam',command=self.clam)
        theme.add_command(label='Classic',command=self.classic)
        
    def sv_light_theme(self):
        sv_ttk.set_theme('light')
        
    def sv_dark_theme(self):
        sv_ttk.set_theme('dark')
        
    def clam(self):
        ttk.Style().theme_use('clam')
        
    def classic(self):
        ttk.Style().theme_use('classic')
    
    def show_about(self):
        CustomMessageBox('About Us','Free for everyone!\nIf anything advices or report\ncontact to "pyaasonehtoo@gmail.com".')

    def save_user_info_and_exit(self):
        numpy.save('db.npy', UserInfo)
        sys.exit()

if __name__ == '__main__':
    app = Main()
    app.mainloop()