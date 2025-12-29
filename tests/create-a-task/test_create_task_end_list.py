from playwright.sync_api import Page, expect

# 002. Создание задачи в конце списка задач


def test_create_task_end_list(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на кнопку "Создать задачу"
    page.get_by_text("Создать задачу").last.click()
    modal_card = page.get_by_role("heading", name="Создание задачи")
    expect(modal_card).to_be_visible(timeout=10000)

    # 2. Ввести название задачи
    page.get_by_label("Название").fill("Новая задача")
    # 3. Ввести описание задачи
    page.get_by_label("Описание").fill("Описание задачи")

    # 4. Нажать на строку "Проект"
    page.get_by_label("Проект").first.click()
    # 5. Выбрать проект, например, "Рефакторинг API"
    page.get_by_role("option").filter(has_text="Рефакторинг API").click()

    # 6. Нажать на строку "Приоритет"
    page.get_by_role("combobox").nth(1).click()
    # 7. Выбрать приоритет, например, "Low"
    page.get_by_role("option").filter(has_text="Low").click()

    # 8. Нажать на строку "Исполнитель"
    page.get_by_role("combobox").nth(3).click()
    # 9. Выбрать исполнителя, например, "Максим Орлов"
    page.get_by_role("option").filter(has_text="Максим Орлов").click()

    # 10. Нажать на кнопку "Создать"
    page.get_by_role("button", name="Создать", exact=True).click()
    # Проверка, что новая задача отображается в списке
    expect(page.get_by_text("Новая задача").first).to_be_visible(timeout=10000)
