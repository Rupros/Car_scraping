# Car Listings Web Scraper

## PROJECT INFORMATION

I worked individually on the project. Since I am frequently checking for new car offers, I decided to create an autonomous bot, which would gather offers, in which I would be interested in.

## Overview

This is a simple web scraper designed to gather car listings based on user-specified criteria. The scraper is written in Python and utilizes the selenium library for web scraping. It is intended to be a starting point for users who want to collect car listings from various websites for their specific interests.

Random time intervals are used in order to make it seem more human like

## Features

- **Customizable Search Criteria:** Price | Mileage based on my needs | only looking for Audi
  
- **Multi-Website Support:** Checking websites in SS.LV and mollerauto.lv

- **Data Output:** Saves links to cars that fit my criteria in a file

## Prerequisites

Make sure you have the following installed before running the scraper:

- Python 3.x
- Selenium

## DISCLAIMER

This web scraper is for educational purposes only. Using it frequently might cause the website to detect it as a bot. Countermeasures, such as randomized time between interactions were implemented. Selenium JS signiture is not hidden, because it depends on the machine it will be ran on. 

### USED LIBRARIES

## Selenium Integration

This web scraper utilizes the Selenium library for enhanced web scraping capabilities. Selenium is employed in scenarios where a website relies heavily on JavaScript, or when interactive elements on the webpage need to be manipulated for data retrieval.

### Selenium Components

- **WebDriver:** The `webdriver` class is the primary interface for interacting with web browsers. It allows the scraper to open a browser window, navigate to web pages, and interact with elements on the page.

- **Options:** The `Options` class, in conjunction with Firefox, enables the configuration of browser behavior. It is often used to set options such as running the browser in headless mode (without a visible UI).

- **By:** The `By` class is utilized to locate HTML elements on a web page. It provides various mechanisms to find elements, such as by ID, name, class name, etc.

- **WebDriverWait:** The `WebDriverWait` class is employed to wait for a certain condition to occur before proceeding with the script execution. This synchronization ensures that the script progresses only when specific conditions are met.

- **expected_conditions:** This module provides predefined conditions that can be used with `WebDriverWait`. It allows waiting for specific events or states on a webpage.

- **TimeoutException:** The `TimeoutException` is raised when an operation times out, often used with `WebDriverWait` to handle situations where an expected condition is not met within a specified time.

### Time and Random

In addition to Selenium, the script incorporates the following modules:

- **time:** The `time` module introduces delays in the script. Waiting for elements to load before interaction is common in web scraping, and `time.sleep()` provides a simple way to add delays.

- **random:** The `random` module is used to introduce randomness in waiting times. This helps in avoiding detection by websites that may block or restrict access to automated scripts. Random waiting times make the scraping activity appear more like human behavior.
