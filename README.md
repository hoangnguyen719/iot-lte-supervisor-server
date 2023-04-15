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

# API Calls
### `GET` all LTE signals
/signals/

### `GET` last LTE signal
/get_last_signal/

### `GET` last `signal_count` LTE signals (optional - from S-Cell ID=`scellid`)
/get_n_signals/?scellid=`scellid`&signal_count=`signal_count`

### `GET` last 1 hour of LTE signals (optional - from S-Cell ID=`scellid`)
/get_1hr_signals/?scellid=`scellid`

### `GET` all LTE cells' info
/cells/

### `GET` most recent LTE cell's info
/get_last_cell/

### `GET` last LTE cell change's timestamp
/get_last_cell_change_timestamp/

### `GET` current frequency
/get_current_frequency/

### `POST` Update signal
/post_signal/<br>
Request body (`required`)<br>

```
# Example value
{
  "pcellid": "string",
  "scellid": "string",
  "mcc": "string",
  "mnc": "string",
  "rsrq": 0,
  "rsrp": 0
}
```

### `POST` Update frequency
/update_current_frequency/<br>