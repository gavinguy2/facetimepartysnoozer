from pydub import AudioSegment
from pydub.playback import play
import random
def faceTimePartySnoozer():
    snooz1 = AudioSegment.from_mp3("Sounds_Good.mp3")
    snooz2 = AudioSegment.from_mp3("I_Understand.mp3")
    snooz3 = AudioSegment.from_mp3("OK.mp3")
    snooz4 = AudioSegment.from_mp3("Sure_why_not.mp3")
    snooz5 = AudioSegment.from_mp3("Thanks_For_Coming.mp3")
    snoozers = [snooz1, snooz2,snooz3,snooz4,snooz5]
    randNum = random.randint(0, 4)
    play(snoozers[randNum])
faceTimePartySnoozer()
