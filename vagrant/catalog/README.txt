This following project is a simple catalog web application that will orginize and display a list of
sports items based on thier category(sports)

Instructions on how to get your application up and running:

1-download or clone the complete file direcotry from the following github link:
    download: https://github.com/omar-jandali/Udacity-Item-Catalog
    clone: git clone https://github.com/omar-jandali/Udacity-Item-Catalog Fullstack

2-download virtual machine in order to run the local database and server for the project
    virtual machine: https://www.virtualbox.org/wiki/Downloads

3-using your prefered VCS machine change directories to the main vagrant folder
    desired directory: Fullstack/vagrant

4-run the following code in your VCS it initiate your local server through virtual machine
    Run code: vagrant up
    (give it up to 30 seconds to run before you see any results.
    there me be pauses that you see with the initialization, but it is
    normal and be patient. the whole process takes a minute or so)

5-one the vagrant machine is set up and running, run the following code
    Run code: vagrant ssh
    (give it a few seconds and then you will see a change in the
    VCS console)

6-move the current file to the desired directory to ruin this project
    Run Code: cd /vagrant/catalog

7-You have to setup the database before you can setup the server by running some code
    Run Code: python setup_database.py
    (This will do a few things, initilaize the databse that
      you will be using for this project. structure the tables.
      and other various tasks. )

8-once the database has been initialized, you can run the local server through the following code
    Run Code: python setup_server.py
    (once you run the code above you should see a message that comes up in your local VCS that
    will say that you are successfully running the web app and it will give you a localhost port
    number that you will use in your favorite browser)

9-Once you open the project through the localhost:8000 port you will be greeted with the home page
    of this project, you can then navigate around the current catalog
10-After logging into your google plus account, you can also create edit and delete items that you
    create in the local database
