import arrow
import canvasapi
import canvaslms.cli
import csv
import config
from nytid.signup import hr
from nytid.signup import sheets
import ladok3.kth
import operator
import os
import sys

def to_hours(td):
    return td.total_seconds()/60/60

def summarize_user(user, course_events):
    hours = to_hours(hr.hours_per_TA(course_events)[user])

    student = ls.get_student(get_ladok_id(f"{user}@kth.se"))

    csvout.writerow([student.personnummer, student.last_name, 
                     student.first_name, f"{user}@kth.se"])
    csvout.writerow([])

    start_idx = sheets.SIGNUP_SHEET_HEADER.index("Start")
    end_idx = sheets.SIGNUP_SHEET_HEADER.index("End")
    type_idx = sheets.SIGNUP_SHEET_HEADER.index("Event")

    events = sheets.filter_events_by_TA(user, sorted(course_events,
            key=operator.itemgetter(start_idx)))
    events = filter(lambda x: user in sheets.get_booked_TAs_from_csv(x)[0], 
                    events)
    events = list(map(lambda x: x[0:len(sheets.SIGNUP_SHEET_HEADER)] + [user], 
                      events))

    for event in events:
        end = arrow.get(event[end_idx])
        start = arrow.get(event[start_idx])
        time = hr.round_time(
                    hr.add_prep_time(end-start, event[type_idx],
                                     date=start.date()))

        csvout.writerow(["",
                         event[start_idx].split()[0], event[type_idx],
                         f"{to_hours(time)} h",
                         f"{to_hours(time)*150} kr"
                        ])

    csvout.writerow([])
    csvout.writerow(["", "Total", "", "",
                     f"{round(hours, 2)} h", f"{round(hours*150)} kr"])
    csvout.writerow([])
    csvout.writerow([])
    csvout.writerow([])
    csvout.writerow([])

def get_ladok_id(user):
    for student in students:
        if student.login_id == user:
            return student.integration_id

cs = canvasapi.Canvas(os.environ["CANVAS_SERVER"], os.environ["CANVAS_TOKEN"])
course = next(canvaslms.cli.courses.filter_courses(cs, "dasak22"))
students = list(course.get_users())

ls = ladok3.kth.LadokSession(os.environ["KTH_LOGIN"], os.environ["KTH_PASSWD"])

course_events = []

for course, url in config.SIGNUP.items():
    course_events += sheets.read_signup_sheet_from_url(url)

csvout = csv.writer(sys.stdout, delimiter="\t")
csvout.writerow(["Tidrapport"])
csvout.writerow([])

if len(sys.argv) > 1:
    for user in sys.argv[1:]:
        summarize_user(user, course_events)
else:
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
