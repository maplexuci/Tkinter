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

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes and Close connection
    commit_and_close(conn)


# Create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Text Boxe Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

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

# Create submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Query Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


root.mainloop()
