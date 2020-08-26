# Web-Crawler
A web crawler in python to automate the job searching process on indeed.com. 

## Usage:
At the moment, the script is written to search for Software Engineering Jobs with 
no more than 2 years of experience. 

You can change the job title in the main() method to anything you want and use it
to crawl jobs on indeed.com. 

Also, for changing the max years of experience per your needs, just edit the
regex value for "p1" variable in criteria_matches() method. Currently, it is
set to jobs with less than 2 years of professional experience, which met my needs
at the time I wrote the script.

Finally, since the script uses Python beautiful soup to do the filtering and 
html page handling, you can easily tweak the script and add or remove filters.

NOTE: This web crawler was built to work on indeed.com only. However, in theory,
you can use the concepts there and built one for almost any job board site given
that you understand their HTML and url structure.

I hope this is useful for you case :)
