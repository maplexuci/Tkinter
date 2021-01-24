from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")


def create_connection(path_to_db_file):
    """ Create a database connection to a SQLite database
    :param path_to_db_file: path directory to the database file, including the file name.
    :return: Connection object or None
    """
    conn = None
    try:
        # Create a database or connect ot one
        conn = sqlite3.connect(path_to_db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_cursor(conn):
    """ Create a cursor for the a connection object 'conn'.

    Args:
        conn ([type]): A connection object to a database
    """
    c = conn.cursor()
    return c


def commit_and_close(conn):
    """ Commit changes to the database and close the database

    Args:
        conn ([type]): A connection object to a database
    """
    conn.commit()
    conn.close()
    return


def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement

    Args:
        conn: Connection object
        create_table_sql: a CREATE TABLE statement
        return:
    """
    try:
        c = create_cursor(conn)
        # Create table
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


# CREATE TABLE expression
address_table = """CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
    """

# Create the table which can be refered in the functions
conn = create_connection("files/address_book.db")
create_table(conn, address_table)


def delete():
    # Create a database or connect ot one
    conn = create_connection("files/address_book.db")
    # Create a cursor
    c = create_cursor(conn)

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    # Commit changes and Close connection
    commit_and_close(conn)


def submit():
    # Create a database or connect ot one
    conn = create_connection("files/address_book.db")
    # Create a cursor
    c = create_cursor(conn)

    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
              }
              )

    # Commit changes and Close connection
    commit_and_close(conn)

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Create a database or connect ot one
    conn = create_connection("files/address_book.db")
    # Create a cursor
    c = create_cursor(conn)

    c.execute("SELECT *, oid FROM addresses") # 'oid' will return the ID for each record in the end.
    records = c.fetchall()
    print(records)

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes and Close connection
    commit_and_close(conn)


def edit():
    editor = Tk()
    editor.title("Record Editor")
    editor.iconbitmap('images/icon.ico')
    editor.geometry("400x400")

    # Create a database or connect ot one
    conn = create_connection("files/address_book.db")
    # Create a cursor
    c = create_cursor(conn)

    record_id = select_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id) 
    records = c.fetchall()

    # Create Text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Boxe Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop over the record and put the content in the Entry box
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a Save Button to save edited record
    edit_btn = Button(editor, text="Save Records", command=edit)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=130)


# Create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

select_box = Entry(root, width=30)
select_box.grid(row=8, column=1, pady=5)

# Create Text Boxe Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

select_label = Label(root, text="Select ID")
select_label.grid(row=8, column=0, pady=5)


# Create submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Query Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Create a delete Button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

# Create an Update Button
edit_btn = Button(root, text="Edit Records", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

root.mainloop()
