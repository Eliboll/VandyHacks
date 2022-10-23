## Inspiration
The average American typically has about four credit cards. Each of these credit cards have differing benefits such as varying cash back rewards. It can be difficult to keep track of which credit card to use at different businesses in order to maximize cash back opportunities, which is why we created Max Cash. 
## What it does
Max Cash uses the physical GPS location of your mobile device to determine which rewards credit card you own will give the best cash back rewards at any given business.
## How we built it
Max Cash is split into two distinct segments. A backend API and a front end. The backend API utilizes python’s Flask framework to take in a user ID and GPS coordinates. It then utilizes Google’s Places API to determine what kind of establishment category is at the GPS coordinates. It then searches in a SQLite database to determine which credit cards an individual has. Using that list of credit cards, and the category the location is in, the backend then determines which credit card you should use to maximize your cashback rate. It then sends a API response back to the front end, as well as an SMS text message using Twilio.

The front end was intended to be built on the Ionic framework allowing for the application to be cross platform. This would have allowed for integration across all major platforms. Unfortunately, we were unable to implement the ability to change users in the react application in the given time, so we prototyped an android application using MIT's app inventor to mimic the desired functionality of the react design.
## Challenges we ran into
We were not familiar with web development/mobile development, so we learned all of the concepts in such a short period of time. We also ran into language structure issues, without a clear understanding of concepts like promises in Javascript. We also experienced issues with the tools we used. For example, Android studio had difficulties syncing changes from the code, into the android emulator. We also had issues with deprecation of features in ionic around packages relating to the GPS data we were trying to get from the device.

As for the backend, the biggest challenge was navigating the documentation of the services we were using, and adapting our design around their restraints.
## Accomplishments that we're proud of
We were proud when we first turned a GPS location into a category. We then were proud when we figured out, given a list of credit cards, which one was the best based on the location. Similarly, we were very proud when we enabled it to know which credit cards a user had, and only look at those. Then finally, we were most proud when our final application prototype worked as intended.
## What we learned
We learned a lot about backend APIs, both using them, and producing them. We learned a lot about web development, both using angular and ionic. We reinforced working in teams, and collaborating with others.
## What's next for Max Cash
Next for Max Cash would be having the application run passively in the background, and detect when the location you are at has changed. Max cash could send you a text within minutes of walking into a store without any user input. Max cash could also be more customizable, with users being able to enter their own rewards cards or less common credit cards. 
