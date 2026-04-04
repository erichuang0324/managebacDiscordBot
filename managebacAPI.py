import requests
from bs4 import BeautifulSoup
cookies = {
    "_managebac_session": "%2BECHFGIAoepylNMWbYK6M0bqi5m6WkWRXRAeS8sAD4YqOq8G21Rd5a87Kjt2eCumkx3T%2BumaHrAeEEB6ab%2B0Zq6XQLvONey9FkdBpI5RjYPc540ubUMVNjWk2KUJvtFBXEbCp6okv2fLVNuDqsszQPtnVQpCEzrDWmAlSBl4bYpvtTa%2F4zA8Fdx0QydPSyjJzwemJ4Uy%2FdB6lwCKViVFWqdK3R0XpiunhMB4SxZPyglNssAbFB7S%2BXY9ewaV4MESip96n08leK4HJpjl8aashIjnNF69YM4YoETZT1Wq5ix2yvryCFAVXNuWvyKaIcrGYVts1085dnrcukJofB6GAxz%2BJfhp%2BntZwqI3cEspiEH9%2B2lKm1cIA3sgq0WUbYU%2FqsngrSqmHwQBX7yuTh9Xz7C5ej5A8s3NbmmZnRL%2Byuj8UogGBD33TF5Xsy7D3BcqZu%2FH9%2FMeZTMSLbnJ2ouea9%2B%2BkCnqwO2lQ5gOMAwSe6vM61DDzRfJdN%2FeM1rRhJ5c2tXBTiRj0PwYRHVoMGMNvVtiRI7G%2Bv7or%2F2YrwMTThShwwkUARnpnI2G1gDppHZxrt2Sdj5pLvxmzHyT93Fgt5OQCsKKd5b2j0ez3ZjBof9evuJsV8pJSHKF6dLnoAFfNO2rQ9ulNr4%3D--IvhezyToPg%2BLma8w--21gKQmV0Kg8HB%2BN67UUy6A%3D%3D"
}



def listAllClasses() -> dict:
    r = requests.get("https://mingdao.managebac.com/student/classes/page/1", cookies=cookies)
    soup = BeautifulSoup(r.text,'html.parser')

    allListItems = soup.find_all('li',class_='f-menu__submenu-item')
    class_data = {}
    for listitem in allListItems:
        div = listitem.find('div','f-menu__submenu-icon f-menu__submenu-indicator')
        if div:
            class_id = ''.join(filter(str.isdigit,listitem.find('a','f-menu__link f-menu__submenu-link').get('href')))
            class_name = listitem.find('span','f-menu__submenu-link-title').get_text()
            class_data[class_name] = class_id
    return class_data

def listAllTaskesOfClass(class_id):
    # Maybe Incorprate findallclasses here
    r = requests.get(f"https://mingdao.managebac.com/student/classes/{class_id}/core_tasks", cookies=cookies)
    soup = BeautifulSoup(r.text,"html.parser")
    allListItems = soup.find_all('div',class_="fusion-card-item short-assignment section hstack flex-wrap")
    
    for listItem in allListItems:
    print(len(allListItems))


listAllTaskesOfClass(12781010)



#
#{'G10 Chinese Language & Literature (Grade 10) 1002': '12781010', 'G10 English Language and Literature (Grade 10) Brian': '12781208', 'G10 Individuals & Societies (Grade 10) 1002': '12781091', 'G10 Physics (Grade 10) 1002': '12781102', 'G10 Math  (Grade 10) Mark': '12781111', 'G10 Visual Art (Grade 10)': '12781117', 'Personal Project (Grade 10) 1002': '12781137', 'G10 Advance Spanish (Grade 10)': '12780940', 'G10 College Advising (Grade 10) 1002': '12780941', 'G10 Guidance (Grade 10) 1002': '12780943', 'G10 Homeroom Hour (Grade 10) 1002': '12780920', 'G10 Physical Education (Grade 10) Group 1': '12780948'}



# ---------------Test Code-----------
# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(r.text)
# print("Saved!")