from bs4 import BeautifulSoup
import json


def find_all_tt_comments(html_code):

    # Parse the HTML
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find all comment containers
    comment_containers = soup.find_all('div', class_='tiktok-ulyotp-DivCommentContentContainer')

    # Initialize a list to store all comments and likes
    comments_data = []

    # Iterate through each comment container
    for container in comment_containers:
        comment_text = container.find('p', class_='tiktok-xm2h10-PCommentText').text.strip()
        likes = int(container.find('span', class_='tiktok-gb2mrc-SpanCount').text)
        comment_data = {
            "comment_text": comment_text,
            "likes": likes
        }
        comments_data.append(comment_data)
    return comments_data

# # Write the information to a JSON file
# with open('comments_info.json', 'w') as json_file:
#     json.dump(comments_data, json_file, indent=4)

# print("Comments information has been extracted and saved to 'comments_info.json'.")