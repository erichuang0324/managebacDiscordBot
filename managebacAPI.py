import requests
from bs4 import BeautifulSoup


class managebacAPI:

    def __init__(self,session_id: str):
        self.cookies ={
            "_managebac_session" : session_id
        }

    def user_info(self) -> list:
        r = requests.get("https://mingdao.managebac.com/student/profile", cookies=self.cookies)
        soup = BeautifulSoup(r.text,'html.parser')

        personalInfo = soup.find('div',class_="min-vw-0")
        name = personalInfo.find('h1',class_='text-truncate f-page-header__text f-name-and-flag').get_text(strip=True)
        className = personalInfo.find('a',class_='color-white').get_text(strip=True)
        schoolID = personalInfo.find('span').get_text(strip=True)

        return [name,className,schoolID]
    def listAllClasses(self) -> dict:
        r = requests.get("https://mingdao.managebac.com/student/classes/page/1", cookies=self.cookies)
        soup = BeautifulSoup(r.text,'html.parser')

        allListItems = soup.find_all('li',class_='f-menu__submenu-item')
        class_data = {}
        for listitem in allListItems:
            div = listitem.find('div',class_='f-menu__submenu-icon f-menu__submenu-indicator')
            if div:
                class_id = ''.join(filter(str.isdigit,listitem.find('a',class_='f-menu__link f-menu__submenu-link').get('href')))
                class_name = listitem.find('span',class_='f-menu__submenu-link-title').get_text()
                class_data[class_name] = class_id
        return class_data
    
    def listAllTaskesOfClass(self,class_id) -> dict:
        # Maybe Incorprate findallclasses here
        r = requests.get(f"https://mingdao.managebac.com/student/classes/{class_id}/core_tasks", cookies=self.cookies)
        soup = BeautifulSoup(r.text,"html.parser")
        allListItems = soup.find_all('div',class_="fusion-card-item short-assignment section hstack flex-wrap")
        task_data ={}
        for listItem in allListItems:
            taskNameId = listItem.find('h4',class_='title')

            task_name = taskNameId.find('a').get_text()
            task_id = ''.join(filter(str.isdigit,taskNameId.find('a').get('href').split('/')[5]))
            task_data[task_name] = task_id
        return task_data
    
    def checkTaskScore(self,class_id,task_id):
        r = requests.get(f"https://mingdao.managebac.com/student/classes/{class_id}/core_tasks", cookies=self.cookies)
        soup = BeautifulSoup(r.text,"html.parser") 
        allListItems = soup.find_all('div',class_="fusion-card-item short-assignment section hstack flex-wrap")
        # print(len(allListItems))
        for listItem in allListItems:
            task_id_get = listItem.find('a')
            check_task_id = ''.join(filter(str.isdigit,task_id_get.get('href').split('/')[-1]))
            if not str(task_id) == check_task_id.strip():
                continue
           
            assessmentSituation = listItem.select_one('.assessment.task-score')
            print(assessmentSituation.get_text(strip=True))
            print("------------------------------------")
            
def main():
    testAPI = managebacAPI("1ABiBqXEDjUPvXdGUS0g4N%2FXnDFtFbLBNSBBO0EeN1hsg7Z5YwGUfOk2osCL1mzVH33sKCKfvShDaawHs3PVs1CwutId52ltng9crQ0aRihpQcNfeMMp%2FXP3VGFJ0sFLr8qkQvFDmON0FRHDdsOzGFbseb3sTNYQVxMwsD%2Bo3A7KS9wMFwU8xHFtEePFkXzx8Y5EfyOpSCPJ5hHAQrGS7ccS%2FKkbXcHE0hPmA6EqdpNFPAdiaZz0gX2btZjxr9dYp7ZSGxghNYrDotgxLarLM8aLotq9FBLp81rH2HvH3JQgewONIw%2FH9gp07zqXGG%2BIkxWDpHgTCgXUj%2BjPdP7rT%2FmOhXhEziVVdycxw5x0ipXKb4U7TN7WQToNX%2F92d6BRn4XrFfuSeqRVu%2BjqKJbKVTASCgTLq0WJ6J70l%2BRcXs8bvl5Avg4Nw0fCLo2X8l%2FYDs3uQTTkkhcIrlBkfAWFnn8sUEWPNBUuCUrmJuwh4LLGBySUcG3ndHu%2BCbzvMD4ghstDcg5dLL4tqqRo%2BKCtMq7OioeDm22Kah1IYKINvKqMD3EbpZ%2BIqQexX0pJpG1q08DTOX1%2FKwFHctCsPMHqI67eRija6BgQEKiX6SZNvi0wXZQqRS8%2F5wN5CcjUSd1IHTAUuNGM9u4%3D--H6TNx4rCQcbROKK%2B--C1zUxmnstijdiPKBEbaW%2Bg%3D%3D")
    testAPI.checkTaskScore(12781117,47349877)

if __name__ == "__main__":
    main()




#
#{'G10 Chinese Language & Literature (Grade 10) 1002': '12781010', 'G10 English Language and Literature (Grade 10) Brian': '12781208', 'G10 Individuals & Societies (Grade 10) 1002': '12781091', 'G10 Physics (Grade 10) 1002': '12781102', 'G10 Math  (Grade 10) Mark': '12781111', 'G10 Visual Art (Grade 10)': '12781117', 'Personal Project (Grade 10) 1002': '12781137', 'G10 Advance Spanish (Grade 10)': '12780940', 'G10 College Advising (Grade 10) 1002': '12780941', 'G10 Guidance (Grade 10) 1002': '12780943', 'G10 Homeroom Hour (Grade 10) 1002': '12780920', 'G10 Physical Education (Grade 10) Group 1': '12780948'}
#assessment task-score score-mobile-collapsible assessment-cell


# ---------------Test Code-----------
# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(r.text)
# print("Saved!")