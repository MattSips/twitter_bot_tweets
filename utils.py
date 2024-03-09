import os
import sqlite3
import requests
from keys import google_key, cx

# Assuming utils.py is inside the app folder
APP_DIR = os.path.dirname(__file__)

# Path to the tweet counter file (inside the /app directory)
# TWEET_COUNTER_FILE = os.path.join(APP_DIR, "tweet_counter.txt")

# Path to the SQLite database file (inside the /app directory)
# DB_FILE_PATH = os.path.join(APP_DIR, "my_database.db")

# Path to jpg file (inside the /app directory)
TEMP_IMAGE_DIR  = os.path.join(APP_DIR, "temp_image.jpg")

# Path to Tweet Order Dict txt file (inside the /app directory)
# TWEET_ORDER_DICT = os.path.join(APP_DIR, "tweet_order_dict.txt")



def save_api_requests():
    return "https://www.christies.com/img/LotImages/2006/NYR/2006_NYR_01717_0118_000(125845).jpg?mode=max"

def create_and_post_tweet(client_v1, client_v2):
    tweet_data = {
        'art_title': "Big Mastiff",
        'artist': "Radovan Rohovsky",
        'year': '2018',
        'description': "A large Mastiff"
    }

    art_title = tweet_data['art_title']
    artist = tweet_data['artist']
    year = tweet_data['year']
    description = tweet_data['description']

    # Check if tweet_text needs to be split into multiple tweets
    tweet_text = f"{art_title} by {artist}\nDate: {year}\n\n{description}"
    desc = None


        # Save the image to a local file (e.g., 'temp_image.jpg')
    media_path = TEMP_IMAGE_DIR
    media = client_v1.simple_upload(filename=media_path)
    media_id = media.media_id
    client_v2.create_tweet(text=tweet_text, media_ids=[media_id])

    print(f"Success - Tweet Number: 1, Tweet ID: 1, Title: {art_title}, has been posted")

        # Delete the image file after tweeting
    os.remove(TEMP_IMAGE_DIR)
"""
            except Exception as e:
            # Exception occurred while downloading image or uploading media
            print(f"Error: {e}")
            if os.path.exists(TEMP_IMAGE_DIR):
                os.remove(TEMP_IMAGE_DIR)  # Remove the invalid image file

            print(
                f"Attempt {attempt} of 7 failed for Tweet Number: {tweet_counter} - Tweet ID: {tweet_id}, generating new image")

            # Attempt to generate a new image link and continue with the next attempt
            attempt += 1
            image_link = create_image_link(search, attempt)
"""