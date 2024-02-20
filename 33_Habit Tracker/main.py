import requests
from datetime import date

today = date.today().strftime('%Y%m%d')

TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
user_parameters = {

    "token": TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_url = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_url, json=user_parameters)
#
#
# print(response.status_code)
# print(response.text)

member ={
"X-USER-TOKEN":TOKEN
}
GRAPHID= "graph3"

graph_parameter = {
    "id":"graph3",
    "name": "Daily Code",
    "unit": "Commit",
    "type":"int",
    "color":"kuro",
    "timezone":"UTC"
}
#-----COMMAND TO CREATE GRAPH-----#

# graph_link = f"https://pixe.la/v1/users/{USERNAME}/graphs"
#
# new_response =requests.post(url=graph_link,json=graph_parameter,headers=member)
#
# print(new_response.text)
#
#-----COMMAND TO POST A PIXEL-----# 
# postAPixel_endpoint=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
#
# pixel_parameter = {
#     "date": f"{today}",
#     "quantity": "1",
# }
#
# response = requests.post(url=postAPixel_endpoint,json=pixel_parameter,headers=member)
#
# print(response.text)

#------COMMAND TO UPDATE A PIXEL------#
# update_pixel = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{today}"

# update_parameter ={
#     "quantity": "3"
# }

# response = requests.put(url=update_pixel, json=update_parameter,headers=member )

# print(response.text)
