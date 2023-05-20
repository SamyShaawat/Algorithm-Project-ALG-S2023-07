import praw

# Set up your credentials
reddit = praw.Reddit(client_id='IVuN*********************',
                     client_secret='1KBG************w',
                     user_agent='Us**************')

# Define the subreddits you want to scrape
subreddits = [ 'subreddit_name'] # get each subreddit_name from list_Of_Subreddits.txt

# Create an empty list to store the usernames
usernames = []

# Loop through the subreddits and collect usernames
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.hot(limit=1000):
        author = submission.author
        if author and author.name not in usernames:
            usernames.append(author.name)
            print(f"Username collected: {author.name}")

    print(f"Finished collecting usernames from {subreddit_name}")

# Write the collected usernames to a file
with open('subreddit_name.txt', 'w') as f: #change subreddit_name to the selected subreddit
    for username in usernames:
        f.write(username + '\n')

print("All usernames collected and saved to file.")
