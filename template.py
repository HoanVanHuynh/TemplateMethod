from abc import abstractmethod, ABCMeta 

# The abstract object is represented by the Trip class.
# It is an interface (Python's abstract base class)
# that defines the details such as the transportation used
# and places to visit on different days. 

class Trip(metaclass=ABCMeta):

    # The setTransport is an abstract method that should be implemented by
    # ConcreteClass to set the mode of transportation. 
    # The day1(), day2(), day3() abstract methods define the places visited on the given day.

    @abstractmethod
    def setTransport(self):
        pass 

    @abstractmethod
    def day1(self):
        pass 

    @abstractmethod
    def day2(self):
        pass 

    @abstractmethod
    def day3(self):
        pass 

    @abstractmethod
    def returnHome(self):
        pass 
    
    # The itinerary() Template Method creates the complete itinerary
    # (The algorithm, in this case, the trip) 
    # The sequence of the trip is to first define the transportatin mode,
    # then the places to visit on each day, and the returnHome. 

    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2() 
        self.day3() 
        self.returnHome()

# In this case, we have two main concrete classes 
# VeniceTrip and MaldivesTrip
# that implement the Trip interface 
# Concrete classes represent two different trips taken by the tourists
# based on their choice and interests

class VeniceTrip(Trip):
    def setTransport(self):
        print('Take a boat and find your way in the Grand Canal')
    
    def day1(self):
        print('Visit St Mark s in St')

    def day2(self):
        print('Appreciate Doge Palace')

    def day3(self):
        print('Enjoy th food near the Rialto Bridge')

    def returnHome(self):
        print('Get souvenirs for friends and get back')


class MaldivesTrip(Trip):
    def setTransport(self):
        print('On foot, on any island, Wow!')
    
    def day1(self):
        print('Enjoy the marine life of Banana reef')
    
    def day2(self):
        print('Go for the water sports and snorkelling')

    def day3(self):
        print('Relax on the beach and enjoy the sun')

    def returnHome(self):
        print('Do not feel like leaving the beach...')

# Let's talk about the travel agency and tourists who want to have an awesome vacation:
# The TravelAgency class represents the Client object in this example
# It defines the arrange_trip() method that provides customers with the choice of 
# whether they want to have a historical trip or beach trip. 
# Based on the choce made by the tourist, an appropriate class is instantiated 
# This object then calls the itineracy() Template Method
# and the trip is arranged for the tourists as per the choice of the customers         

# The following is the implementation for the Dev travel agency 
# and how they arrange for the trip based on the customer's choice: 
class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")        
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()

print(TravelAgency().arrange_trip())