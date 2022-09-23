from selenium.webdriver.common.by import By


class Login:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//*[@type='submit']"
    button_addemp_xpath = "//a[contains(text(),'Add Employee')]"
    textbox_1stname_name = "firstName"
    textbox_midname_name = "middleName"
    textbox_lastname_name = "lastName"
    button_save_xpath = "//button[@type='submit']"
    checkbox_info_xpath = "span[class$='oxd-switch-input oxd-switch-input--active --label-right']"
    textbox_create_user = "//*[text()='Username']/../..//*[@class='oxd-input oxd-input--active']"
    textbox_creat_pass = "//*[text()='Password']/../..//*[@type='password']"
    textbox_creat_c_pass = "//*[text()='Confirm Password']/../..//*[@type='password']"
    button_admin = "//*[text()='Admin']"
    record = "//span[@class='oxd-text oxd-text--span']"
    search_user = "//*[contains(@class,'oxd-input-field-bottom-space')]//*[@class='oxd-input oxd-input--active']"
    search_click_s = "//button[text()=' Search ']"
    #ver = "//*[text()='fgyjhj']/../.."
    data = "(//*[@class='orangehrm-container']//*[@role='row'])[2]"
    table = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
    sys_user = "//*[text()='System Users']"
    Logout_one = "//*[@class='oxd-userdropdown-name']/../../.."
    Logout_two = "//*[text()='Logout']"
    img_xpath= "//*[@class='oxd-icon bi-plus']/../..//*[@class='employee-image-wrapper']"


    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_add_emp(self):
        self.driver.find_element(By.XPATH, self.button_addemp_xpath).click()

    def set_firsname(self, fname):
        self.driver.find_element(By.NAME, self.textbox_1stname_name).send_keys(fname)

    def set_midmane(self, mname):
        self.driver.find_element(By.NAME, self.textbox_midname_name).send_keys(mname)

    def set_lastname(self, lname):
        self.driver.find_element(By.NAME, self.textbox_lastname_name).send_keys(lname)

    def click_empsave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def checkbox_info(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_info_xpath).click()

    def set_create_username(self,creat_use):
        self.driver.find_element(By.XPATH,self.textbox_create_user).send_keys(creat_use)

    def set_create_password(self,creat_password):
        self.driver.find_element(By.XPATH,self.textbox_creat_pass).send_keys(creat_password)

    def set_creat_c_pass(self,creat_password):
        self.driver.find_element(By.XPATH,self.textbox_creat_c_pass).send_keys(creat_password)

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.button_admin).click()

    def search_username(self,creat_user):
        self.driver.find_element(By.XPATH,self.search_user).send_keys(creat_user)

    def search_click(self):
        self.driver.find_element(By.XPATH,self.search_click_s).click()


    def get_rec(self):
        varr = self.driver.find_element(By.XPATH,self.record).text
        return varr

    def get_datas(self):
        varr1 = self.driver.find_element(By.XPATH,self.table).text
        return varr1

    def get_sys_user(self):
        varr2 = self.driver.find_element(By.XPATH,self.table).text
        return varr2

    def log_out_one(self):
        self.driver.find_element(By.XPATH,self.Logout_one).click()

    def log_out_two(self):
        self.driver.find_element(By.XPATH,self.Logout_two).click()

    def imgs_send(self):
        self.driver.find_element(By.XPATH,self.img_xpath).send_keys("C:\\Users\\hkarthis\\PycharmProjects\\Projectoneorange\\testData\\download.png")

