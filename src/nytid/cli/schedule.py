import arrow
from config import COURSES, SIGNUP
import ics.icalendar
import nytid.schedules as sched
import nytid.schedules.utils as utils
import sys

def generate_schedule():
    """Generates schedule, uses sys.args, returns schedule
    as ics.icalendar.Calendar object"""

    schedule = ics.icalendar.Calendar()

    for course, url in SIGNUP.items():
        schedule.events |= set(map(utils.EventFromCSV,
            utils.read_signup_sheet_from_url(url)))

    return schedule


def main():
    """Main program"""
    schedule = generate_schedule()

    if len(sys.argv) > 1:
        try:
            time_limit = arrow.get(2022, 8, 29).shift(weeks=+int(sys.argv[1]))
        except ValueError as err:
            print(f"{sys.argv[0]}: {err}: "
                  f"first argument must be the number of weeks to print",
                  file=sys.stderr)
            sys.exit(1)

    first = True
    for event in schedule.timeline:
        if first:
            first = False
            current_week = event.begin.isocalendar()[1]
        elif event.begin.isocalendar()[1] != current_week:
            current_week = event.begin.isocalendar()[1]
            print(end="\n\n")

        try:
            if event.begin > time_limit:
                break
        except NameError:
            pass

        print(sched.format_event_short(event) + "; " +
                ", ".join([attendee.email for attendee in event.attendees]))


if __name__ == "__main__":
    main()
