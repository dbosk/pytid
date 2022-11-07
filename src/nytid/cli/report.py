import csv
import datetime
import sys
from nytid.schedules import utils

from config import SIGNUP

def to_hours(td):
    return td.total_seconds()/60/60

if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: requires argument 'username'",
          file=sys.stderr)
    sys.exit(1)
else:
    user = sys.argv[1]

booked = []

for course, url in SIGNUP.items():
    booked += utils.read_signup_sheet_from_url(url)

amanuensis = utils.compute_amanuensis_data(booked, low_percentage=0)
data = amanuensis[user]

print(f"{user}: {data[2]:.2f} h, {100*utils.compute_percentage(*data):.1f}%: "
      f"{data[0].format('YYYY-MM-DD')}--{data[1].format('YYYY-MM-DD')}")

events = utils.filter_events_by_TA(user, booked)
events = filter(lambda x: user in utils.get_booked_TAs_from_csv(x)[0], booked)
events = list(map(lambda x: x[0:len(utils.SIGNUP_SHEET_HEADER)] + [user], 
    events))

for event, hours in utils.hours_per_event(events).items():
    print(f"{event}: {to_hours(hours)}")

print()

csvout = csv.writer(sys.stdout)

for event in events:
    date = event[1].split(" ")[0]
    start = datetime.datetime.fromisoformat(event[1])
    end = datetime.datetime.fromisoformat(event[2])
    csvout.writerow([
        event[5],
        event[0],
        date,
        hours:=utils.add_prep_time(utils.round_time(end-start), event[0]),
        to_hours(hours)*150
    ])
