import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'umcasalpelobrasil'
insta_password = 'Vsm2029&'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                password=insta_password,
                headless_browser=True)

try:
        session.login()

    # settings
        session.set_skip_users(skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
        session.set_relationship_bounds(enabled=True,
                               potency_ratio=None,
                                  delimit_by_numbers=True,
                                   max_followers=10000,
                                    max_following=3000,
                                        min_followers=100,
                                      min_following=100)
        session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
        session.set_do_follow(enabled=True, percentage=100)
        session.set_do_like(enabled=True, percentage=100)
        session.set_do_comment(enabled=True, percentage=20)
        session.set_comments([u'📷🔝👏✌️',u'📷❤️🙏🔝👏',u'❤️📷🔝🙌',u'🔝📷❤️👏'])
        session.set_quota_supervisor(enabled=True, sleep_after=["likes"], sleepyhead=True, stochastic_flow=True, notify_me=False,
                              peak_likes=(90, 2070),
                               peak_comments=(None, None),
                                peak_follows=(30, 690),
                                 peak_unfollows=(None, 500),
                                  peak_server_calls=(None, None))

    # actions
        session.interact_user_followers(['topofbrazil'], amount=100, randomize=True)
        session.interact_user_followers(['viagensdagueu'], amount=100, randomize=True)
        session.interact_user_followers(['caiotravels'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['blogumviajante'], amount=100, randomize=True)
        session.interact_user_followers(['vamospraonde'], amount=100, randomize=True)
        session.interact_user_followers(['liviajando'], amount=100, randomize=True)
        session.interact_user_followers(['estevampelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['aninha_pt'], amount=100, randomize=True)
        session.interact_user_followers(['essemundoenosso'], amount=100, randomize=True)
        session.interact_user_followers(['vibe_natureza'], amount=100, randomize=True)
        session.interact_user_followers(['destinosesonhos'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['nosnatrip'], amount=100, randomize=True)
        session.interact_user_followers(['tripadoiss'], amount=100, randomize=True)
        session.interact_user_followers(['marcionomundo'], amount=100, randomize=True)
        session.interact_user_followers(['brasilclique'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomsy'], amount=100, randomize=True)
        session.interact_user_followers(['alemaoviajante'], amount=100, randomize=True)
        session.interact_user_followers(['brazilmaravilhas'], amount=100, randomize=True)
        session.interact_user_followers(['trilheiros_do_brasil'], amount=100, randomize=True)
        session.interact_user_followers(['mturismo'], amount=100, randomize=True)
        session.interact_user_followers(['nordestemeulindo'], amount=100, randomize=True)
        session.interact_user_followers(['douglasviajante'], amount=100, randomize=True)
        session.interact_user_followers(['pernambucolovers'], amount=100, randomize=True)
        session.interact_user_followers(['amoonordeste'], amount=100, randomize=True)
        session.interact_user_followers(['tourpelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['gostariadeiroficial'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['sejogacomigo'], amount=100, randomize=True)
        session.interact_user_followers(['eupraiana'], amount=100, randomize=True)
        session.interact_user_followers(['destinosimperdiveis'], amount=100, randomize=True)
        session.interact_user_followers(['vivendoepostando'], amount=100, randomize=True)
        session.interact_user_followers(['topofbrazil'], amount=100, randomize=True)
        session.interact_user_followers(['viagensdagueu'], amount=100, randomize=True)
        session.interact_user_followers(['caiotravels'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['blogumviajante'], amount=100, randomize=True)
        session.interact_user_followers(['vamospraonde'], amount=100, randomize=True)
        session.interact_user_followers(['liviajando'], amount=100, randomize=True)
        session.interact_user_followers(['estevampelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['aninha_pt'], amount=100, randomize=True)
        session.interact_user_followers(['essemundoenosso'], amount=100, randomize=True)
        session.interact_user_followers(['vibe_natureza'], amount=100, randomize=True)
        session.interact_user_followers(['destinosesonhos'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['nosnatrip'], amount=100, randomize=True)
        session.interact_user_followers(['tripadoiss'], amount=100, randomize=True)
        session.interact_user_followers(['marcionomundo'], amount=100, randomize=True)
        session.interact_user_followers(['brasilclique'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomsy'], amount=100, randomize=True)
        session.interact_user_followers(['alemaoviajante'], amount=100, randomize=True)
        session.interact_user_followers(['brazilmaravilhas'], amount=100, randomize=True)
        session.interact_user_followers(['trilheiros_do_brasil'], amount=100, randomize=True)
        session.interact_user_followers(['mturismo'], amount=100, randomize=True)
        session.interact_user_followers(['nordestemeulindo'], amount=100, randomize=True)
        session.interact_user_followers(['douglasviajante'], amount=100, randomize=True)
        session.interact_user_followers(['pernambucolovers'], amount=100, randomize=True)
        session.interact_user_followers(['amoonordeste'], amount=100, randomize=True)
        session.interact_user_followers(['tourpelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['gostariadeiroficial'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['sejogacomigo'], amount=100, randomize=True)
        session.interact_user_followers(['eupraiana'], amount=100, randomize=True)
        session.interact_user_followers(['destinosimperdiveis'], amount=100, randomize=True)
        session.interact_user_followers(['vivendoepostando'], amount=100, randomize=True)
        session.interact_user_followers(['topofbrazil'], amount=100, randomize=True)
        session.interact_user_followers(['viagensdagueu'], amount=100, randomize=True)
        session.interact_user_followers(['caiotravels'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['blogumviajante'], amount=100, randomize=True)
        session.interact_user_followers(['vamospraonde'], amount=100, randomize=True)
        session.interact_user_followers(['liviajando'], amount=100, randomize=True)
        session.interact_user_followers(['estevampelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['aninha_pt'], amount=100, randomize=True)
        session.interact_user_followers(['essemundoenosso'], amount=100, randomize=True)
        session.interact_user_followers(['vibe_natureza'], amount=100, randomize=True)
        session.interact_user_followers(['destinosesonhos'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['nosnatrip'], amount=100, randomize=True)
        session.interact_user_followers(['tripadoiss'], amount=100, randomize=True)
        session.interact_user_followers(['marcionomundo'], amount=100, randomize=True)
        session.interact_user_followers(['brasilclique'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomsy'], amount=100, randomize=True)
        session.interact_user_followers(['alemaoviajante'], amount=100, randomize=True)
        session.interact_user_followers(['brazilmaravilhas'], amount=100, randomize=True)
        session.interact_user_followers(['trilheiros_do_brasil'], amount=100, randomize=True)
        session.interact_user_followers(['mturismo'], amount=100, randomize=True)
        session.interact_user_followers(['nordestemeulindo'], amount=100, randomize=True)
        session.interact_user_followers(['douglasviajante'], amount=100, randomize=True)
        session.interact_user_followers(['pernambucolovers'], amount=100, randomize=True)
        session.interact_user_followers(['amoonordeste'], amount=100, randomize=True)
        session.interact_user_followers(['tourpelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['gostariadeiroficial'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['sejogacomigo'], amount=100, randomize=True)
        session.interact_user_followers(['eupraiana'], amount=100, randomize=True)
        session.interact_user_followers(['destinosimperdiveis'], amount=100, randomize=True)
        session.interact_user_followers(['vivendoepostando'], amount=100, randomize=True)
        session.interact_user_followers(['topofbrazil'], amount=100, randomize=True)
        session.interact_user_followers(['viagensdagueu'], amount=100, randomize=True)
        session.interact_user_followers(['caiotravels'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['blogumviajante'], amount=100, randomize=True)
        session.interact_user_followers(['vamospraonde'], amount=100, randomize=True)
        session.interact_user_followers(['liviajando'], amount=100, randomize=True)
        session.interact_user_followers(['estevampelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['aninha_pt'], amount=100, randomize=True)
        session.interact_user_followers(['essemundoenosso'], amount=100, randomize=True)
        session.interact_user_followers(['vibe_natureza'], amount=100, randomize=True)
        session.interact_user_followers(['destinosesonhos'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['nosnatrip'], amount=100, randomize=True)
        session.interact_user_followers(['tripadoiss'], amount=100, randomize=True)
        session.interact_user_followers(['marcionomundo'], amount=100, randomize=True)
        session.interact_user_followers(['brasilclique'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomsy'], amount=100, randomize=True)
        session.interact_user_followers(['alemaoviajante'], amount=100, randomize=True)
        session.interact_user_followers(['brazilmaravilhas'], amount=100, randomize=True)
        session.interact_user_followers(['trilheiros_do_brasil'], amount=100, randomize=True)
        session.interact_user_followers(['mturismo'], amount=100, randomize=True)
        session.interact_user_followers(['nordestemeulindo'], amount=100, randomize=True)
        session.interact_user_followers(['douglasviajante'], amount=100, randomize=True)
        session.interact_user_followers(['pernambucolovers'], amount=100, randomize=True)
        session.interact_user_followers(['amoonordeste'], amount=100, randomize=True)
        session.interact_user_followers(['tourpelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['gostariadeiroficial'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['sejogacomigo'], amount=100, randomize=True)
        session.interact_user_followers(['eupraiana'], amount=100, randomize=True)
        session.interact_user_followers(['destinosimperdiveis'], amount=100, randomize=True)
        session.interact_user_followers(['vivendoepostando'], amount=100, randomize=True)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)
        session.interact_user_followers(['topofbrazil'], amount=100, randomize=True)
        session.interact_user_followers(['viagensdagueu'], amount=100, randomize=True)
        session.interact_user_followers(['caiotravels'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['blogumviajante'], amount=100, randomize=True)
        session.interact_user_followers(['vamospraonde'], amount=100, randomize=True)
        session.interact_user_followers(['liviajando'], amount=100, randomize=True)
        session.interact_user_followers(['estevampelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['aninha_pt'], amount=100, randomize=True)
        session.interact_user_followers(['essemundoenosso'], amount=100, randomize=True)
        session.interact_user_followers(['vibe_natureza'], amount=100, randomize=True)
        session.interact_user_followers(['destinosesonhos'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['nosnatrip'], amount=100, randomize=True)
        session.interact_user_followers(['tripadoiss'], amount=100, randomize=True)
        session.interact_user_followers(['marcionomundo'], amount=100, randomize=True)
        session.interact_user_followers(['brasilclique'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomsy'], amount=100, randomize=True)
        session.interact_user_followers(['alemaoviajante'], amount=100, randomize=True)
        session.interact_user_followers(['brazilmaravilhas'], amount=100, randomize=True)
        session.interact_user_followers(['trilheiros_do_brasil'], amount=100, randomize=True)
        session.interact_user_followers(['mturismo'], amount=100, randomize=True)
        session.interact_user_followers(['nordestemeulindo'], amount=100, randomize=True)
        session.interact_user_followers(['douglasviajante'], amount=100, randomize=True)
        session.interact_user_followers(['pernambucolovers'], amount=100, randomize=True)
        session.interact_user_followers(['amoonordeste'], amount=100, randomize=True)
        session.interact_user_followers(['tourpelomundo'], amount=100, randomize=True)
        session.interact_user_followers(['gostariadeiroficial'], amount=100, randomize=True)
        session.interact_user_followers(['viajandocomgabi'], amount=100, randomize=True)
        session.interact_user_followers(['mundodosviajantes'], amount=100, randomize=True)
        session.interact_user_followers(['sejogacomigo'], amount=100, randomize=True)
        session.interact_user_followers(['eupraiana'], amount=100, randomize=True)
        session.interact_user_followers(['destinosimperdiveis'], amount=100, randomize=True)
        session.interact_user_followers(['vivendoepostando'], amount=100, randomize=True)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)
        session.unfollow_users(amount=500, allFollowing=True, style="LIFO", unfollow_after=None, sleep_delay=60)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
