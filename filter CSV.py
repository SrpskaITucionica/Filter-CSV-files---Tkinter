from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter import filedialog as fd
import csv

file_name = ''


def filter_data():
    letter_value = letters_combobox_var.get()
    date_value = date_entry.get()
    records_counter = 0
    data_listbox.delete(0, END)
    with open('babies_names.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if line['FirstForename'][0] == letter_value:
                if line['yr'] == date_value:
                    data_listbox.insert('end', f'Date of birth : {line["yr"]}. Child name: {line["FirstForename"]}')
                    records_counter += 1

    records_value_init = 'Records found: '
    records_label.config(text=f'{records_value_init} {records_counter}')


def filter_custom_file_data():
    field_value = fields_combobox_var.get()
    records_counter = 0
    row_counter = 0
    data_listbox2.delete(0, END)
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            row_counter += 1
            if row_counter != int(limit_entry.get())+1:
                data_listbox2.insert('end', f'{field_value}: {line[field_value]}')
                records_counter += 1
            else:
                records_label2.config(text='Records found: ')
                break
    records_value_init = 'Records found: '
    records_label2.config(text=f'{records_value_init} {records_counter}')




def open_file():
    keys = ''
    filetypes = (
        ('Csv files', '*.csv'),
        ('All files', '*.*')
    )

    global file_name
    file_name = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            keys = list(line.keys())
            break

        fields_combobox['values'] = keys
    print(keys)


app = Tk()
app.resizable(0, 0)
app.title('CSV File Filter')

w = 500  # width for the Tk root
h = 650  # height for the Tk root

ws = app.winfo_screenwidth()  # width of the screen
hs = app.winfo_screenheight()  # height of the screen

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))

y = 30
x = 30

notebook = Notebook(app)
first_frame = Frame(notebook)
second_frame = Frame(notebook)
notebook.add(first_frame, text='Original Frame')
notebook.add(second_frame, text='Custom Frame')
notebook.pack(expand=1, fill="both")

# ------------------------- FRAME ONE ----------------------------------

# ------------------ WIDGET VARIABLES ---------------------
letters_combobox_var = StringVar()

# -------------------- WIDGETS -----------------------------

filter_label_frame = LabelFrame(first_frame, text='Filter Options', width=440, height=150)
letters_combo_box = Combobox(filter_label_frame, textvariable=letters_combobox_var)
letter_label = Label(filter_label_frame, text='Pick a letter: ')
date_label = Label(filter_label_frame, text='Enter a date (1974 - 2020): ')
letters_combo_box['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
date_entry = Entry(filter_label_frame)
filter_button = Button(filter_label_frame, text='FILTER', width=55, bg='lightgreen', command=filter_data)
data_listbox = Listbox(first_frame, height=25, width=73)
scroll_bar = Scrollbar(first_frame, orient=VERTICAL, command=data_listbox.yview)
records_label = Label(first_frame, text='Records found: ')

letters_combo_box.state(['readonly'])
letters_combo_box.set('Select letter')
data_listbox['yscrollcommand'] = scroll_bar.set

# -------------------- WIDGET PLACEMENT -----------------------

filter_label_frame.place(x=x, y=y)
letter_label.place(x=20, y=20)
letters_combo_box.place(x=x + 80, y=20)
date_label.place(x=20, y=50)
date_entry.place(x=165, y=50)
filter_button.place(x=20, y=100)
data_listbox.place(x=x, y=190)
scroll_bar.pack(side="right", fill="y")
records_label.place(x=x, y=600)

# ------------------------------------------ FRAME TWO ------------------------------------------

fields_combobox_var = StringVar()

open_button = Button(second_frame, text='Select file', command=open_file)
filter_label_frame2 = LabelFrame(second_frame, text='Filter Options', width=440, height=100)
fields_combobox = Combobox(filter_label_frame2, textvariable=fields_combobox_var)
fields_label = Label(filter_label_frame2, text='Select field: ')
filter_button2 = Button(filter_label_frame2, text='FILTER', width=55, bg='lightgreen', command=filter_custom_file_data)
data_listbox2 = Listbox(second_frame, height=26, width=73)
records_label2 = Label(second_frame, text='Records found: ')
limit_entry = Entry(filter_label_frame2)
scroll_bar2 = Scrollbar(second_frame, orient=VERTICAL, command=data_listbox2.yview)
rows_label = Label(filter_label_frame2, text='Rows: ')

fields_combobox.set('Select field')
data_listbox2['yscrollcommand'] = scroll_bar2.set

open_button.place(x=x, y=10)
filter_label_frame2.place(x=x, y=y + 20)
fields_label.place(x=20, y=20)
fields_combobox.place(x=x + 80, y=20)
filter_button2.place(x=20, y=50)
data_listbox2.place(x=x, y=160)
records_label2.place(x=x, y=590)
limit_entry.place(x=300, y=20)
scroll_bar2.pack(side="right", fill="y")
rows_label.place(x=260, y=20)

fields_combobox.state(['readonly'])

app.mainloop()
