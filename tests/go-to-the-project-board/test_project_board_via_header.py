from playwright.sync_api import Page, expect

# 008. Открытие карточки задачи


def test_project_board_via_header(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на кнопку "Проекты"
    page.get_by_role("link", name="Проекты").click()

    # Открывается страница со списком проектов
    expect(page).to_have_url("https://avito-tech-internship-psi.vercel.app/boards")

    # 2. В списке проектов нажать на кнопку "Перейти в проект" , например, у проекта "Автоматизация тестирования"
    page.locator('a[href="/board/5"]').click()

    # Открывается страница с выбранной доской и списком задач проекта
    expect(page).to_have_url("https://avito-tech-internship-psi.vercel.app/board/5")
    expect(page.locator("h4")).to_be_visible(timeout=10000)
