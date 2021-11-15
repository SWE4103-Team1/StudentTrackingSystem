from django.test import TestCase
from datamodel.models import Student, Course, Enrolment, UploadSet
import datetime
from django.utils import timezone
from generateCounts.counts import count_coop_students_by_semester,count_total_students_by_semester,count_total_students_by_start_date,count_coop_students_by_start_date,count_students_by_rank_semester

class countsTester(TestCase):

    def test_count_coop_students_by_semester(self):
        _upload_set = UploadSet(upload_datetime=timezone.now())
        _upload_set.save()

        student1 = Student(
            student_number = "3573669",name = "Fletcher Donaldson",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student2 = Student(
            student_number = "4567123",name = "Susie Lee",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student3 = Student(
             student_number = "5439871",name = "Bob Flanigan",campus = "SJ",program ="BSSWE",
             start_date = "2019-09-01",upload_set = _upload_set
        )

        student4 = Student(
             student_number = "4782345",name = "Mary Blue",campus = "FR",program ="BSSWE",
             start_date = "2018-01-01",upload_set = _upload_set
        )

        student5 = Student(
             student_number = "3458989",name = "Charles Smith",campus = "FR",program ="BSSWE",
             start_date = "2020-01-01",upload_set = _upload_set
        )

        student1.save()
        student2.save()
        student3.save()
        student4.save()
        student5.save()

        # COOP Course
        course1 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "FR01B",upload_set = _upload_set
        )

        #COOP Course
        course2 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "SJ01A",upload_set = _upload_set
        )

        #Not COOP Course
        course3 = Course(
            course_code = "ECE*3221",name = "COMPUTER ORGANIZATION",credit_hours = 4.00,
            section = "FR02A",upload_set = _upload_set
        )

        course1.save()
        course2.save()
        course3.save()

        #   student1 enrolled in COOP Course , count =1
        enrolment1 = Enrolment(
            student = student1,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        #   student2 enrolled in COOP course, count =2
        enrolment2 = Enrolment(
            student = student2,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        # student2 enrolled in another coop course in the same term
        # This will probably not happen unless the data is flawed, count =2
        enrolment3 = Enrolment(
            student = student2,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        # student3 enrolled in a non co-op course, count=2
        enrolment4 = Enrolment(
            student = student3,course = course3,term = "2021/WI",upload_set = _upload_set
        )

        # student4 enrolled in a non co-op course, count=2
        enrolment5 = Enrolment(
            student = student4,course = course3,term = "2021/WI",upload_set = _upload_set
        )

        # student4 enrolled in a co-op course , count =3
        enrolment6 = Enrolment(
            student = student4,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        #  student4 duplicate, should not add to count, count = 3
        enrolment5 = Enrolment(
            student = student4,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        # student 5 in a another term, should not be counted, count =3
        enrolment6 = Enrolment(
            student = student5,course = course1,term = "2021/FA",upload_set = _upload_set
        )


        enrolment1.save()
        enrolment2.save()
        enrolment3.save()
        enrolment4.save()
        enrolment5.save()
        enrolment6.save()

        countWinter = count_coop_students_by_semester("2021/WI")
        countFall = count_coop_students_by_semester("2021/FA")
        self.assertTrue(countWinter == 3)
        self.assertTrue(countFall == 1)

    def test_count_coop_students_by_start_date(self):
        _upload_set = UploadSet(upload_datetime=timezone.now())
        _upload_set.save()

        student1 = Student(
            student_number = "3573669",name = "Fletcher Donaldson",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student2 = Student(
            student_number = "4567123",name = "Susie Lee",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student3 = Student(
            student_number = "5439871",name = "Bob Flanigan",campus = "SJ",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student4 = Student(
            student_number = "4782345",name = "Mary Blue",campus = "FR",program ="BSSWE",
            start_date = "2020-01-01",upload_set = _upload_set
        )

        student5 = Student(
            student_number = "3458989",name = "Charles Smith",campus = "FR",program ="BSSWE",
            start_date = "2020-01-01",upload_set = _upload_set
        )

        student1.save()
        student2.save()
        student3.save()
        student4.save()
        student5.save()

        # COOP Course
        course1 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "FR01B",upload_set = _upload_set
        )

        #COOP Course
        course2 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "SJ01A",upload_set = _upload_set
        )

        #Not COOP Course
        course3 = Course(
            course_code = "ECE*3221",name = "COMPUTER ORGANIZATION",credit_hours = 4.00,
            section = "FR02A",upload_set = _upload_set
        )

        course1.save()
        course2.save()
        course3.save()

        #   student1 enrolled in COOP Course , count =1
        enrolment1 = Enrolment(
            student = student1,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        #   student2 enrolled in COOP course, count =2
        enrolment2 = Enrolment(
            student = student2,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        # student2 enrolled in another coop course in the same term
        # This will not happen, but as we may change the range parameter we cant have a student counted twice, count =2
        enrolment3 = Enrolment(
            student = student2,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        # student3 enrolled in a non co-op course, count=2
        enrolment4 = Enrolment(
            student = student3,course = course3,term = "2021/WI",upload_set = _upload_set
        )

        # student4 enrolled in a non co-op course, count=2
        enrolment5 = Enrolment(
            student = student4,course = course3,term = "2021/WI",upload_set = _upload_set
        )

        # student4 enrolled in a co-op course ,but start date doesnt match, count =2
        enrolment6 = Enrolment(
            student = student4,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        #  student4 duplicate, should not add to count, count = 2
        enrolment5 = Enrolment(
            student = student4,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        # student 5 start date does not match
        enrolment6 = Enrolment(
            student = student5,course = course1,term = "2021/FA",upload_set = _upload_set
        )


        enrolment1.save()
        enrolment2.save()
        enrolment3.save()
        enrolment4.save()
        enrolment5.save()
        enrolment6.save()

        count = count_coop_students_by_start_date("2019-01-01")
        self.assertTrue(count == 2)

    def test_count_total_students_by_semester(self):
        _upload_set = UploadSet(upload_datetime=timezone.now())
        _upload_set.save()
        student1 = Student(
            student_number = "3573669",name = "Fletcher Donaldson",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student2 = Student(
            student_number = "4567123",name = "Susie Lee",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student3 = Student(
            student_number = "3617785",name = "Henry MacDonald",campus = "SJ",program ="BSSWE",start_date = "2018-01-01",
            upload_set = _upload_set
        )


        student1.save()
        student2.save()
        student3.save()


        course1 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "FR01B",upload_set = _upload_set
        )

        course2 = Course(
            course_code = "MATH*1503",name = "Linear Algebra",credit_hours = 3.00,
            section = "FR01A",upload_set = _upload_set
        )

        course1.save()
        course2.save()


        enrolment1 = Enrolment(
            student = student1,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        enrolment2 = Enrolment(
            student = student2,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        enrolment1.save()
        enrolment2.save()

        count = count_total_students_by_semester("2021/WI")
        self.assertTrue(count == 2)

    def test_count_total_students_by_start_date(self):
        _upload_set = UploadSet(upload_datetime=timezone.now())
        _upload_set.save()


        student1 = Student(
            student_number = "3573669",name = "Fletcher Donaldson",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student2 = Student(
            student_number = "4567123",name = "Susie Lee",campus = "FR",program ="BSSWE",
            start_date = "2019-01-01",upload_set = _upload_set
        )

        student3 = Student(
            student_number = "5439871",name = "Bob Flanigan",campus = "SJ",program ="BSSWE",
            start_date = "2020-01-03",upload_set = _upload_set
        )


        course1 = Course(
            course_code = "ECE*3221",name = "COMPUTER ORGANIZATION",credit_hours = 4.00,
            section = "FR02A",upload_set = _upload_set
        )

        course2 = Course(
            course_code = "MATH*1503",name = "Linear Algebra",credit_hours = 3.00,
            section = "FR01A",upload_set = _upload_set
        )

        enrolment1 = Enrolment(
            student = student1,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        enrolment2 = Enrolment(
            student = student2,course = course2,term = "2021/FA",upload_set = _upload_set
        )

        enrolment3 = Enrolment(
            student = student2,course = course1,term = "2021/FA",upload_set = _upload_set
        )

        enrolment4 = Enrolment(
            student = student3,course = course1,term = "2021/FA",upload_set = _upload_set
        )

        student1.save()
        student2.save()
        student3.save()
        course1.save()
        course2.save()
        enrolment1.save()
        enrolment2.save()
        enrolment3.save()
        enrolment4.save()

        count = count_total_students_by_start_date("2019-01-01")

        self.assertTrue(count == 2)

    def test_count_students_by_rank(self):
        _upload_set = UploadSet(upload_datetime=timezone.now())
        _upload_set.save()
        student1 = Student(
            student_number = "3573669",name = "Fletcher Donaldson",campus = "FR",program ="BSSWE",
            start_date = "2021-09-01",upload_set = _upload_set,rank = 'FIR'
        )

        student2 = Student(
            student_number = "4567123",name = "Susie Lee",campus = "FR",program ="BSSWE",
            start_date = "2020-09-01",upload_set = _upload_set,rank = 'SOP'
        )

        student3 = Student(
            student_number = "3617785",name = "Henry MacDonald",campus = "SJ",program ="BSSWE",
            start_date = "2019-09-01",upload_set = _upload_set,rank = 'JUN'
        )

        student4 = Student(
            student_number = "3629987",name = "Felix Johnson",campus = "FR",program ="BSSWE",
            start_date = "2018-01-01",upload_set = _upload_set,rank = 'SEN'
        )


        student1.save()
        student2.save()
        student3.save()
        student4.save()


        course1 = Course(
            course_code = "CS*COOP",name = "CO-OP WORK TERM",credit_hours = 0.00,
            section = "FR01B",upload_set = _upload_set
        )

        course2 = Course(
            course_code = "MATH*1503",name = "Linear Algebra",credit_hours = 3.00,
            section = "FR01A",upload_set = _upload_set
        )

        course1.save()
        course2.save()


        enrolment1 = Enrolment(
            student = student1,course = course1,term = "2021/WI",upload_set = _upload_set
        )

        enrolment2 = Enrolment(
            student = student2,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        enrolment3 = Enrolment(
            student = student3,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        enrolment4 = Enrolment(
            student = student4,course = course2,term = "2021/WI",upload_set = _upload_set
        )

        enrolment1.save()
        enrolment2.save()
        enrolment3.save()
        enrolment4.save()

        rank_counts = list(count_students_by_rank_semester("2021/WI").values()) # count_students_by_rank returns dictionary

        self.assertTrue(rank_counts == [1,1,1,1])
