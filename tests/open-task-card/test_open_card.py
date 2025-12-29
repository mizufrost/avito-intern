from playwright.sync_api import Page, expect

# 003. Открытие карточки задачи


def test_open_card(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на задачу в списке
    task_item = page.get_by_text("Реализация новой галереи изображений")
    expect(task_item).to_be_visible(timeout=10000)
    task_item.first.click()

    # Проверка, что открывается детальное описание задачи
    details = page.get_by_label("Название")
    expect(details).to_be_visible(timeout=10000)
