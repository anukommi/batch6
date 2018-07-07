# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun(request):

	return HttpResponse("27.56")


def fun1(request):
	resp="""
	<html>
	<head>
		<title>
			title tag information
		</title>

	</head>
	<!-- <body bgcolor = "#785148"> -->
		this is body part
		<h1>
				This is h1 tag
		</h1>
		<h2>
				This is h2 tag
		</h2>
		<h3>
				This is h3 tag
		</h3>
		<h4>
				This is h4 tag
		</h4>
		<h5>
				This is h5 tag
		</h5>
		<h6>
				This is h6 tag
		</h6>
		<a href="http://www.google.com">Go to google</a><br>
		<a href="http://www.gmail.com">Go to gmail</a><br>
		<a href="http://www.youtube.com">Go to youtube</a><br>
		<a href="http://www.yahoo.com">Go to yahoo</a><br>

		<form>
			username <input type="text"></input><br>
			Password:<input type="password"></input><br>
			Email:<input type="email"></input><br>
			
			Gender:Male:<input type="radio"></input><br>Male:<input type="radio"></input><br>
			Do you want to join immediately?:<input type="checkbox"></input><br>
			Present address:<textarea></textarea><input type="submit"></input><br>
			Courses available:
			<select>
				<optgroup>
					<option>python</option>
					<option>python,ML</option>
					<option>python, Django</option>
					<option></option>
						
					
				</optgroup>

		</form>
	</body>


</html>
"""
	return HttpResponse(resp)


def register_form(request):

	resp_details = """<html>
	<head>
		<title>
			Student Registration Form
		</title>
	</head>
	<body bgcolor="#A9F5E1">
		<form>
			<!-------------------- First Name --------------------->
			First Name &nbsp&nbsp&nbsp&nbsp<input type="text"></input><br><br>

			<!-------------------- Last Name --------------------->
			Last Name &nbsp&nbsp&nbsp&nbsp<input type="text"></input><br><br>

			<!-------------------- Email --------------------->
			Email Id &nbsp&nbsp&nbsp&nbsp<input type="email"></input><br><br>

			<!-------------------- Mobile --------------------->
			Mobile Number &nbsp&nbsp&nbsp&nbsp<input type="text"></input><br><br>

			<!-------------------- Gender --------------------->
			<!-- Gender &nbsp&nbsp&nbsp&nbspMale<input type="radio" ></input> Female<input type="radio"></input><br><br> -->
			<!-- &nbsp&nbsp&nbsp&nbsp<input type="radio" name="Gender"
			value="Male"checked>Male
			<input type="radio" 
			name="gender value="Female">Female<br><br> -->

			<tr>
			<td>Gender</td>&nbsp&nbsp&nbsp&nbsp
			<td>
			Male<input type="radio" name="Gender" value="Male"/>
			Female<input type="radio" name="Gender" value="Female"/>
			</td>
			</tr>
			<br><br>

			<!-------------------- Address --------------------->
			Address &nbsp&nbsp&nbsp&nbsp<textarea></textarea><input type="submit"></input><br><br>

			<!-------------------- City --------------------->
			City &nbsp&nbsp&nbsp&nbsp<input type="text"></input><br><br>

			<!-------------------- Pin Code --------------------->
			Pin Code&nbsp&nbsp&nbsp&nbsp<input type="text"></input><br><br>

			<!-------------------- Course --------------------->
			Course
			<select>
				<optgroup>
					<option>python</option>
					<option>python,Django</option>
					<option>Devops</option>
					<option>AWS</option>
				</optgroup>
			</select>
			<br><br>

			<!-------------------- Submit form --------------------->
			Submit <input type="submit" ></input>
			&nbsp

			<!-------------------- Reset --------------------->
			Reset <input type="reset" ></input>
		</form>
		  
	</body>

</html>

"""

	return HttpResponse(resp_details)

def fun2(request):
	# return render(request, "index.html")
	return render(request, "Cooling_backup/index.html")