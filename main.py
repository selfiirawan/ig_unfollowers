# UNFOLLOWES DETECTOR
# This script extracts Instagram usernames from HTML files and identifies accounts that are not following back.

import re

def extract_username(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # extract username from profile links
    pattern = r"https://www.instagram.com/([a-zA-Z0-9_.]+)"

    # find all users and return as a set
    usernames = set(re.findall(pattern, content))

    return usernames

# extract users from followers & followings
followers = extract_username("followers.html")
followings = extract_username("following.html")

# find users that are not following back 
not_following_back = followings - followers

# output for "not following back"
print("\n=== ACCOUNTS THAT ARE NOT FOLLOWING BACK ===")
count = 1
unfollowers = "Users that are not following back / Unfollowed: \n"
unfollowers += "-" * 50 + "\n\n"

if not_following_back:
    for username in not_following_back:
        unfollowers += f"{count}. {username}\n"
        unfollowers += f"https://instagram.com/{username}\n\n"
        count += 1
else:
    print("\n✔️ Everyone is following you back")

# to see the results in the console
print(unfollowers)


# if want to save the data for later use
with open("unfollowers.txt", "w") as file:
    file.write(unfollowers)