Yoply! or Echyo.
================

When someone tweets at me, reply with a Yo!

Yo! Reply. Yoply! Or Echo Yo... EchYo!

Configuration
-------------

See `constants.py` to map Twitter Users to Yo Users.

Usage
-----

This app requires some environment variables containing you Twitter App Key and
OAuth tokens:

* `TWITTER_APP_KEY`
* `TWITTER_APP_SECRET`
* `TWITTER_OAUTH_TOKEN`
* `TWITTER_OAUTH_TOKEN_SECRET`

As well as your Yo Token:

* `YO_TOKEN`

I stick these in `~/.twitter` and `~/.yo`, and source them prior to running
the app. Example usage:

    $ source ~/.twitter && source ~/.yo && python yoply/main.py

That's it.
