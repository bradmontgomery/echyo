Echyo
=====

When someone tweets at me, this will automatically reply with a Yo!

Want to play?
-------------

Add yourself as a friend to `people.py`, and send me a pull request.

Environment
-----------

If you want to take this app and run it yourself, you'll need some environment
variables containing you Twitter App Key and OAuth tokens:

* `TWITTER_APP_KEY`
* `TWITTER_APP_SECRET`
* `TWITTER_OAUTH_TOKEN`
* `TWITTER_OAUTH_TOKEN_SECRET`

As well as your Yo Token:

* `YO_TOKEN`

I stick these in a dotfile somewhere (e.g. `~/.echyo`), and source them prior
to running the app. Example usage:

    $ source ~/.echyo && python echyo/echyo.py

That's it.
