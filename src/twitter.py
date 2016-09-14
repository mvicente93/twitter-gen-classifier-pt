import tweepy


class TwitterHandler:
    def __init__(self):
        self.auth = tweepy.OAuthHandler('6YAo6l4YuEycyNAaUbl2gPNUF', 'Mi361fQJXEudJy50g9KgwKJuG5RrGCcj7oXFnfg0uvUt9epGCp')
        self.auth.set_access_token('424190326-WknTFl5B7UL6WfMV0stDQIU4MIzo6lb332HxWkeG', 'EWEBSdHQUIgQZGqpULTyCaVGvC23hbgyUKMsjCUjWfnBW')
        self.api = tweepy.API(self.auth)

    def get_user(self, screen_name):
        try:
            return self.api.get_user(screen_name=screen_name)
        except tweepy.TweepError:
            return 'No user'

