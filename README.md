# nytid

Handle TA bookings for lab sessions, tutorials etc.

We want to turn the TimeEdit schedule into a sign-up sheet in Google Sheets 
that our TAs can use to sign up for teaching slots.
```python
import nytid.schedules.utils as utils

COURSES = {
  "DD1310": 
  "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453080.10&e=220609&enol=t&ku=29&k=1B9F3AD696BCA5C434C68950EFD376DD",
  "DD1317": 
  "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=455995.10&e=220609&enol=t&ku=29&k=BA4400E3C003685549BC65AD9EAD3DC58E"
}

for course, url in COURSES.items():
  utils.generate_signup_sheet(course, url)
```
Now we have two CSV files, `DD1310.csv` and `DD1317.csv`, in the current 
working directory that we can upload to Google Sheets. Once uploaded, we can 
use the share URL with the following functions.
```python
import nytid.schedules.utils as utils

dd1317 = utils.read_signup_sheet_from_url(utils.google_sheet_to_csv_url("https://docs.google.com/spreadsheets/d/the-share-url"))

dd1310 = utils.read_signup_sheet_from_url(utils.google_sheet_to_csv_url("https://docs.google.com/spreadsheets/d/the-share-url"))

ta_time_dd1310 = utils.hours_per_TA(dd1310)
amanuenses = utils.compute_amanuensis_data(dd1310+dd1317)
```

