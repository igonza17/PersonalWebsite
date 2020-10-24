from website.models import Courses, PreRequisite

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "adds sample entities to the application"

    def handle(self, *args, **options):

        course_data = [
            [1,'MATH', '1190', 'Calculus I', 'Summer', '2018', 'A'],
            [2,'CSE', '1322', 'Programming and Problem Solving', 'Fall', '2018', 'B'],
            [3,'CSE', '1322L', 'Programming and Problem Solving Lab', 'Fall', '2018', 'A'],
            [4,'CS', '3305', 'Data Structures', 'Spring', '2019', 'A'],
            [5,'CS', '3503', 'Computer Organization and Architecture', 'Spring', '2019', 'B'],
            [6,'MATH', '2202', 'Calculus II', 'Spring', '2019', 'B'],
            [7,'MATH', '2345', 'Discrete Mathematics', 'Fall', '2018', 'A'],
            [8,'CS', '3410', 'Introduction to Database Systems', 'Spring', '2020', 'B'],
            [9,'SWE', '3313', 'Introduction to Software Engineering', 'Spring', '2020', 'A'],
            [10,'CSE', '3801', 'Professional Practices and Ethics', 'Spring', '2020', 'A'],
            [11,'CS', '3502', 'Operating Systems', 'Fall', '2020', 'A'],
            [12, 'CS', '4720', 'Internet Programming', 'Fall', '2020', 'A'],
        ]

        for ad in course_data:
            a = Courses(course_id=ad[0], department=ad[1], course_number=ad[2], course_name=ad[3], semester=ad[4], sem_year=ad[5], grade=ad[6])
            a.save()

        prereq_data = [
            [1, 0,0],
            [2, 0,0],
            [3, 0,0],
            [4, 2,3],
            [5, 2,3],
            [6, 1,0],
            [7, 0,0],
            [8, 2,3],
            [9, 2,3],
            [10, 2,3],
            [11, 4,5],
            [12, 4,8],
        ]


        for pr in prereq_data:
            loc = PreRequisite(course_id=pr[0], prereq1=pr[1], prereq2=pr[2])
            loc.save()

