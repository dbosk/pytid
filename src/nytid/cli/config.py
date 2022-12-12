import arrow
import datetime
from nytid.signup import hr
from nytid.signup import sheets

COURSES = {
        "DD1301":
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453078.10%2C203482.9%2C203489&e=220813&enol=t&ku=29&k=525C9D88748D006E2E700F1600C9BE1D9B3"
        }

SIGNUP = {
        "DD1301": sheets.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1ac9xNFfUNsf0rXeWcgiHumNZb-7t9Ktcy_pOqCBLH3E/edit#gid=0")
        }


def add_prep_time(time, event_type,
  date=datetime.date.today(), amanuensis=False):
  """
  Input:
  - a datetime.timedelta object time,
  - a string containing the title of the event,
  - an optional date (datetime or arrow object) indicating the date of the 
    event. If no date is given, today's date is assumed, meaning the latest 
    prep-time policy will be used.
  - an optional bool indicating amanuensis employment or hourly.

  Output: the time object rounded according to KTH rules.
  """
  event_type = event_type.casefold()

  if date > arrow.Arrow(2023, 1, 1) or \
    (date > arrow.Arrow(2022, 10, 1) and not amanuensis):
    if hr.check_substrings(["laboration", "redovisning"], event_type):
      time *= 1.5
    elif "seminarium" in event_type:
      time *= 3
    elif "övning" in event_type:
      time *= 2
  else:
    if hr.check_substrings(["laboration", "redovisning"], event_type):
      time *= 1.33
    elif "seminarium" in event_type:
        time *= 3
    elif "övning" in event_type:
      time *= 2

  return time

