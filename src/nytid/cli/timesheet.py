import csv
import config
from nytid.signup import hr
from nytid.signup import sheets
import operator
import sys

def to_hours(td):
    return td.total_seconds()/60/60

def summarize_user(user, course_events):
    csvout = csv.writer(sys.stdout)

    hours = to_hours(hr.hours_per_TA(course_events)[user])

    csvout.writerow([f"{user}@kth.se", "Total (inkl förberedelsetid): ",
                     f"{round(hours, 2)} h", f"{round(hours*150)} kr"])

    start_idx = sheets.SIGNUP_SHEET_HEADER.index("Start")
    end_idx = sheets.SIGNUP_SHEET_HEADER.index("End")
    type_idx = sheets.SIGNUP_SHEET_HEADER.index("Event")

    events = sheets.filter_events_by_TA(user, sorted(course_events,
            key=operator.itemgetter(start_idx)))
    events = filter(lambda x: user in sheets.get_booked_TAs_from_csv(x)[0], 
                    events)
    events = list(map(lambda x: x[0:len(sheets.SIGNUP_SHEET_HEADER)] + [user], 
                      events))

    for event, hours in hr.hours_per_event(events).items():
        csvout.writerow(["", event, f"{round(to_hours(hours), 2)} h"])

    csvout.writerow([])

    for event in events:
        csvout.writerow(["", event[start_idx].split()[0], event[type_idx]])

    csvout.writerow([])
    csvout.writerow([])


course_events = []

for course, url in config.SIGNUP.items():
    course_events += sheets.read_signup_sheet_from_url(url)

csvout = csv.writer(sys.stdout)
csvout.writerow(["Tidrapport"])
csvout.writerow([])

for user in hr.hours_per_TA(course_events):
    summarize_user(user, course_events)

csvout.writerow([])
csvout.writerow(["Kontering:"])
csvout.writerow([])
csvout.writerow([])
csvout.writerow([])
csvout.writerow([])
csvout.writerow([])
csvout.writerow([])
csvout.writerow([])
csvout.writerow(["Signatur", "Avdelningschef", "", "Kursansvarig"])
