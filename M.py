from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'https://www.ycs.or.kr/page/etc/login.php?referer=https%3A%2F%2Fwww.ycs.or.kr%2Fyeyak%2Ffmcs%2F43'

driver.get(url)

def click(path) :
    driver.find_element_by_xpath("//" + path).click()
    return

def sendKey(path, keys) :
    action.send_keys_to_element(driver.find_element_by_xpath("//" + path),keys).perform()
    return

def execute(script):
    driver.execute_script(script)
    return

action = ActionChains(driver)

time.sleep(1)

sendKey("input[@name='id']","아이디")
sendKey("input[@name='pw']","비밀번호")
click("input[@class='submit']")

time.sleep(2)

driver.get("https://www.ycs.or.kr/yeyak/fmcs/43")

time.sleep(2)

execute('$("select[name=center]").val("YCS04");')
execute('$("select[name=center]").change();')

time.sleep(0.2)


execute('$("button[class=submit]").click();')

time.sleep(1)


execute("""
let dates = [];
for (let tr of document.querySelector(`div[class='calendar']`).children[0].querySelectorAll(`tr`)){
    for( let td of tr.querySelectorAll(`td`)){
        dates.push(td);
    }
}
let validDates = [];
for(let date of dates){
	if(date.attributes['data-state_cd'].value == 10){
		validDates.push(date);
	}
}
validDates[5].children[0].click();
""")

time.sleep(1)

execute("""
let times = [];
for(let tr of document.querySelector(`div[class=regist_list]`).querySelectorAll(`tr`)){
    if( tr.querySelector(`td`) != null){
        times.push(tr);
    }
}
let validTimes = [];
for(let t of times){
	if(t.querySelector(`input[disabled='disabled']`) == null){
		validTimes.push(t);
	}
}

for(let t of validTimes){
	t.querySelector(`input`).checked = true;
}

console.log(validTimes);
document.querySelector(`button[class='action_application']`).click();
""")


time.sleep(1)

execute("""
document.querySelector(`input[name='team_nm']`).value ="이상근";
document.querySelector(`input[name='users']`).value ="4";
document.querySelector(`input[name='tel']`).value ="";
document.querySelector(`input[name='purpose']`).value ="경기";
document.querySelector(`input[name='agree_use']`).checked =true;
$('input[name="captcha"]').val(document.getElementById('captcha').value)
document.querySelector(`button[class='button action_write']`).click();
""")
time.sleep(1000)
