from config import COURSES, SIGNUP
import csv
from nytid.signup import hr
from nytid.signup import sheets
import operator
import sys

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
    booked += sheets.read_signup_sheet_from_url(url)

amanuensis = hr.compute_amanuensis_data(booked)
data = amanuensis[user]

print(f"{user}: {data[2]:.2f} h, {100*hr.compute_percentage(*data):.1f}%: "
      f"{data[0].format('YYYY-MM-DD')}--{data[1].format('YYYY-MM-DD')}")

events = sheets.filter_events_by_TA(user, booked)
events = filter(lambda x: user in sheets.get_booked_TAs_from_csv(x)[0], booked)
events = list(map(lambda x: x[0:len(sheets.SIGNUP_SHEET_HEADER)] + [user], 
                  events))

for event, hours in hr.hours_per_event(events).items():
    print(f"{event}: {to_hours(hours)}")

print()

csvout = csv.writer(sys.stdout)

for event in events:
    csvout.writerow(event)
