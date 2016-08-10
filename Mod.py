import praw, time, sqlite3, re

#######################################################################################
#This needs to be filled in on your own and should never be shown to anyone           #
#######################################################################################


user_agent = 'A moderator for r/ReportTheBadModerator'
app_id = ''
app_secret = ''
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
refresh_token = ''

#######################################################################################
#Here is the information that the bot will take in                                    #
#######################################################################################

sub = 'reportthebadmoderator'
username = 'thebadmod'
maxposts = 100 #Change this as necessary
disclaimer = '''\n\n--------------------------------------------------------------------------------------------------------\n\n
*I am a bot, and this was done automatically. If you have any questions or concerns regarding the operation of this bot,
[please message the mods](https://www.reddit.com/message/compose?to=%2Fr%2FReportTheBadModerator).
If you would like a bot of your own, feel free to message the [creator of this bot](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)*'''
message = 'Hi, your username was mentioned in r/ReportTheBadModerator. As a mod myself, I think you should go check it out and see if there is any validity to the claim.' + disclaimer

database = sqlite3.connect('database.db')
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()

checks = ['^(.*)u/']

def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(refresh_token)
    print('Loggin in to Reddit as /u/TheBadMod')
    return r


def search_posts():
    submissions = r.get_subreddit(sub).get_new(limit=maxposts)
    for submission in submissions:
        if submission.author.name == None:
            continue
        cur.execute('SELECT * FROM answered WHERE ID=?', [submission.id])
        if not cur.fetchone():
            author = submission.author.name.lower()
            submission_title = submission.title.lower()
            for i in range(len(checks)):
                if re.match(checks[i], submission_title[]):
                    
            
            
