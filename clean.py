from unidecode import unidecode
import sys

with open("cybercorpus.txt", "rb") as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    try:
    	sys.stdout.write(unidecode(c))
    except:
    	pass