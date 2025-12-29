from playwright.sync_api import Page, expect

# 005. Поиск задачи с приминением фильтра по доске

def test_search_by_desk(page: Page):
    # Открыта главная страница
    page.goto("https://avito-tech-internship-psi.vercel.app/")

    # 1. Нажать на кнопку "Доска"
    page.get_by_role("combobox").nth(1).click()

    # 2. Выбрать доску, например, "Переход на Kubernetes"
    page.get_by_role("option", name="Переход на Kubernetes").click()

    # Проверка, что отображается список задач, текст которых содержит "Переход на Kubernetes"
    board_labels = page.locator("p.MuiTypography-body2")
    count = board_labels.count()
    for i in range(count):
        expect(board_labels.nth(i)).to_contain_text("Переход на Kubernetes", ignore_case=True)
