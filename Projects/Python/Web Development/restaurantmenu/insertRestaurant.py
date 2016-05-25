from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem #import classes from databaseSetup file

engine = create_engine('sqlite:///restaurantmenu.db') #lets program know which db engine to connect with
Base.metadata.bind = engine #makes connections between classes and corresponding tables in db

DBSession = sessionmaker(bind = engine) #creates a link between our code and the engine we created

session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")

session.add(myFirstRestaurant) #add python object to staging zone

 secondR = Restaurant(name = "Urban Burger")
 thirdR = Restaurant(name = "Panda Garden")
 fourthR = Restaurant(name = "Tony's Bistro")
 fifthR = Restaurant(name = "Cocina Y Amor")

session.add_all([secondR,thirdR,fourthR,fifthR]) #add multiple objects

session.commit() #commit it to the db

session.query(Restaurant).all()

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()


###########UPDATE###########

#find entry
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers
	print veggieBurger.id
	print veggieBurger.price
	print veggieBurger.restaurant.name
	print "\n"

#find right burger
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one() #returns one item with id = 8

#reset values
UrbanVeggieBurger.price = '2.99'

#add to session
session.add(UrbanVeggieBurger)
session.commit()
#commit


########DELETE #################

#FIND entry
spinach = session.query(MenuItem).filter_by(name = Spinach Ice Cream).one()

#delete
session.delete(spinach)

session.commit()
