from .models import *
import datetime
import math, random
from django import forms
import pandas as pd

df = pd.read_csv("accounts/citizens_data/citizens.csv")

def authenticate(id, password, user_type):
    if user_type == 'voter':
        if Voter.objects.filter(voter_id = id).exists() : 
            if Voter.objects.get(voter_id=id).password == password:
                return True,True
            else:
                return True, False
        else:
            return False,False
    if user_type == 'admin':
        if Admin.objects.filter(admin_id=id).exists():
            if Admin.objects.get(admin_id=id).password == password:
                return True,True
            else:
                return True,False
        else:
            return False,False

def electionId():
    id = '';
    digits = '0123456789'
    for i in range(5):
        id +=digits[math.floor(random.random()*10)]
    return id

def uniqueIdGenerator():
    id_1 = 'ovsid'
    digits = '0123456789'
    id_2 = ''
    for i in range(5):
        id_2 += digits[math.floor(random.random()*10)]
    id = id_1+id_2
    return id

def mature(date_of_birth):
    age = datetime.date.today().year - date_of_birth.year
    if age >=18:
        return True,age
    else:
        return False,age

def calculateWinner(id):
    print("Inside winner")
    voters = Voter.objects.filter(election=id)
    data = {}
    for voter in voters:
        if voter.vote in data.keys():
            data[voter.vote] += 1
        else:
            data[voter.vote] = 1
    temp = 0
    winner = 'none'
    for k, v in data.items() : 
        if v >= int(temp) : 
            winner = k
            temp = v
    c = 0
    for k , v in data.items():
        if v == temp:
            c += 1
    if c == 1 :
        return winner, temp
    else :
        return 'none', c
    return winner, temp


def election_in(region_id):
    print("Inside election_in")
    if Election.objects.filter(region_id = region_id).exists():
        election = Election.objects.get(region_id=region_id)
        system_date = datetime.datetime.now()
        election_date = election.date_created
        deadline = 0
        if election.start_time.hour == election.end_time.hour : 
            if system_date.hour == election.start_time.hour : 
                if system_date.minute >= election.start_time.minute and system_date.minute <= election.end_time.minute : 
                    return 'You can vote'
                elif system_date.minute < election.start_time.minute : 
                    return 'Election not started yet'
                else : 
                    return 'Election is over'
            elif system_date.hour < election.start_time.hour : 
                return 'Election not started yet'
            else : 
                return 'Election is over'
        else :
            if system_date.hour >= election.start_time.hour and system_date.hour < election.end_time.hour : 
                if system_date.minute >= election.start_time.minute : 
                    return 'You can vote' 
                else : 
                    return 'Election not started yet'
            elif system_date.hour == election.end_time.hour : 
                if system_date.minute <= election.end_time.minute : 
                    return 'You can vote'
                else : 
                    return 'Election is over'
            elif system_date.hour < election.start_time.hour : 
                return 'Election not started yet'
            else : 
                return 'Election is over'
    else:
        return "There are no elections going on !!"

def remove_election(r_id) :
    print("Inside remove_election")
    election = Election.objects.get(region_id = r_id)
    winner, votes = calculateWinner(election.election_id)
    data = History(election_id = election.election_id)
    if winner == 'none' : 
        data.winner_id = 'none'
        data.winner_name = 'multiple'
        data.winner_party = 'none'
    else : 
        candidate = Candidate.objects.get(candidate_id = winner)
        data.winner_id = candidate.candidate_id
        data.winner_name = candidate.name
        data.winner_party = candidate.party_name
    data.votes = votes
    data.region_id = r_id
    data.date_created = election.date_created
    data.save()
    region_name = Region.objects.get(region_id=r_id)
    voters = Voter.objects.filter(region=region_name)
    for voter in voters:
        voter.vote = ''
        voter.election = '' 
        voter.save()
    election.delete()


def aadhar_authenticate(aadhar_no, day, month, year, region):
    temp = df[df.aadhar_no == aadhar_no]
    region = str(region) 
    if len(temp) == 0:
        return 'invalid aadahar no'
    else :
        temp = temp.reset_index().drop(['index'], axis = 1)
        lst = temp.date_of_birth[0].split('-')
        if (int(lst[0]) == day and int(lst[1]) == month and int(lst[2]) == year and region == str(temp.region[0])) :
            return 'valid data' 
        else :
            return 'invalid data'