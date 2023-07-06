<details>
  <summary>Table of Contents</summary>
   
  1. [Virtual Wallet App](#virtual-wallet-app)
  2. [Build with](#build-with)
  3. [About the project](#about-the-project)
  4. [Database](#database)
  4. [Authors](#authors)
</details>

# Virtual Wallet App

This is a personal project where I design a virtual wallet to track personal expenses and incomes. The main idea is to spend my time on something more important rather than playing League of Legends and learn during the process.

It is not my first approach to this project. I have been working on a full Python version of it, where I defined the basis of it, such as the database structure, the main functionality, and how the app is supposed to work. You can check the repo at the following link: [Virtual Wallwt](https://github.com/Tomas-Wardoloff/Virtual-Wallet)

I believe I have reached a decent level in that project, but it does not offer a friendly interface for the user. It just prints the results on the terminal. So I created this repo, where I am going to develop a web app version of the project to take the project to another level.

# Build with

I am using Python 3.11.2 and the [Flask](https://flask.palletsprojects.com/en/2.3.x/) module to build the core of the app, Git and Github to keep track of the code versions, HTML and CSS for the different views, MySQL to store and manage the user's data in a database, [pytest](https://docs.pytest.org/en/7.3.x/) to test the functionality and [coverage](https://coverage.readthedocs.io/en/7.2.7/) to see how much of the code is run with those tests.
I am trying to write as much clean code as possible, so I am using the [black](https://black.readthedocs.io/en/stable/) module to format the code and [pylint](https://www.pylint.org/) to analyze the usability.

<div>
   <img src='https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white'/>
   <img src='https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white'/>
   <img src='https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white'/>
   <img src='https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white'/>
   <img src='https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white'/>
</div>

# About the project

- **Account registration**:  
   The application allows the user to create a wallet account and register their personal details such as name, email address, and password .

- **Transaction logging**:
  The application keeps a record of all transactions made, whether it is an income or expense. It tracks every financial operation that involves the movement of money. All the transactions include sensitive information such as the date, the amount of money involved, the category, and a short description that is going to be provided by the user.

- **Transaction analysis**:
  The application shows the user an analysis of their transactions to have a better understanding of their spending and saving habits. The application offer charts and statistics to help the user see how their money is being spent.

# Database

From the beginning, I knew I was going to work with a database and what data I wanted to store, but I did not know how to struct the database. So I asked Chat-GTP.
After chatting and seeing different databases that Chat-GTP provided me, I modified one of those ideas and came out with this. 
The database structure is not the same as the one used in the other version of the project. I added more columns to the user table.

- **Users**
  The Users table will store information about each user, such as their first name, last name, email and password. Each user will have a unique identifier, which will serve as the primary key for this table.

- **Categories**
  This table only stores the information of the different categories that the users can use to identify their transactions, and like the user's table, it has a unique identifier. The users can create their own categories, which is why this table has a foreign key that references the Users table. The categories with UserId = 0 are accessible to all the users.

- **Transactions**
  This table store information about each transaction made by the users. This table will have two foreign keys, one references the User table so each transaction will be associated with a particular user, and the other one references the Categories table.

- **Wallets**
  This table store a "summit" of the user's wallet. This one has a foreign key that references the User table and also stores information such as currency, balance and an identifier.

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

## Authors

- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
