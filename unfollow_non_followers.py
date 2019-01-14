"""
What does this quickstart script aim to do?
- My settings is for running InstaPY 24/7 --> it will unfollow all nonfollowers of the registered user.
"""


from instapy import InstaPy
from instapy.util import smart_run


# get a session!
session = InstaPy(username='', password='', disable_image_load=True, multi_logs=True,  bypass_suspicious_attempt=True, headless_browser=True, nogui=True)


# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=False, potency_ratio=0.0, max_followers=12000, max_following=4500, min_followers=35, min_following=35)
    session.set_skip_users(skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)

    session.set_mandatory_language(enabled=True, character_set='LATIN')
    

    # activity

    #session.interact_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=True)
    #session.follow_user_followers(['user1', 'user2', 'user3'], amount=8000, randomize=False, interact=True)
    session.unfollow_users(amount=1000, nonFollowers=True, style="LIFO", unfollow_after=0, sleep_delay=501)
    #session.unfollow_users(amount=1000, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=0, sleep_delay=501)
