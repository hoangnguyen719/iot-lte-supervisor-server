## junctionx-hanoi-2023-iot-newbees
This is a part of the work for the [JunctionX Hanoi 2023 Hackathon](https://www.junctionxhanoi2023.com/).<br>
- Team: **NEWBEES**<br>
- Competition description: Within 48 hours, set up an IoT system to detect weak/loss of LTE 4G signal.
- Submitted product: see system architecture in image below.<figure>
  <img
  src="images/system_architecture.jpeg"
  alt="Entire System Architecture"
  width=700>
  <figcaption>
    <a href="https://docs.google.com/presentation/d/1SUfOoXLpWCnfktmx_Bo7HddxW_Sc9susIa3Cdxdg0OA/edit?usp=sharing">
      Team NEWBEES' Entire System Architecture
    </a>
  </figcaption>
</figure>

- Repo description: Set up server and database.
- Product presentation
  - PowerPoint Slides: [link to Google Drive](https://docs.google.com/presentation/d/1bPi0vrQAUJJFnyKqWmuZRpBibypFUIaYIDAKa4smMN4/edit?usp=sharing)
  - Full presentation: [link to Facebook video](https://fb.watch/j-aidbyJQP/) (from **02:03:20** to **02:23:41**)

---------

## Set-up Guidelines
### Project Setup
Go through the following steps when you **first** set up or restart the project.

Create a new virtual environment:<br>
`python3 -m venv venv`

Activate it:<br>
`source venv/bin/activate`

Install requirements<br>
`pip install -r requirements.txt`

Set up database:<br>
Install postgreSQL: https://www.postgresql.org/download/

Start postgresql:<br>
`sudo service postgresql start`

Set up user:<br>
`sudo -u postgres createuser fastapi-songs --pwprompt`

### Server Setup
Go through the following steps when you first set up the project or are re-running the server.

Create test database:<br>
`sudo -u postgres psql -c "create database fastapi;"`

init db:<br>
`python3 init_db.py`

Run server:<br>
`uvicorn main:app --reload`

---

## API Calls
#### `GET` /signals/
Get all LTE signals

#### `GET` /get_last_signal/
Get last LTE signal

#### `GET` /get_n_signals/?scellid=*{scellid}*&signal_count=*{signal_count}*
Get last `signal_count` LTE signals (optional - from S-Cell ID=`scellid`)

#### `GET` /get_1hr_signals/?scellid=*{scellid}*
Get last 1 hour of LTE signals (optional - from S-Cell ID=`scellid`)

#### `GET` /cells/
Get all LTE cells' info

#### `GET` /get_last_cell/
Get most recent LTE cell's info

#### `GET` /get_last_cell_change_timestamp/
Get last LTE cell change's timestamp

#### `GET` /get_current_frequency/
Get current frequency

#### `POST` /post_signal/
Update signal database<br>
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

### `POST` /update_current_frequency/{frequency}
Update frequency value<br>
Request body (`required`)<br>
    `frequency`: `int` new frequency