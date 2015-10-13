


import subprocess
import random
import math


with open("Oppgave.py", "w") as file:
	file.write("import time\n")
	for i in range(100):
		stt = "print(\"Epoch {0}: {1} / {2}\")\n".format(i, random.randint(75,107), 107)
		file.write(stt)
		file.write("time.sleep(1)\n")
		
	
subprocess.call(['python', './Oppgave.py'])