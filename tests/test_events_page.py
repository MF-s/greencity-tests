from pages.events_page import EventsPage


# TC1
def test_events_cards_present(home_page):
    home_page.go_to_events()

    events_page = EventsPage(home_page.driver)

    event = events_page.get_events()
    assert event is not None, "Події не знайдені"

    events = events_page.get_all_events()
    assert len(events) > 0

    print(f"Знайдено {len(events)} подій")


# TC2
def test_open_event_details(home_page):
    home_page.go_to_events()

    events_page = EventsPage(home_page.driver)

    events_page.open_first_event()

    details = events_page.is_event_details_opened()
    assert details is not None, "Сторінка деталей не відкрилась"

    print("Деталі події відкрито успішно")


# TC3
def test_search_events(home_page):
    home_page.go_to_events()
    events_page = EventsPage(home_page.driver)

    events_page.click_search()

    # E
    events_page.enter_search_text("E")

    events_E = events_page.wait_for_events()

    assert len(events_E) > 0, "Немає результатів для 'E'"
    print(f"Результати для 'E': {len(events_E)}")

    # Eco (баг)
    events_page.enter_search_text("Eco")

    import time
    time.sleep(1)

    events_Eco = events_page.get_events_after_search()

    assert len(events_Eco) == 0, "Очікувався баг, але результати є"
    print("БАГ підтверджено: для 'Eco' результатів немає")


# TC4
def test_invalid_url_error_message(home_page):
    home_page.go_to_events()

    events_page = EventsPage(home_page.driver)

    events_page.open_invalid_page()

    error = events_page.get_error_message()
    assert error is not None, "Повідомлення про помилку не з'явилось"

    print("Повідомлення про помилку з'явилось")