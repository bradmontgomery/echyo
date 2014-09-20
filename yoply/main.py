from os import environ
from sys import exit, stderr, stdout
from twython import TwythonStreamer

import constants


class StreamNotifier(TwythonStreamer):
    """A Custom Streamer for the Twitter Streaming API.

    Requires Twitter creds (app key/secret, oauth token/secret). E.g.:

        stream = StreamNotifier(
            environ['TWITTER_APP_KEY'],
            environ['TWITTER_APP_SECRET'],
            environ['TWITTER_OAUTH_TOKEN'],
            environ['TWITTER_OAUTH_TOKEN_SECRET'],
            exit_on_error=True
        )

    For more info, see:
        https://twython.readthedocs.org/en/latest/usage/streaming_api.html
    and
        https://dev.twitter.com/streaming/overview/request-parameters

    """

    def __init__(self, *args, **kwargs):
        self.exit_on_error = kwargs.pop("exit_on_error", False)
        return super(StreamNotifier, self).__init__(*args, **kwargs)

    def yo(self):
        stdout.write("---> Yo!\n")

    def _valid_mention(self, text, screen_name):
        """See if I'm being metioned by someone who has a Yo account"""
        return text.startswith(constants.ME) and screen_name in constants.USERS.keys()

    def on_success(self, data):
        if 'text' in data:
            user = data['user']['screen_name'].lower()
            if self._valid_mention(data['text'], user):
                print("Yo! to {0}".format(user))

    def on_error(self, status_code, data):
        stderr.write(u"ERROR: {0}\n".format(status_code))
        if self.exit_on_error:
            exit(1)


def get_stream_notifier():
    return StreamNotifier(
        environ['TWITTER_APP_KEY'],
        environ['TWITTER_APP_SECRET'],
        environ['TWITTER_OAUTH_TOKEN'],
        environ['TWITTER_OAUTH_TOKEN_SECRET'],
        exit_on_error=True
    )


if __name__ == "__main__":
    stream = get_stream_notifier()
    tracked_username = "{0}".format(constants.ME)
    stream.user(replies='all', track=tracked_username)
