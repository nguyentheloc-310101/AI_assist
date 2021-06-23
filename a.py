import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
import wikipedia
import os
import random

today = date.today()
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain  ="  "

def startGoogle():
    global run
    run = False
    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')  




def startgarena():
    global run
    run = False
    os.startfile('C:\Program Files (x86)\Garena\Garena\Garena.exe')  

def startvalorant():
    global run
    run = False
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT')  



def playmusic():
    global run
    music_dir = 'D:\\AllMusic'          
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[0]))
    run = False

def wiki(keyword):
    speak('searching on wikipedia')
    try:
        print('**Result from wiki**')
        print(wikipedia.summary(keyword))      
    except:
        print('Some error occurred! Try again.')
        print('')
    run = False





while True:
	with speech_recognition.Microphone() as mic:
	 	   print("Robot: i'm listening")
	 	   audio =robot_ear.record(mic, duration=3)
	 	   robot_ear.adjust_for_ambient_noise(mic) 
	print(" robot:... ")

	try:
	   you = robot_ear.recognize_google(audio)
	except:
		you=" i can't hear clearly"

	print("you: "+ you)
	###############


	if you ==" ":
	     robot_brain= " i can hear you, try  again"
	elif "hello"in you:
	     robot_brain = " Hello master,  nice to see you,   i'm ready for your recommendation "
	elif  "fun" in you :
		
		with open('joke.txt', 'r') as file:
			 jokelist = file.read().split("\n*")
			
			 joke = str(random.choice(jokelist))
			 robot_content = joke
			 robot_brain=robot_content
	

	elif "date" in you:
	     today = date.today()
	     robot_brain=today.strftime("%B %d, %Y")

	elif "shooting" in you:
		robot_brain = " yes sir, valorant is  opening, dead game"
		startvalorant()
	elif "master"  in you:
	     robot_brain= "my  master is Loc Nguyen, he's very handsome because he created me"

	elif "anyone else" in you:
		 robot_brain=" hmmmmmm, maybe more but i don't know, i'm sorry"
	elif "many times" in you:
		 robot_brain="no problem master, my life is you, i was borned in order to dedicate all i have to you"
	elif  "time" in you:
	     now = datetime.now()
	     robot_brain= now.strftime("%H hours:%M mins:%S secs")
	elif "can you suggest me " in you:
		robot_brain="okay, there are some games that i think they are very interesting. However"
		robot_brain=" i just able to run two games that Valorant and turn on Garena for you, or if you want to open Google Chrome, i will do it for you"

	
	elif "checking" in you:
		robot_brain = "let's have a check"
		
		def isPal(string):
				if(len(string))<=1:
					return True
				if string[0]==string[len(string)-1]:
					return isPal(string[1:len(string)-1])
				else:
					return False
		nhapso=input("ENTER THE NUMBER YOU WANNA CHECK  ")
		if isPal(nhapso):
			print(nhapso, " is Palindrome Number")
		else:
			print("NOT PALINDROME NUMBER ")

	elif "are you stupid" in you:
		robot_brain = " the one who ask me like that is the person that no one can take the top 1 of the stupid mode from him"
	elif"game"in you:
		robot_brain= "yes sir, garena is opening"
		startgarena()
	elif "even or odd" in you:
		robot_brain=" enter the number you wanna check"
		print("nhap so di ma: ")
		number = int(input())
		#if number % 2=0 
			#robot_brain="this is the even number"
		#elif number==0
			#robot_brain =" this is not either odd or even number"
		#else
			#robot_brain =" this is an odd number "
	elif "how are you" in you:
		robot_brain ="i'm ok or not, that depend on your computer battery, sir"
	elif "something" in  you:
		robot_brain="wikipedia is ready, please type something that you wanna look up"
		wiki()

	elif "bye"  in you:
		robot_brain = " goodbye master, have a good day"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif " xin chào" in you:
		robot_brain ="xin chào"
   
	elif "music" in you:
		robot_brain=" yes sir, music on"
		playmusic()
	elif "friends" in you:
		robot_brain= "yeah, the two-stupid are Hoang and KD7"
	elif "mom" in you:
		robot_brain= " why you  ask me that easy question, she is Nguyen Thi Thu Hong"
	elif "open" in you:
		robot_brain = "yes sir,google chrome is bring turning on"
		startGoogle()
	else:
	      robot_brain = "i'm sorry, i'm not programed to answer that question! and maybe there is some noise that refuse the sound"
	
	print( "robot:  "   + robot_brain)


	rate = robot_mouth.getProperty('rate')   
	                      
	robot_mouth.setProperty('rate', 150)   

	voices = robot_mouth.getProperty('voices')       
	  
	robot_mouth.setProperty('voice', voices[1].id)   

	robot_mouth.say(robot_brain)

	robot_mouth.runAndWait()
	robot_mouth.stop()



	  