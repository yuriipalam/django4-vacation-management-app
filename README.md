# Vacation Management App

This is app helps employees to request leaves from administrators.

There are 3 roles of user:
- None (Does not have permission to the panel, unless accepted by administrator)
- Viewer (Have access to the request and requests list pages, but cannot create requests)
- Employee (Allowed to create requests to be reviewed by administrator)

Adminitrator can:
- Manage all users and change their roles (None -> Viewer / Viewer -> Employee / Employee -> None, etc)
- Allow/Reject requests from users, default status of each request is Waiting (Waiting -> Rejected / Waiting -> Approved / Rejected -> Waiting, etc)

Users (Viewer/Employee) can see all their requests and filter them by status. CalendarView is used to choose dates (Start date and Finish date)

The app was built with Django 4. Bootstrap is used for Front-End
- Login/Registration
- SQLite3 DataBase
- Multiple pages
- Two apps (Members, Manaagement System)
- Auth system via email
