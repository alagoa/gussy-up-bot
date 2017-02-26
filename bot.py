import praw
import time

words = {
	'witnesses':'these dudes I know',
	'allegedly':'kinda probably',
	'new study':'tumblr post',
	'rebuild':'avenge',
	'space':'spaaaaace',
	'google glass': 'gameboy',
	'smartphone':'pokedex',
	'electric':'atomic',
	'senator':'elf-lord',
	'car':'cat',
	'election':'eating contest',
	'congressional leaders':'river spirits',
	'homeland security':'homestar runner',
	'could not be reached for comment': 'is guilty and everyone knows it'
}

subreddits = 'smashbros+testabot+upliftingnews+truenews'

def main():

	reddit = praw.Reddit(
		user_agent= 'Gussied up by /u/GussyUpBot)',
		client_id='F6Qzk02F1G5uDw', client_secret='-xsRvjpVON4FDOcmSKx_h1JznGM',
		username='GussyUpBot', password='')

	subreddit = reddit.subreddit(subreddits)
	get_posts(subreddit)

def	get_posts(subreddit):
	try:
		for submission in subreddit.stream.submissions():
			process_submission(submission)
	except praw.exceptions.APIException:
		print 'Rate limit exceeded. I\'m going to rest for 10 minutes.'
		time.sleep(600)
		get_posts()

def process_submission(submission):

	title = submission.title.lower()
	if any(word in title for word in words.keys()):
		improvedTitle = reduce(lambda x, y: x.replace(y, words[y]), words, title)
		submission.reply(improvedTitle)
		print improvedTitle + '\n'


if __name__ == '__main__':
    main()
	

	

