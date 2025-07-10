import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

# Скриншот
def add_screenshot(driver: WebDriver):
    png = driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# Логи браузера
def add_logs(driver: WebDriver):
    try:
        logs = driver.get_log('browser')
        log_text = "\n".join(f"{log['level']} - {log['message']}" for log in logs)
    except Exception as e:
        log_text = f"Логи недоступны: {e}"
    allure.attach(log_text, 'browser_logs', AttachmentType.TEXT)

# HTML-код страницы
def add_html(driver: WebDriver):
    html = driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, extension='.html')

# Скринкаст (если используете Selenoid)
def add_video(driver: WebDriver):
    session_id = driver.session_id
    video_url = f"https://selenoid.autotests.cloud/video/{session_id}.mp4"
    html = f"""
    <html>
        <body>
            <video width='100%' height='100%' controls autoplay>
                <source src='{video_url}' type='video/mp4'>
            </video>
        </body>
    </html>
    """
    allure.attach(html, f'video_{session_id}', AttachmentType.HTML, extension='.html')
