'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncomment to configure in file.
ACCOUNT_SID = "AC82be28758e877815b8b71f1502fb62c1" 
AUTH_TOKEN = "d3a92aa0b15021f25526428d3a14da46"
BSSSPAM_APP_SID = "AP7041c79862b81848642ec778a1db2d6c"
BSS_SPAM_ID = "+12037743144"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
