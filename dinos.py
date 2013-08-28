#this module is imported for the random number generator
import numpy



class Dinosaur(object):

	current_dinos = 0 #keeps track of the global number of dinosaurs
	#the following lists are pulled from based on indices which are generated randomly each time
	dino_list = [['Stegosaurus', 13, 13] , ['Triceratops', 10, 20], ['Tyrannosaurus Rex', 20, 10], ['Brontosaurus', 10, 10], ['Pteradactyl', 15, 5], ['Velociraptor', 17, 8], ['Walrus', 5,20], ['Robot Ninja Dragon', 30, 30]]
	dino_names = ['Charles', 'Snoop', 'Richard', 'Drake', 'Mac Daddy', 'Barney', 'Pimp Master', 'Octavius', 'Optimus Prime', 'Jason', 'Coolio', 'Paulie D', 'Jasmina']
	
	def __init__(self, RND=False):
		random_dino_list_index = numpy.random.random_integers(0, len(Dinosaur.dino_list)-1)
		random_dino_name_index = numpy.random.random_integers(0, len(Dinosaur.dino_names)-1)
		if RND == False: #this was implemented to allow the specific creation of
						 #Robot Ninja Dragons if desired
			self.identity = Dinosaur.dino_list[random_dino_list_index]
		else:
			self.identity = Dinosaur.dino_list[-1]
		self.name = Dinosaur.dino_names.pop(random_dino_name_index)
		self.strength = self.identity[1]
		self.health = self.identity[2]
		self.victory_count = 0
		Dinosaur.current_dinos += 1
		if self.identity[0] == 'Robot Ninja Dragon':
			print "HOLY S**T. I'M A MOTHERF**KING ROBOT NINJA DRAGON.\nTHIS SHOULDN'T EVEN BE HAPPENING.\nOh and my name's {0}.".format(self.name) 
		elif self.strength >= 13:
			print "ROOOOAAARRRR!!!! My name is {0} and I'm a {1}.".format(self.name, self.identity[0])
		else:
			print "GRRRRR! My name is {0} and I'm a {1}.".format(self.name, self.identity[0])
		self.dead = False
#		self.exp_points = 0
	def __del__(self):
		#This provides flavor text for dinosaur objects which are deleted from memory
		Dinosaur.current_dinos -= 1
		if self.health > 0:
			print "BOOOMMM!! A meteor has landed and {0} is gone!".format(self.name)
	def __add__(self, other):
		#This 'try' loop was put in place to avoid problems with trying to add
		#dinosaurs to other objects, and also to stop dead dinosaurs from fighting
		#these cases are caught in assertion errors
		try:
			assert type(other) is Dinosaur
			assert self.dead != True
			assert other.dead != True
			selection = raw_input("Are you sure you want {0} and {1} to fight?\n".format(self.name, other.name))
			if 'no' in selection:
				print "It would seem cooler heads have prevailed"
			else:
				#These two lines are just battle flavor text
				print "THE DINOSAURS ARE FIGHTING EACHOTHER!!!"
				print "FIGHT! FIGHT! FIGHT!\n"*5

				#the attack strength for a dinosaur in a given battle is
				#random, but is weighted with respect to a dinosaur's strength attribute
				my_attack_strength = (self.strength*numpy.random.random_integers(1, 15))/15
				others_attack_strength = (other.strength*numpy.random.random_integers(1,15))/15
				
				#flavor text for either misses or full strength hits (both of which should occur rarely)
				if others_attack_strength ==  0:
					print "Oh no! {0}'s attack missed.".format(other.name)
				if others_attack_strength == other.strength:
					print "{0} roars loudly as a he attacks with his full strength!".format(other.name)
				if my_attack_strength == 0:
					print "Oh no! {0}'s attack missed.".format(self.name)
				if my_attack_strength == self.strength:
					print "{0} roars loudly as he attacks with his full strength!".format(self.name)
				
				self.health -= others_attack_strength
				other.health -= my_attack_strength

				#should take care of dinosaur deaths and related functional consequences
				#and flavor text
				if other.health < 0:
					other.dead = True #attribute which defaults as False
					Dinosaur.current_dinos -= 1
					print "{0} was defeated in battle!".format(other.name)
				if self.health < 0:
					self.dead = True
					Dinosaur.current_dinos -= 1
					print "{0} was defeated in battle!".format(self.name)

				#in cases where both dinosaurs survive
				if self.health > 0 and other.health > 0:
					print "Both {0} and {1} came away from the fight".format(self.name, other.name)
#					self.exp_points, other.exp_points += 3, 3

				#the victorious case
				if other.health < 0:
					self.victory_count += 1
					print "{0} was victorious.".format(self.name)
#					self.exp_points += 5
		except AssertionError as e:
			print "I'm pretty sure you know {0} can't fight something like that...".format(self.name)


			#implemented for dino bragging rights
	def gloat(self):
		if self.victory_count > 10:
			print "F**k I'm invincible. {0} have gone down because of me.".format(self.victory_count)
		elif self.victory_count > 5:
			print "I'm a stone cold gangsta and I can't be stopped. I've dropped {0} dinos and counting.".format(self.victory_count)
		else:
			print "My name is {0} and I've defeated {1} other dinosaurs in battle!".format(self.name, self.victory_count)

			#currently not in use, but was an attempt at handling dinosaur death
class DeadDino(object):
	health = 0
	def __init__(self, old_name):
		Dinosaur.current_dinos -= 1
		print "{0} was defeated in battle!".format(old_name)

