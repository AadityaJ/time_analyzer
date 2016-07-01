Time Analyzer - ProMan16
====================================
### An Employee Efficiency Management and Recommendations  System

#### Intro
The software is be used to effectively **map the efficiency** of various employees with **different specialities** in a project team, which can be reviewed by the manager. The software also gives the ability to the Employee to see his/her own **efficiency** over a time period as well as provide a **Recommendation engine** based on __K-nearest neighbors__ for the manager to recommend employees for upcoming projects.The software uses *Java(>=version 1.7.0)* for all database connection and Recommendation engine, *MySql* for the backend and front-end is designed using *Java Swings in NetBeans*. The software was created as a part of my software engineering project.
#### Features and Methodology
The Software involves multiple levels of views (For example employees can see their own efficiency over the period of time but that of other employees while the manager can see efficiency of all employees). Besides this fundamental statistical features like average working hours for a particular kind of work ([see below](https://github.com/AadityaJ/time_analyzer#mapping))
The software uses K-nearest neighbors approach( __Content Based Filtering__ ) along with a __one-against-all__ strategy for Recommendation where the manager provide features essential for the upcoming project.

##### Modules Involved
* Login
* Employee
* Manager
* Recommend

#### Examples
![Manager](http://www.aadityajamuar.net/selfplots/time-analyzer1.png)</br>
![Recommendation](http://www.aadityajamuar.net/selfplots/time-analyzer2.png) </br>
For more screenshots checkout the */screenshots* repo.
##### Mapping
Mapping to effective hours:
* design : 0.9
* testing : 0.75
* coding : 1
* management:0.8
* algorithms: 1.2
* UI/UX: 0.8
