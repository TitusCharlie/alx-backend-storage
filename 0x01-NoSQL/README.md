# 0x01. NoSQL

## Description

This project focuses on understanding NoSQL databases, specifically MongoDB, and performing various operations such as data insertion, querying, and updates using Python and PyMongo.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the basics of NoSQL databases.
- Use MongoDB to store and retrieve data.
- Perform CRUD operations using PyMongo.
- Create optimized queries using indexes.
- Understand the differences between SQL and NoSQL.
- Use Python to interact with MongoDB.

## Requirements

- MongoDB version 4.2 or higher
- Python 3.x
- `pymongo` Python library

## Project Files

### 0-list_databases.py
Lists all databases in a MongoDB instance.

### 1-insert_school.py
Inserts a new document in a `school` collection based on provided arguments.

### 2-update_topics.py
Changes the topics of a school document based on its name.

### 3-schools_by_topic.py
Returns the list of schools that have a specific topic.

### 4-log_stats.py
Provides statistics about Nginx logs stored in MongoDB, including the total number of logs and the count of different request methods.

### Additional Files

- `8-all.py`: Function to list all documents in a collection.
- `9-insert_school.py`: Function to insert a new document in a school collection.
- `10-update_topics.py`: Function to update topics of a school.
- `11-schools_by_topic.py`: Function to find schools by a specific topic.
- `12-log_stats.py`: Script to provide statistics on Nginx logs in MongoDB.

## Usage

### Install dependencies:

```bash
pip install pymongo