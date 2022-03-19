import vlc
import pafy
import urllib.request
import time

#url = "https://www.youtube.com/watch?v=Yt-OUrx6KPI&ab_channel=MindstormFan"

#url = "https://www.youtube.com/watch?v=f3gxLlOYNzk&ab_channel=MindstormFan"

#url = "https://www.youtube.com/watch?v=vsnrEY7g6Tg&list=RDvsnrEY7g6Tg&start_radio=1&ab_channel=zfk110"

#url = "https://www.youtube.com/watch?v=u5bQNAYTv_4&ab_channel=GaaneNayePurane"

#url = "https://www.youtube.com/watch?v=_2I6inFlQR4&ab_channel=mastkalandr"

url = "https://www.youtube.com/watch?v=gGbYRMqGGsU&ab_channel=crazyoldsongs"

video = pafy.new(url)
best = video.getbest()
playurl = best.url
ins = vlc.Instance()
player = ins.media_player_new()

code = urllib.request.urlopen(url).getcode()
if str(code).startswith('2') or str(code).startswith('3'):
    print('Stream is working')
else:
    print('Stream is dead')

Media = ins.media_new(playurl)
Media.get_mrl()
player.set_media(Media)

ts = time.time()
print(ts)

player.play()

good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]

ts = time.time()
print(ts)

while str(player.get_state()) in good_states:
	pass
print('Stream is not working. Current state = {}'.format(player.get_state()))
player.stop()	
	