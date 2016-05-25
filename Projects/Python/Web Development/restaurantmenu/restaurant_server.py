#setup server
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#setup connection to DB

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem #import classes from databaseSetup file

engine = create_engine('sqlite:///restaurantmenu.db') #lets program know which db engine to connect with
Base.metadata.bind = engine #makes connections between classes and corresponding tables in db

DBSession = sessionmaker(bind = engine) #creates a link between our code and the engine we created

session = DBSession()



class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            #create main page
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                
                for restaurant in session.query(Restaurant):
                    
                    output += "<h1>%s</h1>" % (restaurant.name,)
                    output += "<a href = '/restaurants/%s/edit' >Edit</a>" % restaurant.id
                    output += "<div></div> "
                    output += "<a href = '/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += ""

                for i in range(3):
                    output += "<div></div> &nbsp "
                
                output+= "<a href = '/restaurants/new' style='font-size: 25px' > Make a new restaurant here! </a>"
                output += "</body></html>"

                self.wfile.write(output)
                print output
                return

                #add a new restaurant
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a new restaurant!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name="newRestaurantName" type="text" ><input type="Submit" value="Create"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

                #rename restaurant
            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                if myRestaurantQuery != []:
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Rename %s</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output += "<input name='newRestaurantName' type='text' placeholder = '%s' ><input type='Submit' value='Rename'> </form>" %myRestaurantQuery.name
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return

                #delete restaurant
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                if myRestaurantQuery != []:
                    output = ""
                    output += "<html><body>"
                    output += "<h1> Are you sure you want to delete %s</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type='Submit' value='Delete'> </form>" 
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                #add new restaurant
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()

            #instead of rerunning the home page, use a redirect
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location','/restaurants') #redirect
                self.end_headers()

           
            if self.path.endswith("/edit"):
                
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                #update old restaurant
                oldRestaurant = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                oldRestaurant.name = messagecontent[0]
                session.add(oldRestaurant)
                session.commit()
                

            #instead of rerunning the home page, use a redirect
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location','/restaurants') #redirect
                self.end_headers()


            if self.path.endswith("/delete"):
                
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                #delete restaurant
                oldRestaurant = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                session.delete(oldRestaurant)
                session.commit()
                

            #instead of rerunning the home page, use a redirect
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location','/restaurants') #redirect
                self.end_headers()
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()