from playwright.sync_api import Page, expect

# 007. Переход на доску проекта через карточку задачи

def test_project_board_via_task(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на задачу в списке
    task_item = page.get_by_text("Реализация новой галереи изображений")
    expect(task_item).to_be_visible(timeout=10000)
    task_item.first.click()

    # 2. Нажать на кнопку "Перейти на доску"
    page.get_by_role("link", name="Перейти на доску").click()

    # Открывается страница с доской карточки товара, указанная предварительно при создании карточки задачи.
    expect(page).to_have_url("https://avito-tech-internship-psi.vercel.app/board/1")
    expect(page.locator("h4")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Реализация новой галереи изображений")).to_be_visible(timeout=10000)