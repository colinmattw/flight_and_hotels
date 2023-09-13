# Flight_and_Hotels
**Quick weekend project I made to analyze hundreds of international cities as potential travel destinations for my girlfriend and I. Used Selenium to create two webscraping programs that collected flight and hotel price data on hundreds of cities during a specific date range. This project was done quickly to accomplish one task and was not meant to be polished or readable.**
---------------------------------------------------
**Created by Colin M Wareham**
---------------------------------------------------
This project introduced me to a few new concepts in programming as well refined existing ones:
1. Using OS based macros in Python
2. Using Selenium in Python for web automation
3. Extensive regex usage with HTML
4. Google Chrome developer tools to identify information in web pages
5. Using ChatGPT to create hard-to-obtain datasets
6. More practice with data pre and post-processing


Description:

Since my girlfriend lives in South Korea, I had the goal of finding the best city in the world for us to travel to during a specific date range. Since we would be splitting all costs 50/50, I wanted to find the city with the cheapest combined price of our tickets, and also not too long travel time for either of us. I would also look at the average prices of hotels in each city.

I started by finding a list of countries we could both travel to without a visa. There were 122 countries. Then, I had ChatGPT give me the raw txt list of each country's capital city, I then asked ChatGPT for the next 3 largest cities in each country, if it couldn't find all 3, it would list as many as it could. There were about 277 cities in total. I then fed this raw txt list of cities into a python program I wrote which uses Selenium and OS based macros to navigate to google.com/travel/flights. From there, the program would search for flights out of Chicago and Seoul to the destination city, during the specific date range. It would record both the shortest and cheapest flight it could find in two seperate lists. One that looked for the best flight time, and another that looked for the best price.

Finally, I made another webscraping program that navigated to booking.com and searched for hotels in each city. Booking.com provides a price distribution graphic on the side of the page in the form of vertical bars shaped like a normal distribution. It also says its showing hotels in a price range from x to y. Knowing the price range, and getting the specific shape of the distribution from the HTML, I was able to solve for the average price of a hotel in that city, during that specific date range. I then made a third list with this information.

Finally, I ranked each city by cheapest combined ticket price, shortest journey for the longer of our 2 flights, average hotel price, and population. (Where higher population is a higher rank. I got ChatGPT to give me this info). I then created 3 weighted categories: Total price (cheapest combined ticket price + 8 nights at an average hotel), Shortest flight time for the longer of us two, and population. They were weighted at 45%, 45%, 10% respectively. The results are in an excel sheet in the repo.

