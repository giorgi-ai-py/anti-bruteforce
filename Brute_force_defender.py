import time
import os

os.system('clear')
print ("\033[93m" + r"""                              /#################/
                              <#################|
                               \#################\
                                     '"*##########'
                                    _.,+##########'
                               /#################/
                              <#################|
                               \#################\
                                     '"*##########'      this is a key btw
                                    _.,+##########'
                               /#################/
                              <#################|
                               \#################\
                                     '"*##########
                                       /##########\
                                     /#############\
                                  /#########[]########\
                               /#########'      `########\
                              /######'             `######\
                             '####'    Brute force    `####'
                             |###|       Defender      |###|
                             .####.         By        .####.
                              \#####.  Giorg-ai-py  .#####/
                                \#####.           .######/
                                  \######.      .######/
                                    \#######[]#######/
                                       \##########/
""")

CorrectPassword = "supersecret"
MaxAttempts = 3
attempts = 0

for attempt in range(MaxAttempts):
	password = input ("\nEnter password: ")

	if password == CorrectPassword:
		time.sleep(1.5)
		print ("Access Granted! Welcome back.")
		break
	else:
		attempts += 1
		remaining = MaxAttempts - attempts

	if remaining > 0:
		time.sleep(1.5)
		print (f"\nAccess Denied. {remaining} attempts remaining.")
	else:
		time.sleep(1.5)
		print ("Access Denied.")

if attempts == MaxAttempts:
	time.sleep(1)
	print ("\n System alert: account locked. Too many failed attempts.")
	time.sleep(1)
	print ("Contacting administrator...")
