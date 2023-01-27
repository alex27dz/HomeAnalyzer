# Getting addresses from builders API / Web App and sending them into automation function to get all the data for them and store them into database and xls files

from Analyzer_core_classes_functions import *

metropolitan = 'Greenville'
state = 'South Carolina'
state_to_short_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Builders Class - functions run
builders = Builders(metropolitan, state_to_short_dict[state], 'Builders.xlsx')
builders.lennar_filter_and_toolbar_info_copy()
# builders.community_and_homes_all_data_to_xls_and_SQL()
builders.closeBrowser()
generated_Id_list = builders.return_Generated_Id_list()
address_list_for_automation = builders.return_community_address_list()

print('original address list --------> {}'.format(address_list_for_automation))
print('original generated_Id_list --------> {}'.format(generated_Id_list))

# Automation on all addresses
for i in range(len(address_list_for_automation)):
    print('looking for details about the address in google')
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get("https://www.google.com/maps/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(address_list_for_automation[i])
    driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
    time.sleep(20)
    # locating the parameters for the Automation
    street = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text
    city = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2[1]/span').text
    city = city.split(",")
    city = city[0]
    driver.close()
    print('street - {}'.format(street))
    print('city - {}'.format(city))
    print('short state - {}'.format(state_to_short_dict[state]))
    print('state - {}'.format(state))
    print('random id - {}'.format(generated_Id_list[i]))
    address_data_automate_tool(street, city, state_to_short_dict[state], state, generated_Id_list[i])

