from playwright.sync_api import Page, expect

# 006. Отчистка поискового запроса с помощью крестика


def test_clear_search_data(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Ввести название задачи, например, "Интеграция"
    page.get_by_placeholder("Поиск").fill("Интеграция")

    # Отображается список задач, в названии которых содержится слово "Интеграция"
    task_titles = page.locator("h6")
    count = task_titles.count()
    for i in range(count):
        expect(task_titles.nth(i)).to_contain_text("Интеграция", ignore_case=True)

    # 2. Нажать на кнопку "✖"
    page.locator("div.MuiInputAdornment-positionEnd button").click()
    # Проверка, что поле поиска не содержит данных.
    expect(page.get_by_placeholder("Поиск")).to_have_value("")
