from tkinter import *
import mysql.connector
import Create_account
class Menu(Create_account):

  def  __init__(self):
    screenMenu = Tk()
    self.screenMenu = screenMenu

    super.__init__(self)
    user = StringVar()
    password = StringVar()
    self.user = user
    self.password = password
    connect_db_juda_company = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "AeoN-13014",
      database = "juda_company"
    )
    self.connect_db_juda_company = connect_db_juda_company
    cursor = self.connect_db_juda_company.cursor()
    self.cursor = cursor
    
    
    

  def field_user(self):

    self.user.set("")
    frameUser = Frame(self.screenMenu)
    labelUser = Label(frameUser,text = "utilisateur:")
    entryUser = Entry(frameUser,textvariable = self.user)
    labelUser.pack()
    entryUser.pack()
    frameUser.pack()

  def field_password(self):
    self.password.set("")
    framePassword = Frame(self.screenMenu)
   # labelPassword = Label(framePassword,text = "Passeport:")
    entryPassword = Entry(framePassword,textvariable = self.password)
    #labelPassword.pack()
    entryPassword.pack()
    framePassword.pack()

  def menu_connection(self):
    frameConnection = Frame(self.screenMenu)
    buttonConnection = Button(frameConnection,text = "Se connecter.")
    frameConnection.pack()
    buttonConnection.pack()
  
  def menu_create_account(self):
    frameCreate = Frame(self.screenMenu)
    buttonCreate = Button(frameCreate,text = "Créer un compte.",command = super.show_create_account())
    frameCreate.pack()
    buttonCreate.pack()
  
  def menu_exit(self):
    frameExit = Frame(self.screenMenu)
    buttonExit = Button(frameExit,text ="Quitter.",command = self.screenMenu.quit)
    frameExit.pack()
    buttonExit.pack()
    

  def show(self):
    title = Label(self.screenMenu,text = "Juda Company")
    title.pack()
    self.field_user()
    self.field_password()
    self.menu_connection()
    self.menu_create_account()
    self.menu_exit()
    self.screenMenu.minsize(300,200)
    self.screenMenu.title("Bienvenue à Juda Company")
    self.screenMenu.mainloop()
    

judaCompany = Menu()
judaCompany.show()

