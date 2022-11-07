from config import COURSES, SIGNUP
import nytid.schedules.utils as utils

booked = []

for course, url in SIGNUP.items():
    booked += utils.read_signup_sheet_from_url(url)

for user in utils.hours_per_TA(booked):
    print(user)


