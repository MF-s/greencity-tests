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

Test Steps

| Step | Action              | Data                                           | Expected Result            |
| ---- | ------------------- | ---------------------------------------------- | -------------------------- |
| 1    | Click on More       | Any event                                      | Event details page opens   |
| 2    | Check content       | -                                              | Event title, description, link, location, save event option, join event option, comments and date are displayed | 

✅ Test Case ID: 3, Test Title: Verify search functionality works correctly

Preconditions:

- Events page is opened
- At least one event exists

Test Steps

| Step | Action             | Data                   | Expected Result               |
| ---- | ------------------ | ---------------------- | ----------------------------- |
| 1    | Enter search query | 1 letter (e.g. "E")    | Relevant events are displayed |
| 2    | Enter search query | Full word (e.g. "Eco") | Relevant events are displayed |
| 3    | Enter search query | Full event name        | Exact event is displayed      |

Actual Result:

* Search works only for 1 letter input
* When entering more than 1 letter, no results are displayed
