import allure
@allure.step(title="测试登录的流程")
def test_a():
    allure.attach('登录','输入用户名')
    print("aaa")

    allure.attach('登录','输入密码')

    allure.attach('登录','点击登录')
    assert 0