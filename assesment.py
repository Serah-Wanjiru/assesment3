class Storytelling:
    def __init__(self,oralStory,language,storyTeller):
        self.oralStory=oralStory
        self.language=language
        self.storyTeller=storyTeller
    
    def getStories(self):
        print(f"{self.StoryTeller} purin gave us {self.oralStory} that was written in kikuyu language but She translated to {self.language}")
        
        
    

storytelling=Storytelling("Being submissive to the husband during back day","kiswahili","GrandMa Purin")
storytelling.getStories()
class MyStory(Storytelling):
    def __init__(self,length,moralLessons,ageGroup):
        self.length=length      
        self.moralLessons=moralLessons
        self.ageGroup=ageGroup
    
    def getDetailsOfStory():
        print(f"{self.oralStory} it was narated to us {self.storyTeller} from english to {self.language} which took {self.length} the targeted listeners were girls who were between {self.ageGroup} and above and the most important moral lessons were {self.moralLessons}"):


    
    

mystory=MyStory("one hour","Stand with your values","16yrs")
mystory.getDetailsOfStory() 


# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
class LibraryCatalog{
    def __init__(self,book){
        self.book=[]
    }
    def addNewbook(){
        self.book=[{title:"Kigogo",author:"Pauline Kea",pages:286}]


    }
    def displayBookDetails(){
        print(f"{self.book.title1} was purchased on september");


    }
}
library=LibraryCatalog([
   t= {title1:"The blossoms of the savannah",author:"Hr.Ole Kulet",pages:286},
    {title2:"Decolonise mind",author:"Ngugi wa Thiongo",pages:286},
    {title3:"River And The Source",author:"Margaret",pages:286},
    {title4:"Tumbo Lisiloshiba",author:"Dumu kayamba",pages:286}
])
library.addNewbook()
library.displayBookDetails()

# //Create a FlightBooking class that represents a flight booking system. Implement
# //methods to search for available flights based on destination and date, reserve
# //seats for customers, manage passenger information, and generate booking
# //confirmations.
class FlightBooking:
   def __init__ (self destination,date,seats,information,booking):
        self.destination=destination
        self.date=date
        self.seats=seats
        self.information=information
        self.booking=booking
    
   def availableFlight():
        print(f"The fly Emirate plane will will fly in {self.date} to {self.destination} who ever had given {self.booking} with ${self.information} will seat in {self.seats} the plane will be available for you"):
    

flightBooking=FlightBooking("Eldorect","12.july.2023","infront seats","morning travelling","morning booking")
flightBooking.availableFlight()

# //Create a class called Product with attributes for name, price, and quantity.
# //Implement a method to calculate the total value of the product (price * quantity).
# //Create multiple objects of the Product class and calculate their total values.
class Products:
 
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
empty=[]       
products=Products("milk",200,4) 
empty.append(products)       
        
def totalPrice(self):
    
        for items in empty:
            items.price*items.quantity
print(items) 