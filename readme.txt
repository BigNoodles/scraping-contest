Celebrity Scraper
for questions, email damianhamilton25@hotmail.com


Immediately after opening the zip file, I noticed that the names I recognized 
all seemed to have something to do with the history of Computer Science.

My first thought was to wonder if I could build an "intelligent" script that 
would come to the same conclusion.  I looked at the Page Source and saw it 
would be straightforward to scrape Wikipedia's "normal category" information 
from the bottom of each page and do a word count.

At first I wanted to enforce a rule that each page *must* include a keyword
for it to be considered, but it turns out that Blaise Pascal ruins that idea
because the words "computer" and "science" don't appear in his categories
despite his work on mechanical calculation.  So, I amended my plan to just 
look at a Union of all categories, rather than an Intersection.

BeautifulSoup to parse and collections for the Counter were obvious.  I also
thought that a script like this would likely have real-world application 
scraping large, unknown numbers of real wikipedia pages, so I made get_soup
into a Generator function to preserve memory.

For this "what do these people have in common?" task text output seemed fine,
but you specified data visualization so I added some code to plot a bar graph.

