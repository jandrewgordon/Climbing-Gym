<h1> Climbing Gym </h1>

<i>A booking management system for admin staff of a fantasy climbing gym. First solo project as part of CodeClan. Python backend with PostreSQL database. HTML + CSS front end.</i>

<img width="1440" alt="Home Page" src="https://user-images.githubusercontent.com/82443598/129725786-fd26a356-c356-4a5b-beb4-f712f77302a1.png">

<h2>Features</h2>
<ul>
  <li>Create new memberships and sessions</li>
  <li>Book members into sessions at a time and date</li>
  <li>Sessons have a limited capacity and double bookings are prevented</li>
  <li>Sessions can be classified as "premium"</li>
</ul>

<h2>Screenshots</h2>
<h3>Adding a new member</h3>
<img width="720" alt="Add New Member" src="https://user-images.githubusercontent.com/82443598/129727347-f2cf1648-7875-4808-a9f5-a91cfb2220c3.png">
<h3>Viewing all members</h3>
<img width="720" alt="All Members" src="https://user-images.githubusercontent.com/82443598/129735965-14e20f6c-994e-4bcf-9408-c955a52d8326.png">
<h3>Editing a session</h3>
<img width="720" alt="Editing a Session" src="https://user-images.githubusercontent.com/82443598/129736021-ad773da6-187f-43d7-a7b1-045e7087a612.png">
<h3>Prerequisites</h3>
The following must be installed to run the app:

<ul>
  <li>Python 3</li>
  <li>PostgreSQL</li>
  <li>Flask</li>
 </ul>
 
 <h3>Installation</h3>
 
To run the application, navigate to the project folder in terminal and enter the following.

<code>createdb booking_system</code>

<code>psql -d booking_system -f db/booking_system.sql</code>

<code>python3 console.py</code>

<code>flask run</code>

    
