from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import datetime

# import your forms here
from .forms import *

# import your functions here
from .functions import *

# Create your views here.
def login(request):
	return render(request, 'accounts/login.html')

def voterRegister(request):
	form = VoterForm()
	id = 0;
	messages = {'mess01': False, 'mess02' : False, 'default ' : True}
	if request.method == 'POST':
		form = VoterForm(request.POST)
		if form.is_valid():
			voter = form.save(commit=False)
			aadhar_no = form.cleaned_data['aadhar_no']
			aadhar_no = int(aadhar_no)
			date_of_birth = form.cleaned_data['date_of_birth']
			date = int(date_of_birth.day)
			month = int(date_of_birth.month)
			year = int(date_of_birth.year)
			region = form.cleaned_data['region']
			verify = aadhar_authenticate(aadhar_no, date, month, year, region)
			if(verify == 'valid data'):
				voter.voter_id = uniqueIdGenerator()
				voter.admin = region.admin
				id = voter.voter_id
				dob = voter.date_of_birth
				a,b = mature(dob)
				if a :
					voter.age = b;
					voter.save()
					messages['mess01'] = True
					messages['default'] = True
					
				else:
					messages['mess02'] = True
			else:
				return render(request, 'accounts/error.html')
	if messages['mess01'] : 
		message1 = 'Your voter-id is- ' + str(id)
	else : 
		message1 = ''
	if messages['mess02'] : 
		message2 = 'You are not eligible for voting'
	else : 
		message2 = ''
	context = {'form':form, 'message1':message1, 'message2' : message2}
	return render(request, 'accounts/voterRegister.html', context)

def voterLogin(request):
	messageV = "Invalid voter-id or Password"
	context = {}
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			a,b = authenticate(data['id'], data['password'], 'voter')
			if a and b:
				return redirect('/dashboardVoter/{}/'.format(data['id']))
			else:
				context = {'messageV':messageV}
		else:
			return redirect('accounts/login.html', context)
	return render(request, 'accounts/login.html', context)

def adminLogin(request):
	messageA = "Invalid admin-id or Password"
	context = {}
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			a,b = authenticate(data['id'], data['password'], 'admin')
			if a and b:
				return redirect('/dashboardAdmin/{}/'.format(data['id']))
			else:
				context = {'messageA':messageA}
		else:
			return redirect('accounts/login.html')
	return render(request, 'accounts/login.html', context)

def dashborardVoter(request, id):
	voter = Voter.objects.get(voter_id=id)
	can_vote = ''
	if voter.vote != '' : 
		can_vote = 'You have already voted once !!'
	voter_region = voter.region.region_id
	result = election_in(voter.region.region_id)
	message = result
	if result == 'Election is over':
		remove_election(voter.region.region_id)
		message = 'There are no elections going on !!'
	if Election.objects.filter(region_name=voter.region).exists():
		election = Election.objects.filter(region_name=voter.region).last()
		id_of_election = election.election_id
		election_candidates = election.candidates.all()
		start_time = election.start_time
		end_time = election.end_time
		date_created = election.date_created
		message = election_in(voter.region.region_id) 
	else:
		election_candidates = []
		id_of_election = 'none'
		start_time ='none'
		end_time = 'none'
		date_created = 'none'
	context = {'voter':voter, 'voter_region':voter_region, 'election_candidates':election_candidates, 'id':id, 'election_id':id_of_election, 'start_time':start_time, 'end_time':end_time, 'date_created':date_created, 'message' : message, 'can_vote' : can_vote}
	return render(request, 'accounts/dashboardVoter.html', context)

def dashboardAdmin(request, id):
	admin = Admin.objects.get(admin_id=id)
	admin_region_id = admin.region.region_id
	voters = reversed(admin.voter_set.all())
	voters_count = admin.voter_set.count()
	context = {'admin':admin, 'admin_region_id':admin_region_id, 'voters_count':voters_count, 'voters':voters}
	return render(request, 'accounts/dashboardAdmin.html', context)

def createNew(request, pk):
	admin = Admin.objects.get(id=pk)
	admin_id = admin.admin_id
	admin_region = admin.region
	form = NewElectionForm()
	if request.method == 'POST':
		elections = Election.objects.filter(region_name=admin_region)
		if(elections.count() == 0):
			form = NewElectionForm(request.POST)
			if form.is_valid():
				election = form.save(commit=False)
				election.election_id = electionId()
				election.admin = admin
				election.region_id = admin_region.region_id
				form.save()
				return redirect(dashboardAdmin, id=admin_id)
			else:
				print('error')
		else:
			return render(request, 'accounts/newElectionWarning.html')
	context = {'admin':admin, 'form':form}
	return render(request, 'accounts/createNew.html', context)


def all_candidate(request, region_id):
	candidates_region_name = Region.objects.get(region_id=region_id)
	candidates = reversed(Candidate.objects.filter(region=candidates_region_name))
	region_name = Region.objects.get(region_id=region_id)
	form = AddCandidateForm()
	if request.method == 'POST':
		form = AddCandidateForm(request.POST)
		if form.is_valid():
			candidate = form.save(commit=False)
			candidate.candidate_id = uniqueIdGenerator()
			candidate.region = region_name
			candidate.save()
	context = {'candidates':candidates, 'form':form}
	return render(request, 'accounts/all_candidates.html', context)
		

def verifyVote(request, id, election_id, candidate_id, key):
	if key == '1' : 
		voter = Voter.objects.get(voter_id = id)
		if len(voter.vote) == 0 : 
			voter.vote = candidate_id
			voter.election = election_id
			voter.save()	
		else : 
			print('Voter has already voter !!')
	return redirect('/dashboardVoter/{}'.format(id))


def winner(request, id):
	previous_winners = ''
	winner_id = ''
	winner_name =''
	winner_party = ''
	winner_votes = ''
	last_election_date = ''
	date_created = ''
	if History.objects.filter(region_id = id).exists() :
		previous_winners = reversed(History.objects.filter(region_id=id))
		election = History.objects.filter(region_id=id).last()
		if election.winner_id == 'none' : 
			winner_id = 'none'
			winner_name = 'none'
			candidate = 'multiple'
			winner_party = 'multiple'
		else : 
			winner_id = election.winner_id
			winner_name = election.winner_name
			candidate = Candidate.objects.get(candidate_id = winner_id)
			winner_party = candidate.party_name
		winner_votes = election.votes
		last_election_date = election.date_created
		date_created = election.date_created
	context = {'previous_winners':previous_winners, 'winner_id':winner_id, 'winner_name':winner_name, 'winner_votes':winner_votes, 'winner_party':winner_party, 'last_election_date':last_election_date, 'date_created':date_created}
	return render(request, 'accounts/winner.html/', context)