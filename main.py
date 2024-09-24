import tkinter as tk
from tkinter import ttk, OptionMenu, StringVar
from scraper import scraping




def submit():
    user_input = entry.get()
    selected_category = categories.get()
    result_dict = scraping(user_input, selected_category)

    error_label.config(text='')

    if result_dict == None:
        error_label.config(text='Missing input')
    elif result_dict == False:
        error_label.config(text='Not a valid year')
    else:
        update_table(result_dict, selected_category)



def update_table(result_dict, selected_category):
    if selected_category == 'drivers':
        team_table.pack_forget()  # Hide team table
        driver_table.pack()  # Show driver table
        
        driver_table.delete(*driver_table.get_children())
        driver_table.config(height=len(result_dict))

        for key, values in result_dict.items():
            driver_table.insert('', 'end', values=(key, values['driver'], values['team'], values['points']))
    
    elif selected_category == 'team':
        driver_table.pack_forget()  # Hide driver table
        team_table.pack()  # Show team table
        
        team_table.delete(*team_table.get_children())
        team_table.config(height=len(result_dict))

        for key, values in result_dict.items():
            team_table.insert('', 'end', values=(key, values['team'], values['points']))

    



window = tk.Tk()
window.geometry('1200x800')
window.configure(bg='light blue')
window.title('F1 Result Table')

title_label = tk.Label(window, text='F1 Results Table')
title_label.configure(font=('ariel', 30), bg='light blue')
title_label.pack(pady=(15,10))

entry_label = tk.Label(window, text='Select a category and enter a year below')
entry_label.configure(font=('ariel', 12), bg='light blue')
entry_label.pack()


entry = tk.Entry(width = 40)
entry.config(font=('ariel', 10))
entry.pack(pady=(0, 10))

categories = StringVar()
drop = OptionMenu(window, categories, 'drivers', 'team', 'races')
categories.set('drivers')
drop.config(font=('ariel',12))
drop.pack(pady=(0, 10))



submit = tk.Button(window, text='submit', command=submit)
submit.pack()

error_label = tk.Label(window, text='')
error_label.pack(pady=(10,5))
error_label.configure(bg='light blue', fg='red', font=('ariel', 15))


# table = ttk.Treeview(window, columns=('position', 'driver', 'team', 'points'), show='headings')
# table.config(height=5)
# table.pack(pady=(10, 0))
# table.heading('position', text = 'position')
# table.heading('driver', text = 'driver')
# table.heading('team', text = 'team')
# table.heading('points', text = 'points')


driver_table = ttk.Treeview(window, columns=('Position', 'Driver', 'Team', 'Points'), show='headings')
driver_table.heading('Position', text='Position')
driver_table.heading('Driver', text='Driver')
driver_table.heading('Team', text='Team')
driver_table.heading('Points', text='Points')

driver_table.column('Position', width=65, anchor=tk.CENTER)
driver_table.column('Driver', width=180)
driver_table.column('Team', width=230)
driver_table.column('Points', width=66) 


team_table = ttk.Treeview(window, columns=('Position', 'Team', 'Points'), show='headings')
team_table.heading('Position', text='Position')
team_table.heading('Team', text='Team')
team_table.heading('Points', text='Points')

team_table.column('Position', width=65, anchor=tk.CENTER)
team_table.column('Team', width=230)
team_table.column('Points', width=66) 


style = ttk.Style()
style.configure("Treeview", background='#ededed')



window.mainloop()




