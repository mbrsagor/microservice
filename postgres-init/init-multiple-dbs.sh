#!/bin/sh
set -e

echo "Creating user_db, doctor_db and appointment_db..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres" <<-EOSQL
    CREATE DATABASE user_db;
    CREATE DATABASE doctor_db;
    CREATE DATABASE appointment_db;
EOSQL
echo "Databases created successfully!"
