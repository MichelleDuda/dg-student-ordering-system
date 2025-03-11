# DG Catering Student Meal Plan Portal Testing

* [Validator Testing](#validator-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [Additional Manual Testing](#additional-manual-testing)
* [User Story Testing](#user-story-testing)
* [Browser Compatibility](#browser-compatibility)
* [Bugs](#bugs)
* [Known Bugs](#known-bugs)

## Validator Testing

### HTML Validation
The following files all passed through the [HTML Validator](https://validator.w3.org/nu/#textarea) with no errors:
<img src="static/documentation/testing/validator_images/html_validator.jpg">
- index.html [Full Results](static/documentation/testing/validator_results/html_home.pdf)
- student_dashboard.html [Full Results](static/documentation/testing/validator_results/html_student_dashboard.pdf)
- menu.html [Full Results](static/documentation/testing/validator_results/html_menu.pdf)
- update_profile.html [Full Results](static/documentation/testing/validator_results/html_update_profile.pdf)
- login.html [Full Results](static/documentation/testing/validator_results/html_login.pdf)
- logout.html [Full Results](static/documentation/testing/validator_results/html_logout.pdf)

The following html file returned an error:
<img src="static/documentation/testing/validator_images/html_error_past_orders.jpg">
- past_orders.html [Full Results](static/documentation/testing/validator_results/html_past_orders.pdf)
- This error is not actually valid as the action is processed via Javascript to dynamically update the deletion URL. 

### CSS Validation
The style.css file passed through the [CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors:
<img src="static/documentation/testing/validator_images/css_validator2.jpg">

[Full Results](static/documentation/testing/validator_results/css_validator.pdf)

### Javascript Validation

- [Javascript Validator](https://jshint.com)
  - Code from script.js passed through JSHint site with no errors. The following Metrics were logged: There are 7 functions in this file. Function with the largest signature take 1 arguments, while the median is 0. Largest function has 7 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 2 while the median is 1.



### Python DeLinter
The following files all passed through the [Python PEP8 Linter](https://pep8ci.herokuapp.com/) with no errors:
    <details><summary>settings.py</summary>
    <img src="static/documentation/testing/validator_images/python/py_settings.jpg"> 
    </details>


    - settings.py 
    <img src="static/documentation/testing/validator_images/python/py_settings.jpg">
    - urls.py
    <img src="static/documentation/testing/validator_images/python/py_urls.jpg">




## Lighthouse Testing



## Additional Manual Testing



## User Story Testing

### Site Owner Goals
  
## User Goals

## Browser Compatibility
This website was tested on the following browsers:
- Google Chrome Version 129.0.6668.103 (Official Build) (64-bit)
- Microsoft Edge Version 130.0.2849.46 (Official build) (64-bit)
- Mozilla Firefox Version 128.0.3 (64-bit)

## Bugs


## Known Bugs
There are no unaddressed known bugs at this time. 
  


