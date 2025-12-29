from playwright.sync_api import Page, expect

# 004. Поиск задачи по ключевому слову


def test_search_by_keyworld(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Ввести название задачи, например, "Реализация"
    page.get_by_placeholder("Поиск").fill("Реализация")

    # Проверка, что отображается список задач, в названии которых содержится слово "Реализация"
    task_titles = page.locator("h6")
    count = task_titles.count()
    for i in range(count):
        expect(task_titles.nth(i)).to_contain_text("Реализация", ignore_case=True)
