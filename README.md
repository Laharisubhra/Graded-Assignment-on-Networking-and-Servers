# Graded-Assignment-on-Networking-and-Servers
Graded Assignment on Networking and Servers
Step 1:  Launch an EC2 Instance
Open the AWS Management Console and navigate to the EC2 dashboard.
Click on "Launch Instance" and select an Amazon Machine Image (AMI) of your choice (e.g., Amazon Linux 2).
Choose an instance type, configure instance details, add storage, add tags, configure security group rules, and review your settings.
Launch the instance, and select or create a key pair to connect to the instance securely.

Step 2: Connect to the EC2 Instance

Step 3: Install Nginx

Open your terminal window and run the following command to update the package list:

sudo apt update
Next, install Nginx by running the following command:
sudo apt install nginx
Once the installation is complete, you can verify that Nginx is running by running the following command:
sudo service nginx status
This should display information about the Nginx service, including its current status.

Step 4: change directory to where index.html file resides 
CD /var/www/html

Step 5: Edit and input code in   Index.html File
nano index.html
update with below code 
<!DOCTYPE html>
<html>
<head>
    <title>Awesome Web</title>
</head>
<body>
    <h1>Welcome to Awesome Web!</h1>
    <p>This is a sample website created with Nginx.</p>
</body>
</html>


Save the file once you've made your changes.

Step 6: Configure Nginx default.confuig file 

Nginx needs to be configured to serve your website. Open the Nginx configuration file by running the following command:

sudo nano /etc/nginx/conf.d/default.conf
Add the following code to the end of the file:


server {
    listen 80;
    server_name awesomeweb;
    root /var/www/awesomeweb;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

Step 7:  Set Up a DNS Name
-Go to the AWS Management Console,
- navigate to the Route 53 dashboard.
-Create a new hosted zone with the domain name "awesomeweb."
-Note the nameservers provided by Route 53.

Step 8: Create a "A" record 
launch the Hosted Zone created in AWS with the DOmain name purchased from the DNS provider
click on  the Create record 
Record name  record type - A
Value - Ip public and private for the EC2 instace 

Step 9: Go  to the Namecheap .com website 
find teh domain name associated on aws portal and click on manage 
add teh name servers that are created on teh AWS portal when the Hosted Zone are craeted which are teh NS record 

Step 10 :  if you try to launch  "http://awesomeweb.shop/" you will be able to find teh meesage as in html file 

**********************************************************************************************************************************************************
QUESTION 2

The Python prigram  and the text file the Pythin program is going to use is added to teh main branch of the repo 

Check the status of the website
def check_status(website): try: request = requests.get(website) return request.status_code except requests.ConnectionError: return 'Website is down!'

Check the status of the subdomains every minute
def check_subdomains(): subdomains = get_subdomains() while True: clear() table = prettytable.PrettyTable(['Subdomain', 'Status']) for subdomain in subdomains: status = check_status(subdomain) table.add_row([subdomain, status]) print(table) time.sleep(60)

Get the list of subdomains from the text file
def get_subdomains(): subdomains = [] with open('subdomains.txt', 'r') as file: for line in file: subdomains.append(line.strip()) return subdomains


if name == 'main': check_subdomains()

Here the python file name is 
Subdomain_status_check.py

And teh domain containing file name is 
subdomains.txt


In the code above, we are using the following libraries:

1> os: Provides a way to interact with the operating system.
2> requests: A powerful library for making HTTP requests.
3> time: A library that allows you to deal with time and delays.
4> prettytable: A library for easily displaying data in a tabular format.
5> datetime: A library that provides functions to work with dates and times.

PIP install library name

*********************************************************************************************************************************************************
Question 3 

Step 1:Create and deploy an AWS windows VM and login to it with teh private key 

Step 2: Download VirtualBox

Go to the official VirtualBox website: https://www.virtualbox.org/

Click on the "Downloads" link 

Step 3: Choose the Correct Package

Step 4: Install VirtualBox For Windows

Step 5: Post-installation Configuration add your user account to the  "VirtualBox Users" group (Windows) to grant permissions to manage VMs.

Step 6: Launch VirtualBox

Step 7: Before starting the virtual machine, you need to download an Ubuntu 22.04 image from the OSboxes website (https://www.osboxes.org/ubuntu/). After downloading the image, open VirtualBox and select the newly created virtual machine. Go to "Settings" > "Storage" and click on the empty optical drive icon. Choose "Choose/Create a Disk Image" and select the downloaded Ubuntu 22.04 image.

Step 8: Start the virtual machine by clicking on the "Start" button. Follow the Ubuntu installation prompts to complete the setup process.

Step 9: Once the Ubuntu virtual machine is up and running, open the terminal and update the system by running the following commands:


sudo apt update
sudo apt upgrade
Step 10: Install Nginx by running the following command:

sudo apt install nginx

Step 11: Configure Nginx to host a website from  Nginx configuration at /etc/nginx/sites-available/default.
sudo nano /etc/nginx/sites-available/default
Replace the contents of the file with the following configuration, adjusting the "server_name" and "root" values to match your website:

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name example.com www.example.com;

    location / {
        try_files $uri $uri/ =404;
    }
}
Save  and exit and Restart Nginx to apply  configuration:

sudo systemctl restart nginx

Step 12: Transfer your website files to the Ubuntu virtual machine. You can use the scp command for this purpose:


scp -r /path/to/your/website/ root@<IP_Address_of_Ubuntu_VM>:/var/www/html

Step 13: Open a web browser on your host machine and enter the IP address of the Ubuntu virtual machine in the address bar. You should now be able to view your website hosted on the Nginx server inside the virtual machine.

Step 14: Install Nmap on your host machine 

sudo apt install nmap
Step 15: Scan the Ubuntu virtual machine for open ports using Nmap:

nmap ubuntu vm ip adress 


