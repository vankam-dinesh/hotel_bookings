
# import sqlite3

# conn = sqlite3.connect('hotel.db')
# conn.execute('''
# CREATE TABLE IF NOT EXISTS bookings (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     checkin DATE NOT NULL,
#     checkout DATE NOT NULL,
#     room_type TEXT NOT NULL
# );
# ''')
# conn.commit()
# conn.close()

# print("✅ Database and table created successfully.")