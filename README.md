# slack-question-counter
Quick script to tell you how many questions have been asked in a given Slack channel

# Prerequisites
* Have an app that has the following Bot and User token scopes:
     * groups:history
     * groups:read
     * channels:history
     * channels:read

# Sample command
`python3 slackQuestions.py https://slack.com/api/conversations.history <channel-id> <OAuth-Access-Token>`

* Provide the channelId and your token

# TODO
* Allow to search by name instead of providing the id