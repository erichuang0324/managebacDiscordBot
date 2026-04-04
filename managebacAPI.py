import requests
from bs4 import BeautifulSoup
cookies = {
    "_managebac_session": "AXsxyeXTbYMPPxrGQkbVNVGe9e%2BdsoIC0994usS2elgZr5bYcelZBAoBxMJJEFELCJTOHbi%2F%2BcPjdopCAg9%2BB1qL05ITVwECisvtGfOhnNEc0KyfpLVzJpxXVWgqGS%2FF2qP4pfCr71PlBRBCYMPrYGi6nM%2BKz%2F5yxaDx4JxMMh4n%2FWjwn1BGLIEI3NdIkZoodBpNF%2B%2F2OULAfjSianGciM7R4rqY9aIumzae73ANq0%2FKrG5At4%2FnnvyDcW6vIe8DB9SNqCHPFlLe42b40L%2BBUEyM5n%2BHPxPCFQOcJh7rnGOcRk0RAvoAxoXdGfmvx5FKUNeojFSXA0nQl905aOxKJtN06%2Fw3T1dWL2fIXBe1Ewoyrvo%2FsDj8ZBy384xPvToXrIWHYrj72XSLTmglvASBM4lGx1%2FberbuR%2B%2BoNWRVZC7MIwD8fE0hHSLtm%2FD1AOFp234BK1k6VefGZhpke90xyvpbs9q9se0ekup%2BqtqUq%2BRomnvw6kEv1DNQehjIDY6eoYk4d8f6lfgJPi5O%2BMlfXo24xdI3eJ%2BSVotHDvO8vEAWMcutzEwJA5cU3d%2Bacqow%2B8aYS4Yi%2FYtN0by%2BZD4saGYB%2FXuX98f36BZqn4EScKXN3Eg6wttwo%2F2D%2BFnmRC%2Fa7hpt0upf2cw%3D--n50mmSSua5%2FyjEWo--DpIhjWb%2F3cL8phAzo4ZIbQ%3D%3D"
}



def findAllClasses() -> dict:
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

def listAllTaskesOfClass

print(findAllClasses())



# ---------------Test Code-----------
# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(r.text)
# print("Saved!")