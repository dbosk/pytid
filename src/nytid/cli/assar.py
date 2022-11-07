from config import COURSES, SIGNUP
from nytid.signup import sheets
from nytid.signup import hr

booked = []

for course, url in SIGNUP.items():
    booked += sheets.read_signup_sheet_from_url(url)

for user in hr.hours_per_TA(booked):
    print(user)

