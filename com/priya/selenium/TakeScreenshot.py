'''def take_page_ss(driver, name):
    driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/pythonSelenium/ss1.png" +name+".png")'''


n=int(input("enter number of rows"))
for i in range(0,n):
    for j in range(0,n-5+i):
        print(end=" ")
    for j in range(0,n-i):
        print("*", end=" ")
    print()