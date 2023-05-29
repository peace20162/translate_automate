from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import os
import shutil
import time
import winsound


#drag&drop function 
JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)





###################################################################################

# # Create Chromeoptions instance 
# options = webdriver.ChromeOptions() 
 
# # Adding argument to disable the AutomationControlled flag 
# options.add_argument("--disable-blink-features=AutomationControlled") 
 
options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

edge_dr_path = r'C:\Users\peace\Desktop\Translate automate\edgedriver_win64\msedgedriver.exe'
website = "https://www.onlinedoctranslator.com/en/translationform"
novel_path= r'D:\นิยาย\Hour of sage\split\현자의 시간 1-419 (完)'
trans_path= r'D:\นิยาย\Hour of sage\trans'
no_file = 9
file_name=r'현자의 시간 1-419 (完)' + f'_{no_file}.txt'

# file_list=[f for f in os.listdir(novel_path) if os.path.isfile(os.path.join(novel_path, f))]
# print(file_list)


driver = webdriver.Edge(edge_dr_path,options=options)
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
print("\\\\\\\\\\\\\Open Chrome\\\\\\\\\\....................."+file_name) 
driver.get(website)



#Drop file
print("\\\\\\\\\\\\\Droping file\\\\\\\\\\")
action = ActionChains(driver)
test=os.path.join(novel_path,file_name)
drop_area = driver.find_element(by="css selector",value='html > body > main > section:first-of-type > form > div:first-of-type > div')
time.sleep(5)
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
drag_and_drop_file(drop_target=drop_area,path=test)
time.sleep(30)

print("\\\\\\\\\\\\\Setting\\\\\\\\\\")
#translate file
driver.implicitly_wait(2)
translate_box = driver.find_element(by="xpath",value='//*[@id="translation-button"]')
driver.implicitly_wait(5)
driver.execute_script("arguments[0].scrollIntoView();", translate_box)
form_dropdown = Select(driver.find_element(by="xpath",value='/html/body/main/section[4]/form/div[1]/div[1]/select')).select_by_visible_text('Korean')
driver.implicitly_wait(2)
to_dropdown = Select(driver.find_element(by="xpath",value='/html/body/main/section[4]/form/div[1]/div[2]/select')).select_by_visible_text('English')
driver.implicitly_wait(5)
time.sleep(3)
translate_box.click()
driver.implicitly_wait(2)



#download translated file
print("\\\\\\\\\\\\\Translating file\\\\\\\\\\")
link = WebDriverWait(driver,3600).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Download your translated document!'))) # wait for link
time.sleep(5)
link_element =driver.find_element(By.ID, 'download-link')
driver.implicitly_wait(10)

#<a id="download-link" href="/app/gettranslateddocument" download="사기급 스킬로 좀비 세상에서 꿀빨기 [피제에] 468 完_1.ko.en.txt">Download your translated document!</a>
print("\\\\\\\\\\\\\Downloading file\\\\\\\\\\")
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
action.click(on_element =link_element)
action.perform()
driver.implicitly_wait(25)
time.sleep(10)
driver.quit()


print('\\\\\\\\\\\\\Moving file\\\\\\\\\\')
time.sleep(10)
shutil.move(os.path.join(r'C:\Users\peace\Downloads',file_name.strip('.txt')+'.ko.en.txt'),os.path.join(trans_path,file_name.strip('.txt')+'.ko.en.txt'))


