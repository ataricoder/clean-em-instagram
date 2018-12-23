"""
This template is written by @loopypanda

What does this quickstart script aim to do?
- My settings is for running InstaPY 24/7 with approximately 1400 follows/day - 1400 unfollows/day running follow until reaches 7500 and than switch to unfollow until reaches 0.
"""


from instapy import InstaPy
from instapy.util import smart_run



# get a session!
session = InstaPy(username='clean.em', password='haye12345', disable_image_load=True, multi_logs=True,  bypass_suspicious_attempt=True, headless_browser=True, nogui=True)


# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=False, potency_ratio=0.0, max_followers=12000, max_following=4500, min_followers=35, min_following=35)
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=60)
    session.set_do_like(enabled=True, percentage=100)
    session.set_comments([u"Beautiful place!😍😍😍 @{}", u"Nice photo!💯💯💯 !@{}", u"You have a nice page!🔥🔥🔥 @{}"], media='Photo')
    session.set_skip_users(skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
    session.set_delimit_commenting(enabled=True, comments_mandatory_words=['home','duplex','dreamhome', 'house', 'apartment', 'airbnb', 'condo', 'department','townhome','estate'])
    session.set_mandatory_language(enabled=True, character_set='LATIN')
    #session.set_do_comment(enabled=False, percentage=80)
    #session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')


    # activity

    #session.interact_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=True)
    #session.follow_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=False, interact=True)
    #session.unfollow_users(amount=1000, nonFollowers=True, style="LIFO", unfollow_after=0, sleep_delay=501)
    #session.unfollow_users(amount=1000, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=0, sleep_delay=501)
    session.like_by_tags(['austinrentals'], amount=1000, interact=True)
    #session.like_by_tags(['austinairbnb'], amount=1000)
    #session.unfollow_users(amount=7500, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=3)
