from os import environ
from sys import exit, stderr, stdout
from twython import TwythonStreamer
from yo import Yo

import people


class MentionFilter(TwythonStreamer):
    """Watches the Twitter Streaming api (user) for mentions from friends.

    Requires Twitter credentials (app key/secret, oauth token/secret). E.g.:

        stream = MentionFilter(
            environ['TWITTER_APP_KEY'],
            environ['TWITTER_APP_SECRET'],
            environ['TWITTER_OAUTH_TOKEN'],
            environ['TWITTER_OAUTH_TOKEN_SECRET'],
            exit_on_error=True,
            yo_token=environ['YO_TOKEN']
        )

    For more info, see:
        https://twython.readthedocs.org/en/latest/usage/streaming_api.html
    and
        https://dev.twitter.com/streaming/overview/request-parameters

    """

    def __init__(self, *args, **kwargs):
        self.yo_client = Yo(kwargs.pop("yo_token"))
        self.exit_on_error = kwargs.pop("exit_on_error", False)
        return super(MentionFilter, self).__init__(*args, **kwargs)

    def yo(self, user):
        stdout.write(u"- Sending Yo to {0}...".format(user))
        self.yo_client.yo(username=user)
        stdout.write("- YO'ed!\n")

    def _valid_mention(self, text, screen_name):
        """See if I'm being metioned by someone who has a Yo account"""
        return text.startswith(people.ME) and screen_name in people.FRIENDS.keys()

    def on_success(self, data):
        if 'text' in data:
            user = data['user']['screen_name'].lower()
            if self._valid_mention(data['text'], user):
                print(u"MATCHED: {0} -- from {1}".format(data['text'], user))
                self.yo(people.FRIENDS[user])

    def on_error(self, status_code, data):
        stderr.write(u"ERROR: {0}\n".format(status_code))
        if self.exit_on_error:
            exit(1)


def get_stream_notifier():
    return MentionFilter(
        environ['TWITTER_APP_KEY'],
        environ['TWITTER_APP_SECRET'],
        environ['TWITTER_OAUTH_TOKEN'],
        environ['TWITTER_OAUTH_TOKEN_SECRET'],
        exit_on_error=True,
        yo_token=environ['YO_TOKEN']
    )


if __name__ == "__main__":
    stream = get_stream_notifier()
    tracked_username = "{0}".format(people.ME)
    stream.user(replies='all', track=tracked_username)
