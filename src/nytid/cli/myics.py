import arrow
from config import COURSES, SIGNUP
import functools
import ics.icalendar
from nytid.signup import sheets
import os
import sys

def add_reserve_to_title(ta, event):
    """
    Input: an event in CSV form.
    Ouput: the same CSV data, but with title prepended "RESERVE: " if TA is 
    among the reserves.
    """
    _, reserves = sheets.get_booked_TAs_from_csv(event)
    if ta in reserves:
        event[0] = "RESERVE: " + event[0]

    return event

def generate_schedule():
    """Generates schedule, uses sys.args or USER environment variable, returns 
    schedule as ics.icalendar.Calendar object"""

    schedule_csv = []

    for course, url in SIGNUP.items():
        schedule_csv += sheets.read_signup_sheet_from_url(url)

    if len(sys.argv) < 2:
        user = os.environ["USER"]
    else:
        user = sys.argv[1]

    schedule_csv = sheets.filter_events_by_TA(user, schedule_csv)
    schedule_csv = map(functools.partial(add_reserve_to_title, user), 
            schedule_csv)

    schedule = ics.icalendar.Calendar()
    schedule.events |= set(map(sheets.EventFromCSV, schedule_csv))

    return schedule


def main():
    """Main program"""
    print(generate_schedule())


if __name__ == "__main__":
    main()
