# This is a quick cheatsheet of postgres commands that I have found useful over time.


# Log in to postgres console
sudo -u postgres psql

# Create a pg database
sudo -u postgres createdb <dbname>


# Connect to an existing postgres database
/c <dbname>

# Create a pg user
sudo -u postgres createuser <username>


# List existing postgres databases
/l


# Check current user

select current_user;


# Set database user

SET role <username>




