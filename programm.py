
from tkinter import *
from tkinter import ttk


class Login(Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('password data base')
        self.geometry('1000x1000')
        self.create_widget()
        self.mainloop()

    def create_widget(self):
        self.label = Label(self, text='ENTER THE PASSWORD TITLE : ', font=('tahoma', 12, 'bold'))
        self.label.pack(pady=10)

        self.password = StringVar()
        self.entry = Entry(self, textvariable=self.password, font=('tahoma', 12, 'bold'))
        self.entry.pack()
        
        self.button1 = Button(self, text='LOG IN', font=('tahoma', 12, 'bold'), command=self.__check_password)
        self.button1.pack(pady=30)

    def __check_password(self):
        password = self.password.get() 

        if password == 'ccpnasa1384':
            self.destroy()
            MyApp()

class MyApp(Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('password data base')
        self.geometry('1000x1000')
        self.create_widget()
        self.mainloop()

    def create_widget(self):
        self.label = Label(self, text='ENTER THE PASSWORD TITLE : ', font=('tahoma', 12, 'bold'))
        self.label.pack(pady=10)

        self.tile_password = StringVar()
        self.entry = Entry(self, textvariable=self.tile_password, font=('tahoma', 12, 'bold'))
        self.entry.pack()

        self.label1 = Label(self, text='ENTER THE PASSWORD : ', font=('tahoma', 12, 'bold'))
        self.label1.pack(pady=10)

        self.password = StringVar()
        self.entry1 = Entry(self, textvariable=self.password, font=('tahoma', 12, 'bold'))
        self.entry1.pack()

        self.button1 = Button(self, text='SAVE PASSWORD', font=('tahoma', 12, 'bold'), command=self.__save_password)
        self.button1.pack(pady=30)

        self.label4 = Label(self, text='ENTER THE TITLE : ', font=('tahoma', 12, 'bold'))
        self.label4.pack(pady=10)

        self.title_search = StringVar()
        self.entry4 = Entry(self, textvariable=self.title_search, font=('tahoma', 12, 'bold'))
        self.entry4.pack()


        self.button4 = Button(self, text='SEARCH', font=('tahoma', 12, 'bold'), command=self.__get_passwords)
        self.button4.pack(pady=30)

        self.image = PhotoImage(file='images.png')
        self.label5 = Label(self, image=self.image)
        self.label5.pack(side='bottom')
        self.label6 = Label(self, text='Ghafar Soft Company', font=('tahoma', 12, 'bold'))
        self.label6.pack(pady=5)

    def __save_password(self):
        self.get_password_title = self.tile_password.get()
        self.get_password = self.password.get()
        
        algoritm_alfa = []
        for ch in self.get_password:
            data = ord(ch) + 2
            algoritm_alfa.append(chr(data))

        password = ''.join(algoritm_alfa)
        final_password = {'Title':self.get_password_title, 'Password':password} 
        with open('data.txt', 'a') as file:
            file.write(f'{final_password}\n')
       
        self.label3 = Label(self, text='SAVE PASSWORD SUCCESS', font=('tahoma', 12, 'bold'), background='green')
        self.label3.pack(side='bottom')
 
    def __get_passwords(self):
        self.get_title = self.title_search.get()

        with open('data.txt') as file:
            data = file.readlines()
            data_list = list(map(lambda item : eval(item.strip()), data))

        for item in data_list:
            print(item, type(item))
            if item['Title'] == self.get_title:
                algoritm_data_alfa = []
                for ch in item['Password']:
                    data = ord(ch) - 2
                    algoritm_data_alfa.append(chr(data))
                
                password = ''.join(algoritm_data_alfa) 
                
                self.label4 = Label(self, text=f'{password}', font=('tahoma', 12, 'bold'))
                self.label4.pack(pady=10)
                self.label4.after(10000, lambda : self.label4.destroy())

Login()

