# junctionx-hanoi-2023-iot-newbees

Team NEWBEES' work for JunctionX Hanoi 2023 Hackathon

Create a new virtual environment:
python3 -m venv venv

Activate it:
source venv/bin/activate

pip install -r requirements.txt

Set up database:
Install postgreSQL: https://www.postgresql.org/download/

Start postgresql:
sudo service postgresql start

Set up user:
sudo -u postgres createuser fastapi-songs --pwprompt

Create test database:
sudo -u postgres psql -c "create database fastapi;"

init db:
python3 init_db.py

Run server:
uvicorn main:app --reload
