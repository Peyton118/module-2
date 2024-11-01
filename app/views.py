from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass
from typing import List

# Create your views here.

@dataclass

class Team():
    name : str
    desc: str
    members: List


pro_team = Team("Procurement Team", "Procurement team has the job of acquiring food everyday of the week and then cooking it so that everyone has something to eat during lunch.", ["Jacob", "Arthur", "Aaron", "Markell"])

mana_team = Team("Management Team", "Management team has the job of ensuring that all of the chores for the day get completed and that people have the equipment to do the chores.", ["Chris", "Kilan", "Aiden", "Tanner"])

docu_team = Team("Documentation Team", "Documentation team is responsible for taking photos of guest speaker, community events , and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.", ["Jason, Patrick"])

comm_team = Team("Community Team", "The community team has the job of preparing an activity every two weeks on a friday. An example of these could be taking everyone to a bowling alley or having a movie night at basecamp along with a few others. They also have to figure out how people will get somewhere if the activity is outside of water valley", ["Arianna", "Peyton"])


teams = {
    "Procurement": pro_team,
    "Management": mana_team,
    "Community": comm_team,
    "Documentation": docu_team,

    }

man_name = teams['Management'].name
pro_name = teams['Procurement'].name
doc_name = teams['Documentation'].name
com_name = teams['Community'].name
man_desc = teams['Management'].desc
pro_desc = teams['Procurement'].desc
doc_desc = teams['Documentation'].desc
com_desc = teams['Community'].desc
man_members = teams['Management'].members
pro_members = teams['Procurement'].members
doc_members = teams['Documentation'].members
com_members = teams['Community'].members



def home_view(request):
    context = {

        "names": [pro_team.name, mana_team.name, docu_team.name, comm_team.name]

    }
    return render(request, "home.html", context)


def team_view(request, team):

    if team == "Management Team":
        team_context = {
        "name": man_name,
        "desc": man_desc,
        "members": man_members,
        }
    elif team == "Procurement Team":
        team_context = {
        "name": pro_name,
        "desc": pro_desc,
        "members": pro_members,
        }
    elif team == "Documentation Team":
        team_context = {
        "name": doc_name,
        "desc": doc_desc,
        "members": doc_members,
        }
    elif team == "Community Team":
        team_context = {
        "name": com_name,
        "desc": com_desc,
        "members": com_members,
        }

    return render(request, "teams.html", team_context)