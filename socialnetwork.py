import person
import copy

def main():
	#read in file
	infile = open('network.txt', 'r')
	allLines = infile.readlines()

	#network representation
	users = []

	for line in allLines:

		#the following block of code is to ensure that a 
		#comma or \n is not placed inside of a list value
		line = line.strip()
		line += ' \n'
		line = line.split(', ')

		#a list containing a username, password &
		#two nested lists (statuses and friends)
		users.append(line)

	for i in users:
		i.remove('\n')

	running = True
	while running:

		#user authentication
		authenticated = False

		while not authenticated:
			userInputName = raw_input('Please enter a username: ') #renamed to input() in python 3.x

			for i in users:
				if userInputName == i[0]:
					userInputPass = raw_input('Please enter a password: ')

					if userInputPass == i[1]:
						#assign authenticated user as 'user'
						user = i
						authenticated = True
					else:
						print('Incorrect password')
		
		#object of logged-in user
		userObject = person.PersonClass(user)

		#main menu
		loggedin = True

		while loggedin:
			print('\n1. Print all my friends')
			print('2. Print all my messages/status updates')
			print('3. Post a message/status update')
			print("4. Print all my friends' messages/status updates")
			print('5. Add a friend')
			print('6. Logout/Change user')
			print('7. Search friends')
			print('8. Exit\n')

			command = raw_input('Please enter a number from the menu above: ')

			if command == '1':
				print(userObject.getFriends())

			if command == '2':
				print(userObject.getStatuses())

			if command == '3':
				newStatus = raw_input('Enter a status/message: ')
				userObject.setStatus(newStatus)

			if command == '4':
				for friend in userObject.getFriends():
					for i in users:
						#locate friend by index
						if i[0] == friend:
							#create object & call method for each friend
							friendObject = person.PersonClass(i)
							theirstatus = str(friendObject.getStatuses())
							print(friend + ': ' + theirstatus)

			if command == '5':
				newFriend = input("Enter a friend's name: ")

				#list of all usernames
				people = []
				for i in users:
					people.append(i[0])

				#input validation, essentially
				if newFriend in people:
					for i in users:
						if i[0] == newFriend:
							userObject.setFriend(newFriend)
				else:
					print('This friend is not registered')

			if command == '6':
				loggedin = False

			#EXTRA CREDIT
			if command == '7':
				search = raw_input("Enter a friend's name: ")

				#again, some input validation
				if search in userObject.getFriends():
					for i in users:
						if i[0] == search:
							friendDictionary = {}
							friendObject = person.PersonClass(i)
							friendDictionary[search] = friendObject.getStatuses()
							print(friendDictionary)
				else:
					print('That person is not your friend!')

			if command == '8':
				#copy contents of users list
				updated = copy.deepcopy(users)

				for i in updated:
					#replace logged-in user's info w/ correct format
					if i[0] == userObject.getUsername():
						#remove old info
						del(i[:])
						#add updated info
						i.append(userObject.getUsername())
						i.append(userObject.getPassword())

						i.append('messages')

						for aStatus in userObject.getStatuses():
							i.append(aStatus)

						i.append('friends')

						for aFriend in userObject.getFriends():
							i.append(aFriend)

				infile.close()

				#write out updated file
				outfile = open('network.txt', 'w')

				for i in updated:
					i = ", ".join(i)
					i += ',\n'
					outfile.write(i)

				outfile.close()

				#close program
				loggedin = False
				running = False

main()
