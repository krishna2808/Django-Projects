from django.shortcuts import render
from .models import *


# book_name = []
# Create your views here.
def information(request):
    engineering = Department.objects.all()
    if request.method == 'POST':
        book_name = []

        semester = request.POST['sem']
        department = request.POST['dept']
        details = Book.objects.all()
        print("**************************************************************************")
        # print(type(department))
        # print(semester)

        for ob in details:
            if str(ob.department) == department and str(ob.semester) == semester:
                book_name.append(ob.book_name)
        # print(book_name)
        if (book_name != []):
            return render(request, 'store/information.html', {'eng': engineering, 'book_name': book_name})
        else:
            return render(request, 'store/information.html', {'eng': engineering, 'error': 'Book is not  Available','book_name': None})


    else:
        # sem = Semester.objects.all()

        return render(request, 'store/information.html', {'eng': engineering})


def bookDetails(request):
    engineering = Department.objects.all()
    semester = Semester.objects.all()

    details = Book.objects.all()

    if request.user.is_authenticated:
        if request.method == 'POST':
            department = request.POST['dept']
            sem = request.POST['sem']
            subject1 = request.POST['subject1']
            # subject2 = request.POST['subject2']
            # subject3 = request.POST['subject3']
            # subject4 = request.POST['subject4']
            # subject5 = request.POST['subject5']
            # subject6 = request.POST['subject6']
            # print(type(subject1))
            print("**************************************************************************")

            for ob_department in engineering:
                if str(ob_department.dept) == department:
                    # sem = ob.dept
                    object_dept = ob_department
                    # print(type(object_dept.dept))
                    # # print(type(sem))
                    # print(type(ob_department))
                    # print("**************************************************************************")

            for ob_semester in semester:
                if str(ob_semester.semester) == sem :
                    object_sem = ob_semester


            if (len(sem) == 1) and (len(subject1) > 2):
                # for no_of_book in range(6):
                #     book_name = "subject"+str(no_of_book+1)
                #     print(type(book_name))
                #     if str(book_name) == subject1:
                #         print("yes")
                # # print(book_name)
                #         print("***************************************************************************")



                    book_details = Book(department=object_dept,  semester=object_sem, book_name=subject1)
                    book_details.save()
                    success = 'successfully Uploaded '
                    return render(request, 'store/bookDetails.html', {'eng': engineering, 'success': success})
            else:
                error2 = 'Invalid Insert your data '
                return render(request, 'store/bookDetails.html', {'eng': engineering, 'error2': error2})

            print("**************************************************************************")
        # print(details)
        # for i in details:
        #     print(i.department)
        #     print(i.semester)
        #     print(i.book_name)
        # print("**************************************************************************")
        else:
            return render(request, 'store/bookDetails.html', {'eng': engineering})
    else:
        error1 = {"error": "Please First Login your Account "}
        return render(request, 'accounts/home.html', error1)
def howToTakenBook(request):
    return render(request, 'store/howToTakenBook.html')