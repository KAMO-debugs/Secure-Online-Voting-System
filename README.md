# Live SRC Voting System

A secure web-based voting system designed to manage **Student Representative Council (SRC) elections**. The system allows eligible students to register, authenticate themselves, vote electronically, and view election results while providing administrators with tools to manage elections, candidates, students, and audit records.

---

##  Project Overview

The **Live SRC Voting System** is a Django-based online voting platform developed to support SRC elections.

The system focuses on two main election types:

- **Institutional SRC Elections**
- **Campus SRC Elections**

The system is designed to ensure that only registered and eligible students can vote, while preventing students from voting more than once in the same election.

The system also supports scheduled elections and provides live visibility of voting results.

---

##  Objectives

The main objectives of the system are to:

- Provide a secure online voting platform for SRC elections.
- Verify students against an official student list.
- Prevent unregistered or ineligible students from voting.
- Prevent multiple votes by the same student in an election.
- Allow administrators to create and manage elections.
- Allow administrators to manage registered students.
- Allow candidates to be associated with specific elections.
- Display election results.
- Maintain audit logs of important system activities.
- Support different campuses and election types.
- Improve transparency and accessibility of SRC elections.

---

##  Main Features

###  Student Features

- Student registration
- Secure login and authentication
- Student profile
- View available elections
- View election details
- Vote for a candidate
- Prevention of duplicate voting
- View election results
- Logout

###  Election Management

Administrators can:

- Create elections
- Edit elections
- Delete elections
- Schedule election opening and closing times
- Define election types
- Associate elections with campuses
- Manage election status

Supported election types include:

1. Institutional SRC
2. Campus SRC
3. Runoff

###  Student Management

Administrators can import official student information using an Excel file.

Student information includes:

- Student Number
- Full Name
- Campus
- Faculty
- Registration status
- Eligibility status
- Account status

###  Candidate Management

Candidates can be associated with specific elections.

The system supports:

- Organizations
- Independent candidates
- Candidate descriptions
- Candidate images

###  Results

The results system provides:

- Total votes
- Votes received by each candidate
- Candidate vote percentages
- Winner identification

Results can be displayed based on the election status.

###  Security and Integrity

The system includes:

- Django authentication
- Login protection
- Student eligibility verification
- Registration verification
- Account-status verification
- One-vote-per-student-per-election restriction
- Audit logging
- Scheduled election opening and closing
- Staff-only administrative functionality

---

##  System Architecture

The project follows a Django web application architecture.

```text
                ┌─────────────────────┐
                │      Student        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Web Interface    │
                │   HTML / CSS / JS   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       Django        │
                │     Application     │
                └──────────┬──────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        Authentication   Elections    Voting
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      Database       │
                │       MySQL         │
                └─────────────────────┘
