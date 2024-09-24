from bs4 import BeautifulSoup
import requests


def scraping(user_input, selected_category):

    if user_input == '':
        return None
    
    elif not user_input.isdigit():
        return False
    
    url = 'https://www.formula1.com/en/results.html/' + user_input + '/' + selected_category + '.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    

    result_table = soup.find('table', class_ = 'resultsarchive-table')

    
    try:
        result_table.find_all('tbody')
    except AttributeError:
        return False


    if selected_category == 'drivers':
        return driver_scrap(result_table)
    elif selected_category == 'team':
        return team_scrap(result_table)
        

def driver_scrap(result_table):
    result_dict = {}
    for driver_result_table in result_table.find_all('tbody'):
        rows = driver_result_table.find_all('tr')

        for i, row in enumerate(rows):

            # driver's name 
            first_name = row.find('span', class_='hide-for-tablet').text
            last_name = row.find('span', class_='hide-for-mobile').text

            # team name 
            team = row.find('a', class_='grey semi-bold uppercase ArchiveLink').text

            # points scored
            points = row.find('td', class_='dark bold').text

            # add all infomation to a lis, key being the leaderboard position
            result_dict[i+1] = {
                'driver' : first_name + " " + last_name,
                'team' : team,
                'points' : points
            }
    return result_dict

def team_scrap(result_table):
    result_dict = {}
    for driver_result_table in result_table.find_all('tbody'):
        rows = driver_result_table.find_all('tr')

        for i, row in enumerate(rows):

            # team name 
            team = row.find('a', class_='dark bold uppercase ArchiveLink').text

            # points scored
            points = row.find('td', class_='dark bold').text

            # add all infomation to a lis, key being the leaderboard position
            result_dict[i+1] = {
                'team' : team,
                'points' : points
            }
    return result_dict



# def race_scrap(result_table):
#     result_dict = {}
#     for driver_result_table in result_table.find_all('tbody'):
#         rows = driver_result_table.find_all('tr')

#         for i, row in enumerate(rows):

#             # grand prix name
#             gp = row.find('a', class_='dark bold ArchiveLink').text

#             # date
#             date = row.find('td', class_='dark hide-for-mobile').text


#             # winner's name 
#             first_name = row.find('span', class_='hide-for-tablet').text
#             last_name = row.find('span', class_='hide-for-mobile').text

#             # team name 
#             team = row.find('td', class_='semi-bold uppercase ').text

#             # laps completed
#             points = row.find('td', class_='bold hide-for-mobile').text

#             # add all infomation to a lis, key being the leaderboard position
#             result_dict[i+1] = {
#                 'driver' : first_name + " " + last_name,
#                 'team' : team,
#                 'points' : points
#             }
#     return result_dict