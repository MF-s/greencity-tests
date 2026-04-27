import allure
from src.pages.events_page import EventsPage


@allure.feature("Events Page")
@allure.story("Verify events list is displayed")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC1: Verify events list is displayed")
def test_events_cards_present(home_page):

    home_page.go_to_events()
    events_page = EventsPage(home_page.driver)

    cards = events_page.get_event_cards()

    assert len(cards) > 0, "No events found"

@allure.feature("Events Page")
@allure.story("Verify event details can be opened")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC2: Open event details")
def test_open_event_details(home_page):

    home_page.go_to_events()
    events_page = EventsPage(home_page.driver)

    events_page.open_first_event()

    assert events_page.is_event_details_opened() is not None



@allure.feature("Events Page")
@allure.story("Verify search functionality")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC3: Search events")
def test_search_events(home_page):

    home_page.go_to_events()
    events_page = EventsPage(home_page.driver)

    events_page.click_search()

    events_page.enter_search_text("E")
    assert len(events_page.wait_for_events()) > 0

    events_page.enter_search_text("Eco")
    assert len(events_page.wait_for_events()) > 0, "BUG: search not working"


@allure.feature("Events Page")
@allure.story("Verify invalid URL handling")
@allure.severity(allure.severity_level.MINOR)
@allure.title("TC4: Open invalid URL")
def test_invalid_url_error_message(home_page):

    home_page.go_to_events()
    events_page = EventsPage(home_page.driver)

    events_page.open_invalid_page()

    assert events_page.get_error_message() is not None