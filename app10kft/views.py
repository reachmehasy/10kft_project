from django.shortcuts import render
import xlsxwriter,io
from django.http import HttpResponse



def index(request):
    return render(request,'index.html')

def validate(request):
    usr = request.POST['uname']
    pwd = request.POST['pswrd']
    res = usr + pwd
    if res == 'adminadmin':
        return render(request, 'index.html', {'result':'Welcome '+usr.capitalize()+'!'})
    else:
        return render(request, 'index.html', {'result': 'Incorrect user name and password'})

def downloadExcel(request):
    
# Create an new Excel file and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
# Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)
# Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
# Write some simple text.
    worksheet.write('A1', 'Hello')
# Text with formatting.
    worksheet.write('A2', 'World', bold)
# Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)
    workbook.close()
    output.seek(0)
    filename = 'reportfile.xlsx'
    response = HttpResponse(output,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

