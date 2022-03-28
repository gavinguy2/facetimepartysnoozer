from pydub import AudioSegment
from pydub.playback import play
import random
def faceTimePartySnoozer():
    snooz1 = AudioSegment.from_mp3("/home/gavin/Desktop/Master_Folder/python/Snoozer/Sounds_Good.mp3")
    snooz2 = AudioSegment.from_mp3("/home/gavin/Desktop/Master_Folder/python/Snoozer/I_Understand.mp3")
    snooz3 = AudioSegment.from_mp3("/home/gavin/Desktop/Master_Folder/python/Snoozer/OK.mp3")
    snooz4 = AudioSegment.from_mp3("/home/gavin/Desktop/Master_Folder/python/Snoozer/Sure_why_not.mp3")
    snooz5 = AudioSegment.from_mp3("/home/gavin/Desktop/Master_Folder/python/Snoozer/Thanks_For_Coming.mp3")
    snoozers = [snooz1, snooz2,snooz3,snooz4,snooz5]
    randNum = random.randint(0, 4)
    play(snoozers[randNum])
faceTimePartySnoozer()
