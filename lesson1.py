from selenium import webdriver
przegladarka = webdriver.Chrome()
przegladarka.get('http://wp.pl')
przegladarka.maximize_window()