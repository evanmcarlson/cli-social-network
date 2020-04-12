class PersonClass:
	#Initialize
	def __init__(self, user):
		self._username = user[0]
		self._password = user[1]
		
		for i in range(0, len(user)):
			if user[i] == 'friends':
				self._statuses = user[3 : i]
				self._friends = user[i + 1 : len(user)]

	#Getters
	def getUsername(self):
		return self._username

	def getPassword(self):
		return self._password

	def getStatuses(self):
		return self._statuses

	def getFriends(self):
		return self._friends

	#Setters
	def setStatus(self, newStatus):
		self._statuses.append(newStatus)

	def setFriend(self, newFriend):
		self._friends.append(newFriend)

	#Str
	def __str__(self):
		outputstring = 'Username: ' + self._username + '\n' + 'Password: ' + self._password + '\n' + 'Statuses: ' + str(self._statuses) + '\n' + 'Friends: ' + str(self._friends)
		return outputstring



