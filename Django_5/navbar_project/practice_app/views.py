from django.shortcuts import render
import datetime
def design(request):
    dic = {
            'name':'erfan',
            'age': 9,
            'list':['mango','jackfruits','banana','apple'],
            'courses': [
                {
                    'id': 1,
                    'courseName': 'python',
                    'fee': 5500
                },
                {
                    'id': 2,
                    'courseName': 'django',
                    'fee': 4000
                },
                {
                    'id': 3,
                    'courseName': 'sql',
                    'fee': 3000
                }
            ],
            'emptyVariable': "",
        }
    # return render(request,'practice_app/language.html', context=dic)
    return render(request,'practice_app/language.html', dic)