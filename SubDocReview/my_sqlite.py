# Based on https://datatofish.com/create-database-python-using-sqlite3/
# https://pythonexamples.org/python-sqlite3-check-if-table-exists/

import sqlite3
import os
DELETE_DATABASE = False
DROP_TABLE = True
POPULATE_TABLE = False
PATH = 'project/document_segments.db'

if DELETE_DATABASE:
    if os.path.exists(PATH):
        os.remove(PATH)

# Create new sqlite file.
if not os.path.exists(PATH):
    conn = sqlite3.connect(PATH)  # You can create a new database by changing the name within the quotes
    c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved
    conn.commit()
    conn.close()

with sqlite3.connect('project/document_segments.db') as conn:
    conn = sqlite3.connect('project/document_segments.db')
    c = conn.cursor()
    make_table_query = '''
                CREATE TABLE document_segment_for_db (
                id INTEGER NOT NULL,
                document_id VARCHAR(80) NOT NULL,
                line_number VARCHAR(80) NOT NULL,
                main_pii_class VARCHAR(80) NOT NULL,
                is_birth VARCHAR(80) NOT NULL,
                is_empahi VARCHAR(80) NOT NULL,
                is_heali VARCHAR(80) NOT NULL,
                is_healins VARCHAR(80) NOT NULL,
                is_medhist VARCHAR(80) NOT NULL,
                is_wre VARCHAR(80) NOT NULL,
                is_finan VARCHAR(80) NOT NULL,
                all_pii_classes VARCHAR(160) NOT NULL,
                created_at DATETIME NOT NULL,
                PRIMARY KEY (id)
            );
            '''
    drop_table_query = '''
        DROP TABLE IF EXISTS document_segment_for_db;
    '''

    if DROP_TABLE:
        c.execute(drop_table_query)
        conn.commit()

    # Check whether table exists
    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='document_segment_for_db' ''')
    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists.')
    else:
        # Create table
        c.execute(make_table_query)
        conn.commit()

    # Close the connection
    conn.close()

print('Done')