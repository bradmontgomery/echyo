Yoply! or Echyo.
================

When someone tweets at me, reply with a Yo!

Yo! Reply. Yoply! Or Echo Yo... EchYo!

Configuration
-------------

See `constants.py` to map Twitter Users to Yo Users.

Usage
-----

This app requires a Twitter App Key and OAuth tokens, which it will read from
the following environment variables:

* `TWITTER_APP_KEY`
* `TWITTER_APP_SECRET`
* `TWITTER_OAUTH_TOKEN`
* `TWITTER_OAUTH_TOKEN_SECRET`


I stick these in `~/.twitter`, and run `source ~/.twitter` prior to running
the filter.

Example usage:

    $ source ~/.twitter && python yoply/main.py

That's it.
