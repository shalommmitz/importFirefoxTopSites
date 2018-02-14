<p align="center">
  <h3 align="center">importFirefoxTopSites</h3>

  <p align="center">
    A software to set the Top Sites shown when you open a new tab in FireFox.
  </p>
</p>
<br>
Noramlly, FireFox will set those sites automatically.  However, you might wish to set all the Top Sites at once, for example, on a new installation. 

Also, if "Never save history" is active, firefox won't update those sites. This software will still work. 

## Table of contents

- [Quick start](#quick-start)
- [Related Tasks](#Related-Tasks)
    - [Set Firefox to display the desired number of Top Sites](#Set Firefox to display the desired number of Top Sites)
    - [How to create the "browser.newtabpage.pinned" prefernce](#How to create the "browser.newtabpage.pinned" prefernce)
    - [Usefull Information from Mozilla](#Usefull Information from Mozilla)
- [Prerequisites and Installing](#rerequisites and Installing)
- [Author](#Author)
- [License](#License)

## Quick start

In order to set the Firefox Top Sites:

- Clone the repo: `git clone https://github.com/shalommmitz/importFirefoxTopSites.git`
- Select the sites: modify the file "urls.txt"
- Generate the json string: `python main.py'
- Open the Firefox configuration page: At a new tab type the url "about:config". Accept the warning.
- Find the Prefernce "browser.newtabpage.pinned". If it does not exist, see below on how to create it.
- Replace existing string with the string genrated by main.py
- Restart Firefox
- Open a new tab - you should see your sites.

## Related Tasks

### Set Firefox to display the desired number of Top Sites

The 3 steps below will display 12 Top Sites in any new Tab.

    1. Open a new Tab in Firefox (E.g., by clicking on the "+" on the upper-right corner).
    
    2. Open the "Customize your New Tab page", by clicking on the cog-wheel on the top-right corner.
    
    3. Make sure both "Top Sites" and "Show two rows" are checked.
    
The following [firefox support-ticket](https://support.mozilla.org/en-US/questions/1185690) explains how to set the number of Top Sites to any desired number. Look near the end of the text.
    

### How to create the "browser.newtabpage.pinned" prefernce

If you never modified your Top Sites, this prefernce does not exsit, and you will not be able to modify it using "about:config". 

Any change to the Top Site will create this prefernce. 
For example, you can do this:

    1. Open a new tab. This will show the existing Top Sites.
    2. Move the mouse pointer to the middle of the one of the Top Sites icons.   
       A cirle will appear at the top-left corder of the icon. 
    3. Click on this cirle and choose "Edit". 
    4. Change one of the entries and click on "Save".

This will create the needed preference. 

### Other information related to Firefox's Top Sites

- In order to set a site on the Top Sites without using this software, take the following steps:
    1. Add the site to the bookmarks toolbar
    2. Open a new tab. This will display the Top Sites
    3. Drag the desired site form the bookmarks toolbar into one of the icons of the Top Sites
- This [Mozilla support page](https://support.mozilla.org/en-US/kb/customize-new-tab-page) explains how to change the Top Sites using the Firefox build-in tools.


## Prerequisites and Installing

All that is needed is Python (either 2.x or 3.x). 

This software was tested on Firefox version 58. 

No installation is needed. Just get the repository.


## Author

**Shalom Mitz** - [shalommmitz](https://github.com/shalommmitz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

