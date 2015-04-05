# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from datetime import datetime, timedelta
from django.utils import timezone
from setenta_members.models import Members
from setenta_members.models import Authorizations
from django.core.mail import send_mail
from setenta_members import secret_keys
import os, base64
import urllib

login_url = "https://xn--mi-wia.com/setenta/login?token="

def generate_secure_key():
    return base64.b64encode(os.urandom(40))

# Create your views here.

def index(request):
	error = ""
	if request.session.get('auth_fail', False):
		error = "Vain @helsinki.fi -osoitteet ovat mahdollisia"
		request.session['auth_fail'] = False
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'error': error,
	})
	return HttpResponse(template.render(context))

def logout(request):
	request.session.flush()
	return redirect('index')

def send_email_key(request):
	email = request.POST.get("email", "")[:100]
	return send_key_to(request, email)

def send_key_to(request, email):
	#Only @helsinki.fi emails are allowed
	if not email.endswith("@helsinki.fi"):
		request.session['auth_fail'] = True
		return redirect('index')
	expirity = datetime.now() + timedelta(days=1)
	key_auth = generate_secure_key()
	try:
		auth = Authorizations.objects.get(email=email)
		if auth.expirity > timezone.now():
			#There is a token and it's not expired -> require captcha
			request.session['email'] = email
			return redirect('captcha')
		else:
			#Let's update the expired token
			auth.expirity = expirity
			auth.key = key_auth
			auth.save()

	except:
		#There is no token registered for the email
		auth = Authorizations(email=email, key=key_auth, expirity=expirity)
		auth.save()

	global login_url

	link = login_url + urllib.quote_plus(key_auth)
	title = "Setentan jäsenrekisteri - kirjautumislinkki"
	body= "Hei,\n\nOlet yrittänyt kirjautua Setentan jäsenrekisteriin. Voit jatkaa kirjautumista seuraamalla henkilökohtaista linkkiäsi:\n\n"
	body = body + link + "\n\nT. Setenta Ry\n\nPS. Älä vastaa suoraan tähän viestiin"

	send_mail(title, body, 'noreply@xn--mi-wia.com', [email], fail_silently=False)
	request.session['email'] = email
	return redirect('mail_sent')

def mail_sent(request):
	email = request.session.get('email', "")
	if email == "":
		return redirect('index')

	template = loader.get_template('mail_sent.html')
	context = RequestContext(request, {
		'email': email,
	})
	request.session.flush()
	return HttpResponse(template.render(context))

def captcha_view(request):
	email = request.session.get('email', "")
	if email == "":
		return redirect('index')
	error = ""
	if request.session.get('capthcha_fail', False):
		error = "Hups! Virheellinen captcha"
		request.session['capthcha_fail'] = False
	template = loader.get_template('captcha.html')
	context = RequestContext(request, {
		'error': error,
		'email': email,
		"public_key": secret_keys.recaptcha_public(),
	})
	return HttpResponse(template.render(context))

def remove_authorization(email):
	try:
		auth = Authorizations.objects.get(email=email)
		auth.delete()
	except:
		pass

def check_captcha(request):
	email = request.session.get('email', "")
	if email == "":
		return redirect('index')
	response = request.POST.get("g-recaptcha-response","")
	payload = {'secret': secret_keys.recaptcha_secret(), 'response': response}
	r = requests.post("https://www.google.com/recaptcha/api/siteverify", params=payload)
	r_json = r.json()
	data = json.load(r_json)
	if data["success"] == True:
		#Captcha correct
		remove_authorization(email)
		return send_key_to(request, email)
	else:
		request.session['capthcha_fail'] = True
		return redirect('captcha')

def create_empty_user(email):
	try:
		#If user exists, do nothing
		Members.objects.get(email=email)
	except:
		#The user doesn't already exist
		member = Members(name="",email=email, city="",semester=0,subjects="")
		member.save()

def login_failed(request):
	template = loader.get_template('login_failed.html')
	context = RequestContext(request, {'email': '',})
	return HttpResponse(template.render(context))

def login(request):
	key = request.GET.get("token", "")
	try:
		auth = Authorizations.objects.get(key=urllib.unquote_plus(key))
		if auth.expirity > timezone.now():
			#There is a token and it's not expired -> login
			create_empty_user(auth.email)
			request.session['logged_user'] = auth.email
			auth.delete()
			return redirect('edit_profile')
		else:
			return redirect('login_failed')
	except:
		raise
		return redirect('login_failed')


def edit_profile(request):
	user = request.session.get('logged_user', "")
	if user == "":
		#The user is not logged in
		return redirect('index')
	member = Members.objects.get(email=user)
	error = ""
	if request.session.get('update_fail', False):
		error = "Täytä kaikki kentät ja valitse vähintään yksi pää- tai sivuaine"
		request.session['update_fail'] = False
	template = loader.get_template('edit_profile.html')
	context = RequestContext(request, {
		'error': error,
		'email': user,
		'name': member.name,
		'city': member.city,
		'subjects': member.subjects,
	})
	return HttpResponse(template.render(context))

#This method returns the next semester from June onwards
def current_semseter():
	now = datetime.now()
	if now.month > 5:
		return now.year
	else:
		return now.year - 1

#This method returns the next semester from September onwards
def active_semseter():
	now = datetime.now()
	if now.month > 8:
		return now.year
	else:
		return now.year - 1

def update_profile(request):
	user = request.session.get('logged_user', "")
	if user == "":
		#The user is not logged in
		return redirect('index')

	name = request.POST.get("name", "")
	city = request.POST.get("city", "")
	subjects = request.POST.getlist('subjs')

	if len(name)*len(city)*len(subjects)==0:
		request.session['update_fail'] = True
		return redirect('edit_profile')

	subject_string = ";".join(subjects)

	member = Members.objects.get(email=user)
	member.name = name
	member.city = city
	member.subjects = subject_string
	member.semester = current_semseter()
	member.save()
	return redirect('update_complete')

def update_complete(request):
	user = request.session.get('logged_user', "")
	if user == "":
		return redirect('index')

	semester = str(current_semseter()) + "-" + str(current_semseter()+1)
	template = loader.get_template('update_complete.html')
	context = RequestContext(request, {
		'email': user,
		'semester': semester,
	})
	return HttpResponse(template.render(context))