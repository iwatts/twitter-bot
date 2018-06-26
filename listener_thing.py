# listener_thing.py

# Link for mySQL db connector:
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

# Basic commands as functions, acceptable param listeners

# For Reference: https://github.com/JakeCooper/Zork/blob/master/Zork.py

# exitCmd = re.compile('(?:Exit|Quit|Close|End|Suicide)', flags=re.IGNORECASE)
# examineCmd = re.compile('(?:Look at|Examine|Inspect) (\w+)', flags=re.IGNORECASE)
# moveCmd = re.compile('(?:Move|Go|Travel) (\w+)', flags=re.IGNORECASE)
# inventoryCmd = re.compile('(?:Inventory|Items)', flags=re.IGNORECASE)
# helpCmd = re.compile('(?:Help|H|\?|-H|-Help)(.*)', flags=re.IGNORECASE)


# if examineCmd.match(cmd):
# 		#Will not match with "examine". Need "examine what?" response, fix regex.
# 		cmdParams = examineCmd.match(cmd).groups()
# 		if cmdParams[0] == " ":
# 			print("Examine what?")
# 		elif cmdParams[0].lower() == 'room':
# 			hero.room.examine()
# 		else:
# 			print("There is no {0} around here".format(cmdParams[0])) if not cmdParams[0].endswith("s") else print("There are no {0} around here".format(cmdParams[0])) #Crappy plural checker statement
