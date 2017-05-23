## Role of GASP Webmaster

The GASP Webmaster is responsible for maintaining the GASP website at http://sites.utoronto.ca/gasp/ and other social media such as the Facebook page. This will require updates about once a week as event planners make their posters and event details available to update the site or FB page with. This may include but is not limited to social/sports events, GASP academic events, photos from these events, general annoucements pertaining to GASP, relevant information or links for Physiology students. 

As a GASP council member, you must attend the monthly meetings and two other events during the year: 
  1. Help organize the Physiology Holiday Luncheon skit or entertainment along with the other GASP members in December. You will help plan the entertainment prior to the event and potentially help on the day of as well. You are expected to attend the luncheon.
  2. You are committed to helping out at Frontiers in Physiology (FIP), typically held in May which includes a briefing meeting a week or so prior, set-up the night before, and helping out the day of.   
  
Furthermore, as a GASP council member, you will be the first people other GASP members will turn to when they are in need of helpers for their events, so please extend a helping hand when you can.

## Instructions for Maintaining GASP Website:

# Preparation:
- Install Anaconda Python 3.x.x https://www.continuum.io/downloads  
- Install Git Bash (if using windows): https://git-scm.com/downloads  
- Previous owner will transfer you a folder with the appropriate make/config files
  - Transfer these to your computer
  - For transferring to next year's owner:
    - The folders in uoftgasp that must be transferred: 
      - The /contents/ folder
      - the /www-data/ folder, contents don't need to be transferred just the folder
      - Makefile
      - peliconconf.py
      - upload.sh
      
- Use Bash to do the following to get the site onto your laptop:
```
cd "/desired/folder/with/transferred/files"  
conda install pelican
make html
```


## To Update Council Members page:

- Crop images to be all of equal size (e.g. 300x400px)  
- Save each as a jpeg titled First_Name.jpg such that First_Name matches the pelicanconf.py listing  
- Transfer images to uoftgasp/content/images/  
- Open pelicanconf.py:
  - EXECMEMBERS lists Executive Members, COUNCILMEMBERS lists council members. Each individual is formatted as (row_number, Role_Name, First_Name, Last_Name, Email).
  - e.g. (3, 'President', 'Jane', 'Smith', 'j23.smith@utoronto.ca')
- Each row can list at most three members, so the position of an individual in the chart is indicated by row_number, and order listed; hence, **there can be no more than three individuals with the same row_number.** Edit EXECMEMBERS and COUNCILMEMBERS accordingly.
- .jpg filenames MUST MATCH the First_Name listed in EXECMEMBERS

## Add New Posting:

- Postings are organized into categories listed under uoftgasp/content/category/
- Choose the category you would like to post in (i.e. Events, Gallery or General) and make a new .md file in that directory named like 2016-10-25-post-name.md or copy another pre-existing file and edit contents
- Open the file and edit using the following format:

```
Title: Post Title - no colons (':') can be used
Date: yyyy-mm-dd date of posting

Content here.
```
- You do not need to put a title in the main content body as it will be generated automatically from the `Title:` header.

### Some tips:
- add an image into the uoftgasp/content/posters folder, and in the post using `![alt ({filename}/posters/year/poster_name.png)`
- make use of headings using ## at the start of the line (the more #'s indicate the level of heading with one # being the highest level)
- bold using `**bolded word**` or italicize with `__emphasis__`
- link with `[displayed words](link)`

## To Change Sidebar for Upcoming Events:
- Note: If you do not want to include upcoming events in the sidebar, set `UPCOMING_EVENTS = False`, otherwise follow the instructions below to update upcoming events
- Open pelicanconf.py
- Under UPCOMING_EVENTS, remove any events that have passed, and add new ones in the format: ('Event Name', 'Date/Time', 'Location', 'post-title') where 'post-title' will be the lowercase version of event title joined by dashes (-). Each event bracket must be separated by a commma. Events with no posting can have a 'post-title' as ''.

## To Push Changes to the Website:
Using shell:

```
# go to folder
cd /path/to/uoftgasp/
# push changes to html
make html
#to sync server with local changes to html
bash upload.sh
```
Changes should be updated within 5min minutes, may require a refresh of browser.
