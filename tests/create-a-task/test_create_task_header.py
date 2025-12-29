from playwright.sync_api import Page, expect

# 001. Создание задачи через header


def test_create_task_header(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на кнопку "Создать задачу"
    page.get_by_text("Создать задачу").first.click()
    modal_card = page.get_by_role("heading", name="Создание задачи")
    expect(modal_card).to_be_visible(timeout=10000)

    # 2. Ввести название задачи
    page.get_by_label("Название").fill("Тестовая карточка")
    # 3. Ввести описание задачи
    page.get_by_label("Описание").fill("Описание для задачи")

    # 4. Нажать на строку "Проект"
    page.get_by_label("Проект").first.click()
    # 5. Выбрать проект, например, "Редизайн карточки товара"
    page.get_by_role("option").filter(has_text="Редизайн карточки товара").click()

    # 6. Нажать на строку "Приоритет"
    page.get_by_role("combobox").nth(1).click()
    # 7. Выбрать приоритет, например, "High"
    page.get_by_role("option").filter(has_text="High").click()

    # 8. Нажать на строку "Исполнитель"
    page.get_by_role("combobox").nth(3).click()
    # 9. Выбрать исполнителя, например, "Екатерина Смирнова"
    page.get_by_role("option").filter(has_text="Екатерина Смирнова").click()

    # 10. Нажать на кнопку "Создать"
    page.get_by_role("button", name="Создать", exact=True).click()
    # Проверка, что новая задача отображается в списке
    expect(page.get_by_text("Тестовая карточка").first).to_be_visible(timeout=10000)
