from tkinter import *

class Create_account:
    def __init__(self):
      screenCreateAccount = Tk()
      self.screenCreateAccount = screenCreateAccount
      rib = StringVar()
      email = StringVar()
      Lastname = StringVar()
      firstName = StringVar()
      confirmPassword = StringVar()
      self.rib = rib
      self.email = email
      self.lastName = lastName
      self.firstName = firstName
      self.confirmPassword = confirmPassword

    def field_first_name(self):
    
        self.firstName.set("")

        frameFirstName = Frame(self.screenCreateAccount)
        labelFirstName = Label(frameFirstName,text = "Prénom:")
        entryFirstName = Entry(frameFirstName,textvariable = self.firstName)

        frameFirstName.pack()
        labelFirstName.pack()
        entryFirstName.pack()

    def field_last_name(self):

        self.lastName.set("")

        frameLastName = Frame(self.screenMenu)
        labelLastName = Label(frameLastName,text = "Nom:")
        entryLastName = Entry(frameLastName,textvariable = self.lastName)

        frameLastName.pack()
        labelLastName.pack()
        entryLastName.pack()

    def field_email(self):

        self.email.set("")

        frameEmail = Frame(self.screenCreateAccount)
        labelEmail = Label(frameEmail,text = "Email:")
        entryEmail = Entry(frameEmail,textvariable = self.email)

        frameEmail.pack()
        labelEmail.pack()
        entryEmail.pack()
    
    

    def field_confirm_password(self):

        self.confirmPassword.set("")

        frameConfirmPassword = Frame(self.screenCreateAccount)
        labelConfirmPassword = Label(framePassword,text = "Confirme passeport:")
        entryConfirmPassword = Entry(framePassword,textvariable = self.confirmPassword)

        labelConfirmPassword.pack()
        entryConfirmPassword.pack()
        frameConfirmPassword.pack()

    def field_rib(self):

        self.rib.set("")

        frameRib = Frame(self.screenCreateAccount)
        labelRib = Label(frameRib,text = "Rib:")
        entryRib = Entry(frameRib,textvariable = self.rib)

        frameRib.pack()
        labelRib.pack()
        entryRib.pack()

    def show_create_account(self):
        self.field_first_name()
        self.field_last_name()
        self.field_email()
        self.field_confirm_password
        self.field_rib()
