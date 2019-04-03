from django.shortcuts import render
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
# Create your views here.
data=""" <table>
	            <tr>
	                <th>Emp_id</th>
	                <th>Emp_name</th>
	                <th>Emp_salary</th>
	            </tr>
	            <tr>
	                <td>AB203</td>
	                <td>Krishn Kumar Patel</td>
	                <td>234434.00</td>
	            </tr>
	            <tr>
	                <td>NP45</td>
	                <td>Mohan Dash</td>
	                <td>43453.00</td>
	            </tr>
	            <tr>
	                <td>FR235</td>
	                <td>Suresh Kumar</td>
	                <td>353453.00</td>
	            </tr>
	            <tr>
	                <td>MP323</td>
	                <td>Krishn Gopal Thakur</td>
	                <td>434453.00</td>
	            </tr>
	            <tr>
	                <td>SR353</td>
	                <td>Venkat Reddy</td>
	                <td>23432.00</td>
	            </tr>

        </table> """

def pdfview(request):
	response=HttpResponse(content_type='application/pdf')
	response['Content_Disposition']='fvattachment; filename="myfile.pdf"'
	p=canvas.Canvas(response)
	p.drawString(100,100,"Hello,World.")
	p.showPage()
	p.save()
	return response


def htmlview(request):
	return HttpResponse(data,content_type='text/html')


def xmlview(request):
	return HttpResponse(data,content_type='application/xml')

