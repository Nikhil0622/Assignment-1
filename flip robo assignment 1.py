#!/usr/bin/env python
# coding: utf-8

# # Question-1

# In[1]:


from urllib.request import urlopen


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


import requests


# In[4]:


html = urlopen ("https://en.wikipedia.org/wiki/Main_Page")


# In[5]:


bs = BeautifulSoup(html, "html.parser")


# In[6]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[7]:


print ('List all the header tags :', *titles, sep ='/n/n')


# # Question-2

# In[8]:


from requests import get


# In[9]:


urll = get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')


# In[10]:


request  = urll.text


# In[11]:


from bs4 import BeautifulSoup as Soup


# In[12]:


soup_data = Soup( request, 'html.parser' )


# In[13]:


soup_data.title.text


# In[14]:


movies = soup_data.findAll ('div',{'class':"lister-item mode-advanced"})


# In[15]:


first_movie = movies[0]


# In[16]:


first_movie.h3.a.text


# In[17]:


first_movie.find('span',{'class':"lister-item-year text-muted unbold"}).text[1:5]


# In[18]:


first_movie.find('div',{'class':"inline-block ratings-imdb-rating"})['data-value']


# In[19]:


first_movie.find('div',{'class':"inline-block ratings-metascore"}).span.text.strip()


# In[20]:


first_movie.find('span',{'name':'nv'})['data-value']


# In[21]:


Name = []
Year = []
Rating = []
Meta_score = []
Votes = []
for i in movies:
    Name.append(i.h3.a.text)
    Year.append(i.find('span',{'class':"lister-item-year text-muted unbold"}).text[1:5])
    Rating.append(i.find('div',{'class':"inline-block ratings-imdb-rating"})['data-value'])
    try:
        Meta_score.append(i.find('div',{'class':"inline-block ratings-metascore"}).span.text.strip())
    except:
        Meta_score.append(0)
    Votes.append(i.find('span',{'name':'nv'})['data-value'])


# In[22]:


data = list(zip(Name,Year,Rating,Meta_score,Votes))


# In[23]:


import pandas as pd
df = pd.DataFrame(data,columns=["Name","Year","Rating","Meta_score","Votes"])


# In[24]:


df.head()


# # Question-3

# In[25]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')


# In[26]:


ind_soup = BeautifulSoup(page.content)
ind_movietitle = ind_soup.find_all('td', class_="titleColumn")
ind_movietitle

ind_movies = []

for ind_movie in ind_movietitle:
    ind_movie = ind_movie.get_text().replace('\n', "")
    ind_movie = ind_movie.strip(" ")
    ind_movies.append(ind_movie)
ind_movies[:100]
    
ind_scraped_ratings = ind_soup.find_all('td', class_='ratingColumn imdbRating')
ind_ratings = []
for ind_rating in ind_scraped_ratings:
    ind_rating = ind_rating.get_text().replace('\n', '')
    ind_ratings.append(ind_rating)
ind_ratings

import pandas as pd
ind_data = pd.DataFrame()
ind_data['Movie Names'] = ind_movies[:100]
ind_data['Ratings'] = ind_ratings[:100]
ind_data


# # Question-4

# In[27]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[28]:


president_soup = BeautifulSoup(page.content) 
tag = ["h3"]
presidentname = []
for tags in president_soup.find_all(tag):
    tags = tags.get_text().strip()
    presidentname.append(tags)
presidentname


# In[29]:


tag2 = ["p"]
term = []
for tag1 in president_soup.find_all(tag2):
    tag1 = tag1.get_text().strip()
    tag1 = tag1.replace('Term of Office: ', "")
    term.append(tag1)
term.remove("http://pranabmukherjee.nic.in")
term.remove("http://pratibhapatil.nic.in")
term.remove("http://abdulkalam.nic.in")
term[:13]


# In[30]:


import pandas as pd
presidentlist = pd.DataFrame()
presidentlist['President Name'] = presidentname
presidentlist['Term of Office'] = term[:14]
presidentlist


# # Question-5 (a)

# In[31]:


import  requests
from  bs4 import BeautifulSoup


# In[32]:


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"


# In[33]:


def Top_Mens_Teams(url):
    page = requests.get(url)


# In[34]:


page = requests.get(url)


# In[35]:


soup = BeautifulSoup(page.text,"html.parser")


# In[36]:


table = soup.find("tbody")


# In[37]:


team_name = table.find_all("span",class_="u-hide-phablet")[0:10]


# In[38]:


teams = []
for i in team_name:
    teams.append(i.text)


# In[39]:


match =  table.find_all("td",class_="table-body__cell u-center-text")


# In[40]:


f_match = table.find("td",class_="rankings-block__banner--matches").text


# In[41]:


f_match = table.find("td",class_="rankings-block__banner--matches").text


# In[42]:


matches = ['f_match','f_points']
for i in match:
    matches.append(i.text)


# In[43]:


m_records = matches[0:20:2]


# In[44]:


m_points = matches[1:20:2]


# In[45]:


f_rating = table.find("td",class_="rankings-block__banner--rating u-text-right").text.replace('\n','').strip()


# In[46]:


ratings = table.find_all("td",class_="table-body__cell u-text-right rating")[0:9]


# In[47]:


team_rating = [f_rating]
for i in ratings:
    team_rating.append(i.text)


# In[48]:


data = list(zip(teams,m_records,m_points,team_rating))
import pandas as pd
df = pd.DataFrame(data, columns = ["Team Name","Matches","Points","Ratings"])
df


# # Question-5(b)

# In[49]:


url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"


# In[50]:


page = requests.get(url)


# In[51]:


soup = BeautifulSoup(page.text,"html.parser")


# In[52]:


table = soup.find("table",class_="table rankings-table")


# In[53]:


first_player = table.find("div",class_="rankings-block__banner--name-large").text
first_team = table.find("div",class_="rankings-block__banner--nationality").text.replace('\n','')
first_rating = table.find("div",class_="rankings-block__banner--rating").text


# In[54]:


players = table.find_all("td",class_="table-body__cell rankings-table__name name")[0:9]


# In[55]:


player = [first_player]
for i in players:
    player.append(i.text.replace('\n',''))


# In[56]:


teams= table.find_all("span",class_="table-body__logo-text")[0:9]


# In[57]:


team = [first_team]
for i in teams:
    team.append(i.text)


# In[58]:


ratings = table.find_all("td",class_="table-body__cell rating")[0:9]


# In[59]:


rating = [first_rating]
for i in ratings:
    rating.append(i.text)


# In[60]:


data = list(zip(player,team,rating))
import pandas as pd
df = pd.DataFrame(data, columns = ["Player Name","Team","Rating"])
df


# # Question-5(c)

# In[61]:


url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"


# In[62]:


table = soup.find("table",class_="table rankings-table")


# In[63]:


f_bowler = table.find("div",class_="rankings-block__banner--name-large").text


# In[64]:


b_team= table.find("div",class_="rankings-block__banner--nationality").text.replace('\n','')
b_rating = table.find("div",class_="rankings-block__banner--rating").text
bowlers = table.find_all("td",class_="table-body__cell rankings-table__name name")[0:9]


# In[65]:


bowler = [f_bowler]
for i in bowlers:
    bowler.append(i.text.replace('\n',''))


# In[66]:


teams = table.find_all("span",class_="table-body__logo-text")[0:9]


# In[67]:


ratings = table.find_all("td",class_="table-body__cell rating")[0:9]


# In[68]:


rating = [b_rating]
for i in ratings:
    rating.append(i.text)


# In[69]:


data = list(zip(bowler,rating))
import pandas as pd
df = pd.DataFrame(data, columns = ["Bowler Name","Ratings"])
df


# # Question-6(a)

# In[70]:


url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"


# In[71]:


def Top_Womens_Team(url):
    page = requests.get(url)


# In[78]:


table = soup.find("table",class_="table rankings-table")
table = soup.find("tbody")
team_name = table.find_all ("span",class_="u-hide-phablet")[0:10]


# In[79]:


teams = []
for i in team_name:
    teams.append(i.text)


# In[80]:


match = table.find("td",class_="rankings-block__banner--matches").text
point = table.find("td",class_="rankings-block__banner--points").text
matches = table.find_all("td",class_="table-body__cell u-center-text")


# In[81]:


matches_ = [match,point]
for i in matches:
    matches_.append(i.text)
    


# In[82]:


m_record = matches_[0:20:2]
m_points = matches_[1:20:2]
f_rating = table.find("td",class_="rankings-block__banner--rating u-text-right").text.replace('\n','')
ratings = table.find_all("td",class_="table-body__cell u-text-right rating")
rating = [f_rating]
for i in ratings:
    rating.append(i.text)


# In[83]:


data = list(zip(teams,m_record,m_points,rating))
df = pd.DataFrame(data,columns = ["Team Name","Matches","Points","Ratings"])
df


# # Question-6(b)

# In[84]:


url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"


# In[85]:


page = requests.get(url)


# In[86]:


soup = BeautifulSoup(page.text,"html.parser")


# In[87]:


table = soup.find("table",class_="table rankings-table")


# In[88]:


first_player = table.find("div",class_="rankings-block__banner--name-large").text
first_team = table.find("div",class_="rankings-block__banner--nationality").text.replace('\n','')
first_rating= table.find("div",class_="rankings-block__banner--rating").text


# In[89]:


w_players = table.find_all("td",class_="table-body__cell rankings-table__name name")[0:9]
w_player = [first_player]
for i in w_players:
    w_player.append(i.text.replace('\n',''))


# In[90]:


w_teams = table.find_all("span",class_="table-body__logo-text")[0:9]
w_team = [first_team]
for i in w_teams:
    w_team.append(i.text)


# In[91]:


w_ratings = table.find_all("td",class_="table-body__cell rating")[0:9]
w_rating = [first_rating]
for i in w_ratings:
    w_rating.append(i.text)


# In[92]:


data = list(zip(w_player,w_team,w_rating))
df = pd.DataFrame(data, columns = ["Bowler Name","Team","Rating"])
df


# # Question6-(c)

# In[93]:


url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
page = requests.get(url)


# In[94]:


a_table = soup.find("table",class_="table rankings-table")


# In[95]:


f_allrounder = a_table.find("div",class_="rankings-block__banner--name-large").text
a_team = a_table.find("div",class_="rankings-block__banner--nationality").text.replace('\n','')
a_rating = a_table.find("div",class_="rankings-block__banner--rating").text
allrounders = a_table.find_all("td",class_="table-body__cell rankings-table__name name")[0:9]
allrounder = [f_allrounder]
for i in allrounders:
    allrounder.append(i.text.replace('\n',''))


# In[96]:


all_teams = a_table.find_all("span",class_="table-body__logo-text")[0:9]
all_team = [a_team]
for i in all_teams:
    all_team.append(i.text)


# In[97]:


all_ratings = a_table.find_all("td",class_="table-body__cell rating")[0:9]
all_rating = [a_rating]
for i in all_ratings:
    all_rating.append(i.text)


# In[98]:


data = list(zip(allrounder,all_team,all_rating))
df = pd.DataFrame(data, columns = ["Allrounder Name","Team","Rating"])
df


# # Question-7

# In[99]:


import  requests
from  bs4 import BeautifulSoup


# In[100]:


url = "https://www.cnbc.com/world/?region=world"


# In[101]:


def Top_Mens_Teams(url):
    page = requests.get(url)


# In[102]:


page = requests.get(url)


# In[103]:


news_headline = []
for i in soup.find_all("a", class_='LatestNews-headline'):
    news_headline.append(i.text)
news_headline


# In[104]:


news_time = []
for i in soup.find_all("span",class_="LatestNews-wrapper"):
    news_time.append(i.text)
news_time


# In[105]:


news_link = []
for i in soup.find_all("a", class_='LatestNews-headline'):
    news_link.append(i.get('href'))
news_link


# # Question-8

# In[106]:


url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"


# In[107]:


def Top_Mens_Teams(url):
    page = requests.get(url)


# In[108]:


page = requests.get(url)


# In[109]:


soup = BeautifulSoup(page.text,"html.parser")


# In[110]:


title = []
for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    title.append(i.text)
title


# In[111]:


pub_date = []
for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
    pub_date.append(i.text)
pub_date


# # Question-9

# In[112]:


url = "https://www.dineout.co.in/delhi-restaurants/buffet-special"


# In[113]:


page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
titles = [] 
for i in soup.find_all("div", class_="restnt-info cursor"):
    x = i.find('a').text
    titles.append(x)
titles


# In[114]:


loc = []
for i in soup.find_all("div", class_="restnt-loc ellipsis"):
    loc.append(i.text)
loc


# In[115]:


rating = []
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[116]:


image = []
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
image


# # Question-10

# In[117]:


url = ('https://scholar.google.com/citations?view_op=top_venues&hl=en')


# In[118]:


page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
rank = []
for i in soup.find_all('td', class_="gsc_mvt_p"):
    rank.append(i.text)
rank


# In[119]:


publication = []
for i in soup.find_all('td',class_="gsc_mvt_t"):
    publication.append(i.text)
publication


# In[120]:


h5_index = [] 

for i in soup.find_all("td",class_="gsc_mvt_n"):
    x = i.find(class_="gs_ibl gsc_mp_anchor")
    h5_index.append(x.text)
    
res = h5_index[::2]

h5_index = res

h5_index
    


# In[121]:


h5_median = []
for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
    h5_median.append(i.text)
h5_median


# In[122]:


print(len(rank), len(publication), len(h5_index), len(h5_median))


# In[123]:


df = pd.DataFrame({'Rank':rank, 'Publication':publication, 'h5-index':h5_index, 'h5-mean':h5_median})
df

