import os
import requests


def add_participant_row(name, date_of_birth, sex, height, weight):
    page_id = 'b3c14c52358544369e448c8be68b47b5'
    token = os.getenv("NOTION_API_KEY")
    url = "https://api.notion.com/v1/pages"

    payload = {
        "parent": {"database_id": page_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Date of Birth": {
                "date": {
                    "start": date_of_birth
                }
            },
            "Sex": {
                "multi_select": [
                    {
                        "name": sex
                    }
                ]
            },
            "Height": {
                "number": height
            },
            "Weight": {
                "number": weight
            }
        }
    }

    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
        "Authorization": "Bearer " + token,
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()