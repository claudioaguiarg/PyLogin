import tkinter as tk

#Arthor: Cláudio Aguiar

user_dict = {'claudio':'123'}
authorization = False
def login_verify():
    global authorization
    user_name = entry_user.get()
    entry_user.delete('0', 'end')
    user_password = entry_password.get()
    entry_password.delete('0', 'end')
    if user_name in user_dict.keys() and user_password in user_dict.values():
        authorization = True
        main.destroy()
    else:
        feedback.config(text='Username or password is wrong')
    pass

#Making a main window
main = tk.Tk()
main.title('Pylogin')
main.geometry('250x150')

title = tk.Label(text='LOGIN', font=('Arial',12, 'bold'),).place(x = 99, y = 10)

#Making user nickname area
label_user = tk.Label(main, 
                      text='Username', 
                      justify='right').place(x = 25, y = 40)
entry_user = tk.Entry(main)
entry_user.place(x = 90, y = 42)
#Making user password area
label_password = tk.Label(main, 
                          text='Password',
                          justify='left').place(x = 25, y = 65)
entry_password = tk.Entry(main, show='●')
entry_password.place(x = 90, y = 67)

#Making Buttom to send data to comparing
bgimage = tk.PhotoImage('green.jpg')
done_buttom = tk.Button(text='Done', 
                        width=6, 
                        border=2, 
                        bg='#FF6600',
                        command=login_verify).place(x=100, y=100)

#Create feedback
feedback = tk.Label(main,
                    text = '',
                    font =('Arial',8, 'bold'), 
                    foreground='red', 
                    justify='center')
feedback.place(relx=0.13, y = 130)

main.mainloop()

if authorization == True:
        painel = tk.Tk()
        painel.geometry('400x300')

        title_logged_area = tk.Label(text = 'Logged Area', font = ('Arial',15, 'bold')).pack()

        painel.mainloop()

