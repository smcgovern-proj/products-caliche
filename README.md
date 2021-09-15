# Intro
This repo showcases my work on the backend "products" service for a MERN-stack ecommerce app. In short, I was given some rather large, messy .csv files and asked to load them into a MongoDB database, as well as hook up an Express backend that would serve a few basic GET requests. 

![Screen Shot 2021-09-15 at 12 37 09 AM (2)](https://user-images.githubusercontent.com/84145162/133371600-f29c2773-4979-4cf1-b1b1-27dfa33106eb.png)


# Dev Process
Though I'm not very familiar with Python, I ended up using a tool called [pandas](https://pandas.pydata.org/) to clean my .csv files and do a couple SQL-style joins on the data. As someone who feels most comfortable with JS/CSS on the frontend, teaching myself as I went was an equally rewarding and difficult experience. Luckily, doing that work upfront made writing the actual endpoints in Express relatively trivial. It also led to fairly quick operations! I didn't have to do much work with aggregations pipelines and the like, as my data was largely in the shape I already wanted it to be. At the end of the day, I was able to bring the median response time to well under 100ms at a sustained, 1000 request per second load.
