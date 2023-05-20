import praw

# Authenticate using your Reddit app credentials
reddit = praw.Reddit(client_id='IVuN*********************',
                     client_secret='1KBG************w',
                     user_agent='Us**************')

# Get the top 100 subreddits in Egypt
subreddit_list = reddit.subreddits.search('Egypt', limit=105)
subreddits = []

# Collect the names of the subreddits
for subreddit in subreddit_list:
    subreddits.append(subreddit.display_name)

# Save the output in a text file
with open('List_Of_Subreddits.txt', 'w') as file:
    file.write('\n'.join(subreddits))

print("Subreddits saved to 'List_Of_Subreddits.txt' file.")
