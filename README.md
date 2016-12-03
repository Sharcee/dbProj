## Introduction
#### Purpose
This document is the software specification report for Yucked. Yucked aims to provide a platform to serve users whose social environments are not conductive to good social experiences. We aim to provide users a means to look up businesses and inform them of local events and promotions in the city. The system is intended to serve the needs of students from FSU and the surrounding community.
#### Scope of the System Specified
The need for the system is to ensure that students are informed as possible. Currently, users do not have a way to rate businesses and be alerted when businesses have limited-time promotions all on a social platform. The software will automate a method to ping businesses with promotional updates and present the users with the information obtained.
#### Definitions, Acronyms, and Abbreviations
| Term | Definition |
|:--------|:-------:|
| System Administrator | Responsible for maintaining the software, database, network, and configuration of the backend. Has permission to access all parts of the system for testing purposes.|
| User | The end user of the software. They have permission to use functions that can query the database and add a favorite place |
#### References to Supporting Documents
#### Overview of rest of SRS
## General Description
#### Product Perspective
Yucked is a web-based system with interaction to a database containing relevant testing data, the user's phone numbers, and the system being used by the user to find local promotions. The system provides a secure environment for all registrations and for storing and retrieving of confidential user information.
#### Product Functions
Yucked allows a user to log onto the system, search which businesses they want to review, select promotions, and set favorite place. To use the system, a phone number and password is required during registration, and a user can decide their user id. A user can then log on and begin querying the database for promotions and reviews. A system administrator must make requests to local businesses so that promotions can then be scheduled into the system and registered into the database.
#### User Characteristics
Systems Administrators
Can maintain the software, configure the system, access all parts of the system for testing and debugging, and can take on the privileges of Testing Center, Faculty, and Student roles.
Users
Can login into the system, they can search which businesses they want to review, they can select promotions, and they can set a favorite place.
#### General Constraints
The constraints are the systems dependency on reliable connection to the database. With multiple users making queries to the database simultaneously, a good connection is very important because without it, users will reach a "Connection Timed Out" error. The user will also need a reliable connection to the server as all the systems functions and resources are located on the server side.
#### Assumptions and Dependencies
The systems front-end is dependent on the most recent versions of internet browsers. This decision is due to the fact that coding for several versions of different browsers is time consuming.
## Functional Requirements
A first-time user of Yucked will encounter a landing page when the method of display presents the interface. Being a first-time user, they will encounter a form that will initialize a new profile.

A regular user will encounter a method on the landing page to log on and access their profile on the system. Every user should have an account on the system where they can edit their personal profile, as well as exam dates, and depending on if they are an administrator, test and develop on the system.

ID: FR1  
TITLE: User Registration - Landing Page  
DESC: A user on the landing page should be able to access a method to register a new account.  
RAT: In order to register new users to the system  
DEP: None


ID: FR2  
TITLE: Retrieve Username  
DESC: A user who has registered should be able to recover their username via e-mail in case they forgot their credentials.  
RAT: User Support  
DEP: FR1


ID: FR3  
TITLE: Retrieve Password  
DESC: A user who has registered should be able to recover their username via e-mail in case they forgot their credentials.  
RAT: User Support  
DEP: FR1

ID: FR4  
TITLE: Search  
DESC: A user who has registered should be able to use the app and search for events and businesses.  
RAT: App functionality  
DEP: FR1

ID: FR5  
TITLE: Retrieve favorite place  
DESC: A user who has defined a business as their favorite place will be allowed to call a getter function that will return their favorite place.  
RAT: App functionality  
DEP: FR1 FR4

## Non-Functional Requirements
The system will provide accurate data derived from business listings. The system will provide a private, secure environment to guarantee the confidentiality of user data, including information on promotions and businesses. The system must have a reliable connection from user to server and server to database as all user interactions are dealt on the server side. Lastly, the system will provide a modern user interface with a minimalistic design and free of unnecessary features.
## Appendices
#### Actor Descriptions

| Term | Description |
|:--------|:-------:|
| entry | lorem ipsum|

#### Use Case Descriptions

| Use Case | Description |
|:--------|:-------:|
| entry | lorem ipsum|

#### Class Descriptions

| Class | Attributes/Relationship |
|:--------|:-------:|
| entry | lorem ipsum|
