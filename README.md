# AlumNet
Alumnet is a dynamic, PHP-based webpage designed to connect alumni from a college or university. With Alumnet, alumni can easily sign up and create a profile, providing information such as their name, graduation year, and field of study. The platform allows alumni to connect with each other, offering a range of communication channels, including private messaging and public forums.

Alumnet makes it easy for alumni to stay up-to-date with college news and events, providing a centralized platform where alumni can learn about upcoming events, reunions, and other opportunities to get involved with the college community. Additionally, the platform allows alumni to stay in touch with the college administration and faculty, creating a valuable resource for networking and career opportunities.

Alumnet is designed with security in mind, with features such as password-protected accounts and secure data storage. The platform is user-friendly, with an intuitive interface that makes it easy to navigate and use. Whether you're looking to reconnect with old classmates or network with alumni in your field, Alumnet is the perfect tool for staying connected with your college community.

<h1>Installation</h1>

<h2>Method 1</h2>

1. You need xampp to run this application, you can download xampp using this [link](https://www.apachefriends.org/download.html)
2. Clone this repository using 

```
https://github.com/sumukhchitloor/AlumNet.git
```
3. Move the contents of the "Alumnet" directory to the "htdocs" directory within your XAMPP installation folder.

4. Open XAMPP and start the Apache and MySQL services.

5. Open a web browser and navigate to http://localhost/phpmyadmin. Create a new database for the Alumnet project.

6. Open the "config.php" file in the "Alumnet" directory and update the database credentials to match the database you just created.

7. Open a web browser and navigate to http://localhost/Alumnet to access the Alumnet project.


<h2>Method 2</h2>

<h3>Docker Container</h3>

1. Install Docker
2. Run docker pull alumnet/alumnet or docker pull alumnet/alumnet:v4
3. Run docker run --rm -p 8080:8080 alumnet/alumnet:v4
4. Browse to http://127.0.0.1:8080
5. Remove existing image using docker image rmalumnet/alumnet and pull again incase of any error

<h3>From Docker-Compose</h3>

1. Install Docker
2. Run docker-compose up or docker-compose up -d

<h3>Build Docker Image and Run</h3>

1. Clone the repository   git clone https://github.com/sumukhchitloor/alumnet.git
2. Change the directory where Dockerfile exists<br>
3. Build the docker image from Dockerfile using   docker build -f Dockerfile -t alumnet 
4. Run the docker image  docker run --rm -p 8080:8080 alumnet:v4
5. Browse to http://127.0.0.1:8080<br>  
