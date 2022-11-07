from config import COURSES, SIGNUP
import config
from nytid.signup import utils
from nytid.signup import sheets
from nytid.signup import hr

def to_hours(td):
    return td.total_seconds()/60/60

def needed_TAs(event):
    if "Övning" in event.name and event.begin.weekday() in [3, 4]:
        return 1
    elif "laboration" in event.name or "Laboration" in event.name:
        return event.description.split().count("grupp")
    return utils.needed_TAs(event)

for course, url in COURSES.items():
    sheets.generate_signup_sheet(course, url, needed_TAs, lambda x: x)

booked = []

for course, url in SIGNUP.items():
    booked += sheets.read_signup_sheet_from_url(url)

h_per_student = hr.hours_per_student(booked)

print("# dasak")

for event, hours in h_per_student.items():
    print(f"{event}: {to_hours(hours):.2f} h/student")

print(f"Booked: {to_hours(hr.total_hours(booked)):.2f} h "
        f"({to_hours(hr.max_hours(booked)):.2f} h)\n")


print("# Amanuenser")
amanuensis = hr.compute_amanuensis_data(booked,
        add_prep_time=config.add_prep_time)
for user, data in amanuensis.items():
    if not user:
        continue
    print(f"{user}: {data[2]:.2f} h, "
          f"{100*hr.compute_percentage(*data):.1f}%: "
          f"{data[0].format('YYYY-MM-DD')}--{data[1].format('YYYY-MM-DD')}")

print()
print("# Hourly")
for user, hours in hr.hours_per_TA(booked, 
                                   add_prep_time=config.add_prep_time).items():
    if not user or user in amanuensis:
        continue
    print(f"{user}: {to_hours(hours):.2f} h")


