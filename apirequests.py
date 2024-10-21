import requests

def get_page_access_token(page_id, user_access_token):

    # Define the Graph API version and construct the API URL to request the Page Access Token
    version = 'v21.0'
    api_url_token = f'https://graph.facebook.com/{version}/{page_id}?fields=access_token&access_token={user_access_token}'
    
    try:
        
        response = requests.get(api_url_token)
        response.raise_for_status()  
        data = response.json()
        print(data)
        return data['access_token']
    
    except requests.exceptions.RequestException as e:    
        print("Error:", e)
        return None



def post_content(page_id, page_access_token):
    message = 'Rokari is testing and running tests on app#4'
    
    url = f'https://graph.facebook.com/v20.0/{page_id}/feed'
    payload = {
        "message":message,
        "access_token": page_access_token
    }
    
    # running the post request, testing payload
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return("post successful")
    else: 
        print(f'failed to post: {response.status_code}')
        print(response.json())

# useless data # 
user_access_token = "EAAX5julbAOYBO5t6qCkIzs8c0na5i80ljrz9rghZAHJrjLUS5g5naYvN5a0b5k8pmDE7QIqCo1W7BtysoRImwb8t5PirIXDs8kr5ZBVWfM4NBZAZB1PZA1eST5LqaS85vicESZAaTiAOOMrteDkZCzAQy8w56etNww5DRB0iQLevIevTpO7Lw15TehI8jExZC6WCrioog6UTae0HQqT23HSlMxuRJQwZD"

page_id = "462579260270042"

page_access_token = get_page_access_token(page_id, user_access_token)

post_content(page_id=page_id, page_access_token=page_access_token)