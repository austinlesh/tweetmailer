# tweetmailer

This repo contains a Python script for checking if a particular user has tweeted recently* about keywords of interest. For example, I might want to know if a gaming company I like, @manticgames, has tweeted recently about a sale. If there are matching tweets, it will send an email to an address input by the user.

Running the script requires a gmail address with access from [less secure apps](https://support.google.com/accounts/answer/6010255?hl=en) enabled. I created a new account to use for this.

* Right now, it checks for the last two days -- my current idea is for this repo to eventually contain another script to schedule a once-a-day check.
