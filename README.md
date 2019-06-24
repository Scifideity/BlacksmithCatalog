
## Blacksmith Catalog (Item Catalog App)

My Blacksmith Catalog is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

### Features

    *   Full CRUD support via SqlAlchemy and Flask
    *   Authentication and Authorization checks.
    *   Styles and Layout via Bootstrap
    *   JSON Endpoints
    *   Implements OAuth using Google Sign-in API

### Files

    database_setup.py       -  Create the database
    StarterDataandUser.py   -  Populate the database with starter user and data
    application.py          -  Main Application code
    static/styles.css       -  a few local overrides to Bootstrap
    templates/              -  HTML pages called by the application

## Getting Started

    You can clone or download this project via GitHub to your local machine.

### Prerequisites

    You will need to have or install the following:

    1. Unix-style terminal
        * Windows - Use [Git Bash](https://git-scm.com/downloads)
        * Mac - You're already set with Terminal (Like it should be :D )
    2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    3. [Vagrant](https://www.vagrantup.com/downloads.html)
    4. These [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) files

### Installation / Setup

    1. Unzip the **VM configuration** to your working directory
    2. Using *Git Bash* (_Windows_) or *Terminal* (_Mac_)
       Navigate to your working directory where you unzipped *VM configuration*
       You will find the *vagrant* directory
    3. Type `cd vagrant` to navigate into the VM repository
    4. Run the following command
    `$ vagrant up`
        This will setup and configure your VM downloading what it needs in the process.
    5. When complete and back to a shell prompt, Login to your VM via SSH with:
    `$ vagrant ssh`
    6. Move the folder you downloaded from GitHub into the vagrant folder
    7. In your terminal, change to the *vagrant* directory
    `$ cd /vagrant`

### Application Prep

    1. Still in your Terminal (get used to working there), set up the database
    `$ python database_setup.py`
    2. Populate the database with initial data
    `$ python StarterDataandUser.py`
    3. Once complete it will display
    `Starter Database populated...`

### Run the application

    `$ python application.py`

### Access the application

    Using your browser, navigate to http://localhost:8000

#### Enjoy

## Credits and Code References
Udacity Full Stack Web Developer Nano Degree :
https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004
GitHub : https://github.com/
Python : https://www.python.org/
Flask : http://flask.pocoo.org/docs/1.0/
Bootstrap : https://getbootstrap.com/
FontAwesome : https://fontawesome.com/
Google APIs : https://cloud.google.com/apis/docs/overview
