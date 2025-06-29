import tkinter as tk
from tkinter import ttk, OptionMenu, StringVar
from scraper import scraping




def submit():
    '''
    handles the event when submit button is clicked
    '''
    # get the year input
    user_input = entry.get()
    # get the category input, either drivers or team
    selected_category = categories.get()
    # scrap the webpage for the relevant information
    result_dict = scraping(user_input, selected_category)

    # clear error message displayed
    error_label.config(text='')

    # handle case there year is missing or is not valid
    if result_dict == None:
        error_label.config(text='Missing input')
    elif result_dict == False:
        error_label.config(text='Not a valid year')
    else:
        # update the table if there is a valid result
        update_table(result_dict, selected_category)



def update_table(result_dict, selected_category):
    '''
    update the table displayed on the GUI

    input:
        - result_dict: the dictionary containing the driver or team results
        - selected_category: the selected category, either drivers or team
    '''
    
    if selected_category == 'drivers':
        # hide the team table and display the driver table 
        team_table.pack_forget() 
        driver_table.pack() 
        
        # clear the existing rows and readjust the table height
        driver_table.delete(*driver_table.get_children())
        driver_table.config(height=len(result_dict))

        # insert driver's information into the table 
        for key, values in result_dict.items():
            driver_table.insert('', 'end', values=(key, values['driver'], values['team'], values['points']))
    
    elif selected_category == 'team':
        # hide the driver table and show the team table
        driver_table.pack_forget()
        team_table.pack()

        # clear the existing rows and readjust the table height
        team_table.delete(*team_table.get_children())
        team_table.config(height=len(result_dict))

        # insert team's information into the table 
        for key, values in result_dict.items():
            team_table.insert('', 'end', values=(key, values['team'], values['points']))

    


# create the main GUI window
window = tk.Tk()
window.geometry('1200x800')
window.configure(bg='light blue')
window.title('F1 Result Table')

# title label
title_label = tk.Label(window, text='F1 Results Table')
title_label.configure(font=('ariel', 30), bg='light blue')
title_label.pack(pady=(15,10))

# instructional label
entry_label = tk.Label(window, text='Select a category and enter a year below')
entry_label.configure(font=('ariel', 12), bg='light blue')
entry_label.pack()

# input box for the year input
entry = tk.Entry(width = 40)
entry.config(font=('ariel', 10))
entry.pack(pady=(0, 10))

# dropdown box to choose a category, either drivers, teams or races
# note: races category has not been implemented yet and is currently not functional
categories = StringVar()
drop = OptionMenu(window, categories, 'drivers', 'team', 'races')
categories.set('drivers')
drop.config(font=('ariel',12))
drop.pack(pady=(0, 10))

# create submit button
submit = tk.Button(window, text='submit', command=submit)
submit.pack()

# create error label, set to blank for initial setup 
error_label = tk.Label(window, text='')
error_label.pack(pady=(10,5))
error_label.configure(bg='light blue', fg='red', font=('ariel', 15))

# table for drivers result
driver_table = ttk.Treeview(window, columns=('Position', 'Driver', 'Team', 'Points'), show='headings')
driver_table.heading('Position', text='Position')
driver_table.heading('Driver', text='Driver')
driver_table.heading('Team', text='Team')
driver_table.heading('Points', text='Points')

driver_table.column('Position', width=65, anchor=tk.CENTER)
driver_table.column('Driver', width=180)
driver_table.column('Team', width=230)
driver_table.column('Points', width=66) 

# table for teams result
team_table = ttk.Treeview(window, columns=('Position', 'Team', 'Points'), show='headings')
team_table.heading('Position', text='Position')
team_table.heading('Team', text='Team')
team_table.heading('Points', text='Points')

team_table.column('Position', width=65, anchor=tk.CENTER)
team_table.column('Team', width=230)
team_table.column('Points', width=66) 

# style for table row
style = ttk.Style()
style.configure("Treeview", background='#ededed')


# run the GUI window
window.mainloop()




