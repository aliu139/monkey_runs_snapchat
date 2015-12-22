from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

def openApp (p_name, a_name):
	apk_path = device.shell('pm path ' + p_name)
	if apk_path.startswith('package:'):
		print p_name + " installed"
	else:
		print "need to install app"

	runComponent = p_name + "/" + a_name
	device.startActivity(component=runComponent)

def takeSnap ():
	device.touch(725,2380, 'DOWN_AND_UP')

def hitSend ():
	device.touch(1275, 2445, 'DOWN_AND_UP')

def navigateTo (userName):
	device.touch(135, 2420, 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	device.touch(1150, 210, 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	device.type(userName)
	MonkeyRunner.sleep(2)
	device.drag((300,430), (1350, 430), 0.1, 2)
	MonkeyRunner.sleep(2)

def sendSnapWithMessage(message):
	hitSend()
	MonkeyRunner.sleep(2)
	takeSnap()
	MonkeyRunner.sleep(2)
	device.touch(700,1300, 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	device.type(message)
	MonkeyRunner.sleep(2)
	device.touch(700, 650, 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	result = device.takeSnapshot()
	result.writeToFile('~/snaps/sent.png','png')
	hitSend()
	MonkeyRunner.sleep(2)	

def returnToMain():
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

def snap(userName, message_text):
	navigateTo(userName)
	sendSnapWithMessage(message_text)
	returnToMain()
	MonkeyRunner.sleep(1)

def seeAndSave(userName):
	navigateTo(userName)
	device.touch(125, 500, 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	result = device.takeSnapshot()
	result.writeToFile('~/snaps/saved.png','png')

def sendMessage(userName, message_text_2):
	navigateTo(userName)
	device.touch(160, 2440, 'DOWN_AND_UP')
	device.type(message_text_2)
	#not finished yet

openApp('com.snapchat.android', 'com.snapchat.android.LandingPageActivity')
MonkeyRunner.sleep(5)

# friends = ['jam']
# for f in friends:
# 	snap(f, 'totallyautomatedsnap')
