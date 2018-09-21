def hi():
	print("Hello Mr. Jones! How are you today?")
	print("Helloyou today?")

def hello(name):
	print("Hello ",name," How are you today?")
	print("Helloyou today?")

def hello1(name="Sir"):
	print("Hello ",name," How are you today?")
	print("Helloyou today?")

def get_distance(speed, duration):
	distance_in_kilometers = speed * duration
	distance_in_meters = distance_in_kilometers * 1000
	return distance_in_meters

print(get_distance(50,3))
print(get_distance(100,5))

hello("Mr. XYZ")
hello1()
hello1("Guest")
hi()

