from bs4 import BeautifulSoup
import requests


def scraping(user_input, selected_category):
    '''
    scraps either all driver's or team's results from the website based on a given year

    input:
        - selected_category: containing whether ther user is request for the drivers or team results
        - user_input: the year the results are based on
    
    output:
        - a dictionary where it's key represents the leaderboard position and its value containing a list representing the 
        information of the driver or the team
    '''

    # if no year is selected, return none
    if user_input == '':
        return None
    
    # if the year provided is not numeric, return false
    elif not user_input.isdigit():
        return False
    
    # craft the url based on the given category and year
    url = 'https://www.formula1.com/en/results.html/' + user_input + '/' + selected_category + '.html'

    # Send a GET request to the URL and parse the HTML
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # located the table on the page
    result_table = soup.find('table', class_ = 'resultsarchive-table')

    # if no table found, return false
    try:
        result_table.find_all('tbody')
    except AttributeError:
        return False

    # call the appropriate scraping function based on the selected category
    if selected_category == 'drivers':
        return driver_scrap(result_table)
    elif selected_category == 'team':
        return team_scrap(result_table)
        

def driver_scrap(result_table):
    '''
    extract driver's information (driver name, team name and total points) from the result table

    input:
        - result_table: beautifulSoup tag object containing the driver's results
    output:
        a dictionary where each key represents a leaderboard position and their value containing a list with the driver's 
        name, team name and total points scored
    '''
    result_dict = {}

    # loop through each tbody in case there are multiple sections (in the case if website design changes)
    for driver_result_table in result_table.find_all('tbody'):
        
        # loop through each row 
        rows = driver_result_table.find_all('tr')
        for i, row in enumerate(rows):

            # obtain driver's name 
            first_name = row.find('span', class_='hide-for-tablet').text
            last_name = row.find('span', class_='hide-for-mobile').text

            # obtain team name 
            team = row.find('a', class_='grey semi-bold uppercase ArchiveLink').text

            # obtain total points scored
            points = row.find('td', class_='dark bold').text

            # store all driver's infomation into a dictionary, key representing the leaderboard position
            result_dict[i+1] = {
                'driver' : first_name + " " + last_name,
                'team' : team,
                'points' : points
            }

    return result_dict

def team_scrap(result_table):
    '''
    extract team's information (team name and total points) from the result table

    input:
        - result_table: beautifulSoup tag object containing the team's results
    output:
        a dictionary where each key represents a leaderboard position and their value containing a list with the team's 
        name and total points scored
    '''
    result_dict = {}

    # loop through each tbody in case there are multiple sections (in the case if website design changes)
    for driver_result_table in result_table.find_all('tbody'):

        # loop through each row 
        rows = driver_result_table.find_all('tr')
        for i, row in enumerate(rows):

            # obtain team name 
            team = row.find('a', class_='dark bold uppercase ArchiveLink').text

            # obtain total points scored
            points = row.find('td', class_='dark bold').text

            # store all team's infomation into a dictionary, key representing the leaderboard position
            result_dict[i+1] = {
                'team' : team,
                'points' : points
            }

    return result_dict

