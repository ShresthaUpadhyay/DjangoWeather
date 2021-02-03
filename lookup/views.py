from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']

		api_request = requests.get(" https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=25&API_KEY=7C335ED6-5D29-4CF4-9CA0-A82CFA3A6245")
		
		try:
			api = json.loads(api_request.content)


		except Exception as e:
			api = 'Error...'


		if api[0]['Category']['Name']=="Good":
			category_discription = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name']=="Moderate":
			category_discription = "(51 to 100)	Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color ="Moderate"
		elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups":
		 	category_discription = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		 	category_color = "USG"
		elif api[0]['Category']['Name']=="Unhealthy":
		 	category_discription = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects"
		 	category_color = "Unhealthy"
		elif api[0]['Category']['Name']=="Very Unhealthy":
		 	category_discription = "(201 to 300) Health alert: The risk of health effects is increased for everyone."
		 	category_color = "Very_Unhealthy"
		elif api[0]['Category']['Name']=="Hazardous":
		 	category_discription = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected." 	
		 	category_color = "Hazardous"

		return render(request,'home.html',
			{'api':api,
			'category_discription':category_discription,
			'category_color':category_color })	

	else:

		api_request = requests.get(" https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=40061&distance=25&API_KEY=7C335ED6-5D29-4CF4-9CA0-A82CFA3A6245")
		
		try:
			api = json.loads(api_request.content)


		except Exception as e:
			api = 'Error...'


		if api[0]['Category']['Name']=="Good":
			category_discription = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name']=="Moderate":
			category_discription = "(51 to 100)	Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color ="Moderate"
		elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups":
		 	category_discription = "(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		 	category_color = "USG"
		elif api[0]['Category']['Name']=="Unhealthy":
		 	category_discription = "(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects"
		 	category_color = "Unhealthy"
		elif api[0]['Category']['Name']=="Very Unhealthy":
		 	category_discription = "(201 to 300) Health alert: The risk of health effects is increased for everyone."
		 	category_color = "Very_Unhealthy"
		elif api[0]['Category']['Name']=="Hazardous":
		 	category_discription = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected." 	
		 	category_color = "Hazardous"

		 	 	 	 	
				


		return render(request,'home.html',
			{'api':api,
			'category_discription':category_discription,
			'category_color':category_color })

def about(request):
	return render(request,'about.html',{})	