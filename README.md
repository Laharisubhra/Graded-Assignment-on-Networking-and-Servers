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
