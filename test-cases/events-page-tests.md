✅ Test Case ID: 1, Test Title: Verify events list is displayed

Preconditions:

- User opens browser

Test Steps

| Step | Action              | Data                                           | Expected Result           |
| ---- | ------------------- | ---------------------------------------------- | ------------------------- |
| 1    | Go to page          | https://www.greencity.cx.ua/#/greenCity/events | Page loads successfully   |
| 2    | Observe events list | -                                              | List of events is visible |

✅ Test Case ID: 2, Test Title: Verify event details can be opened

Preconditions:

- Events page is opened
- At least one event exists


| Step | Action              | Data                                           | Expected Result            |
| ---- | ------------------- | ---------------------------------------------- | -------------------------- |
| 1    | Click on More       | Any event                                      | Event details page opens   |
| 2    | Check content       | -                                              | Event title, description, link, location, save event option, join event option, comments and date are displayed | 
