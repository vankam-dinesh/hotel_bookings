
USE hotel_db;

-- Step 2: Create the bookings table
CREATE TABLE IF NOT EXISTS bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    room_type VARCHAR(50) NOT NULL
);