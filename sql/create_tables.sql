-- Aggregated Tables
CREATE TABLE IF NOT EXISTS aggregated_transactions (
    state TEXT,
    year INTEGER,
    payment_category TEXT,
    type TEXT,
    count INTEGER,
    amount REAL,
    source_file TEXT
);



CREATE TABLE IF NOT EXISTS aggregated_user (
    state TEXT,
    year INTEGER,
    brand TEXT,
    count INTEGER,
    percentage REAL,
    registered_users INTEGER,
    app_opens INTEGER,
    source_file TEXT
);


CREATE TABLE IF NOT EXISTS aggregated_insurance (
    state TEXT,
    year INTEGER,
    insurance_type TEXT,
    count INTEGER,
    amount REAL,
    source_file TEXT
);


-- Map Tables
CREATE TABLE IF NOT EXISTS map_transaction (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    count INTEGER,
    amount REAL,
    level TEXT,
    region TEXT,
    source TEXT
);



CREATE TABLE IF NOT EXISTS map_user (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    registered_users INTEGER,
    app_opens INTEGER,
    level TEXT,
    region TEXT,
    source TEXT
);


CREATE TABLE IF NOT EXISTS map_insurance (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    level TEXT,
    region TEXT,
    source TEXT,
    count INTEGER,
    amount REAL
);


-- Top Tables
CREATE TABLE IF NOT EXISTS top_transaction (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    category TEXT,
    type TEXT,
    name TEXT,
    count INTEGER,
    level TEXT,
    region TEXT,
    amount REAL
);



CREATE TABLE IF NOT EXISTS top_user (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    district TEXT,
    category TEXT, 
    level TEXT,
    region TEXT,
    registered_users INTEGER,
    app_opens INTEGER
);


CREATE TABLE IF NOT EXISTS top_insurance (
    year INTEGER,
    quarter INTEGER,
    state TEXT,
    level TEXT,
    category TEXT,
    type TEXT,
    region TEXT,
    name TEXT,
    count INTEGER,
    amount REAL
);
