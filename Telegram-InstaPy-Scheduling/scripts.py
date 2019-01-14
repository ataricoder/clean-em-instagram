#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, traceback



# Create your script here:
def awesome(InstaPy, username, password, proxy=None):
    try:
        session = InstaPy(username=username, password=password)
        session.login()
        session.end()
    except:
        print(traceback.format_exc())

def biglikers(InstaPy, username, password, proxy=None):
    try:
        session = InstaPy(username=username, password=password)
        session.login()
        session.end()
    except:
        print(traceback.format_exc())

def massiveunfollow(InstaPy, username, password, proxy=None):
    try:
        session = InstaPy(username=username, password=password)
        session.login()

        # Settings

        session.set_dont_unfollow_active_users(enabled=True, posts=5)

        # Actions

        session.unfollow_users(amount=1200, nonFollowers=True, style="RANDOM", unfollow_after=48*60*60, sleep_delay=600)
        session.end()
    except:
        print(traceback.format_exc())

def massivefollow(InstaPy, username, password, proxy=None):
    try:
        CLARIFAI_API_KEY="8da494ee7d5a4421ab7373e2d3563969"
        session = InstaPy(username='clean.em', password='haye12345', disable_image_load=True, multi_logs=True,  bypass_suspicious_attempt=True, headless_browser=True, nogui=True)
        session.login()
        session.set_relationship_bounds(enabled=True, delimit_by_numbers=False, potency_ratio=0.0, max_followers=12000, max_following=4500, min_followers=35, min_following=35)
        session.set_user_interact(amount=2, randomize=True, percentage=80, media='Photo')
        session.set_do_follow(enabled=True, percentage=100)
        session.set_do_comment(enabled=True, percentage=25)
        session.set_do_like(enabled=True, percentage=100)
        #session.set_comments([u"Beautiful place!😍😍😍 @{}", u"Nice photo!💯💯💯 !@{}", u"You have a nice page!🔥🔥🔥 @{}"], media='Photo')
        session.set_skip_users(skip_no_profile_pic=True,
                        no_profile_pic_percentage=100)

        # Check Description to determine commenting behavior

        #session.set_delimit_commenting(enabled=True,max=None, min=None, comments_mandatory_words=['home','duplex','dreamhome', 'house', 'apartment', 'airbnb', 'condo', 'department','townhome','estate','space'])
        session.set_mandatory_language(enabled=True, character_set='LATIN')

        # Use Image detection for comments

        session.set_use_clarifai(enabled=True, api_key=CLARIFAI_API_KEY, probability=0.72, models=['travel'])
        session.clarifai_check_img_for(['conference room','internet area','hallway','entrance','ballroom','bar','stairs'], comment=True, comments=[u"Beautiful place!😍😍😍 @{}"])
        session.clarifai_check_img_for(['reception'], comment=True, comments=[u"Very nice reception!🤩🤩🤩 @{}"])
        session.clarifai_check_img_for(['lounge','living room'], comment=True, comments=[u"That's a cool lounge!💯💯💯 @{}"])
        session.clarifai_check_img_for(['lobby'], comment=True, comments=[u"Nice lobby!💯💯💯 @{}"])
        session.clarifai_check_img_for(['garden'], comment=True, comments=[u"Pretty garden!😍😍😍 @{}"])
        session.clarifai_check_img_for(['terrace'], comment=True, comments=[u"Pretty terrace!😍😍😍 @{}"])
        session.clarifai_check_img_for(['food & beverages'], comment=True, comments=["Yummy!", "Tasty!"])
        session.clarifai_check_img_for(['view'], comment=True, comments=[u"Nice view!🔥🔥🔥"])
        session.clarifai_check_img_for(['bedroom'], comment=True, comments=[u"Nice bedroom!🤩🤩🤩"])
        #session.set_do_comment(enabled=False, percentage=80)
        #session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')
        
        # Quota Supervisor

        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(200, None),
                               peak_comments=(40, None),
                                peak_follows=(80, None),
                                 peak_unfollows=(50, None),
                                  peak_server_calls=(500, None))


        # activity

        #session.interact_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=True)
        #session.follow_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=False, interact=True)
        #session.unfollow_users(amount=1000, nonFollowers=True, style="LIFO", unfollow_after=0, sleep_delay=501)
        #session.unfollow_users(amount=1000, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=0, sleep_delay=501)
        session.set_smart_hashtags(['clean','apartment','airbnb','austin'], limit=1, sort='top', log_tags=True)
        session.like_by_tags(amount=100, use_smart_hashtags=True, interact=True)
        session.end()
    except:
        print(traceback.format_exc())


# !! Not delete the following code.

functions = [f for fname, f in sorted(globals().items()) if callable(f)]
scripts = {}
for function in functions:
    scripts[str(function.__name__).lower()] = function
