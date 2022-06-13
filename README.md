# Project 3 - Dancer App
Been to a dance competition/event? Want to know which teams performed? Want to see who's on that team? Want to see more of their dancing?
Are you a dancer? Come create your own profile to share more about yourself and showcase pieces you've choreographed or been a part of.
Team/Company director? Come create a profile for your team. Share more about the team and showcase the team's performances.

## Deployed App
[Dancer-Connect](https://dancer-connect.herokuapp.com/)

## Project Description
Application that provides information about a dance community. This application will display dancer and team information. Users can sign-up to create their own profiles that will be displayed.
Will use Django Framework for Front-End & Back-End.

## Technologies Used
HTML, CSS, Javascript
Python, Django, Postresql

## Usage
Application Usage: [Dancer-Connect](https://dancer-connect.herokuapp.com/)

Contributor Usage:
- Fork & Clone Repository
- Create Development Branch
- Submit Issue or Pull Request
  - If you identify bugs, submit an issue on the Git repo. Please detail the bug in your issue.
  - If you know how to fix it, feel free to note the methods you would use. You could also submit a pull request with suggested code to fix it.

## Installation/Setup
Install Python, Django, Pip. Setup Pipenv, SQL database.

Comment out `django_heroku.settings(locals())` in dancer_app/settings.py to allow it to run locally.

To run app `python manage.py runserver`


## Scope
### MVP Scope
- Index page of Dancers
- Show page for a Dancer

- Index page of Teams
- Show page for a Team

- Connect a Dancer to a Team
- Connect a Dancer to their Pieces

### Stretch Goals
Use REACT frontend

Authentication: Users/dancers can sign-in to modify their detail page
Display Embedded Video

Social Media:
Follow other dancers
Follow other teams

Dancers can create posts
Dancers can comment on posts
Dancers can comment on Piece videos

Chat/messaging feature

## User Stories
Any User:
As a user, I want to view a dancer's information.
As a user, I want to view a team's information.
As a user, I want to view (video link) performances.

User Signed-In:
As a user, I want to register and sign-in.
As a user, I want to create a profile for myself.
As a user, I want to add a video of my piece to my profile.
As a user, I want to comment on pieces posted by other dancers.

## Wireframes
![Screen Shot 2022-06-03 at 4 35 17 PM](https://user-images.githubusercontent.com/101363667/171948451-f53dd9ec-d372-46bc-944e-36b78d83542a.png)
![Screen Shot 2022-06-13 at 3 00 31 PM](https://user-images.githubusercontent.com/101363667/173425774-fb30522a-4fa7-4f72-9ed1-391afc020981.png)
![Screen Shot 2022-06-13 at 3 00 49 PM](https://user-images.githubusercontent.com/101363667/173425801-64306314-c905-45f9-ac3d-0ffbc78336e1.png)
![Screen Shot 2022-06-13 at 3 01 13 PM](https://user-images.githubusercontent.com/101363667/173425837-0780dd42-2574-44d6-a95c-b415548d8099.png)
![Screen Shot 2022-06-13 at 3 01 32 PM](https://user-images.githubusercontent.com/101363667/173425843-f49b15d5-e544-48cf-9196-d850adc97339.png)


## Data Models
![Screen Shot 2022-06-03 at 3 11 49 PM](https://user-images.githubusercontent.com/101363667/171938835-6b76c602-35bc-494a-baf6-3d815138760d.png)
