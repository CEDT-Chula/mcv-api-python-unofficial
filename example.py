from mcv_api.session.session import ChulaLogin
from dotenv import load_dotenv
load_dotenv()
import os

client = ChulaLogin(
    username=os.environ.get('CU_USERNAE', None),
    password=os.environ.get('CU_PASSWORD', None)
)
courses = client.get_joined_courses()

for each in courses:
    print("---------------", each.semester)
    for course in each.courses:
        print(course.courseno, course.title)