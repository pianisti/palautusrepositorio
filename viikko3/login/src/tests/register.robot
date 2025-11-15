*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kalle1
    Set Password  kalle1
    Set Confirmation  kalle1
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle2
    Set Password  kallekalle
    Set Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle3
    Set Password  kalle123
    Set Confirmation  kalle321
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Click Button  Register
    Go To Register Page
    Set Username  kalle
    Set Password  kalle1234
    Set Confirmation  kalle1234
    Click Button  Register
    Register Should Fail With Message  Username is already in use

*** Keywords *** 
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords *** 
Reset Application Create User And Go To Register Page
  Reset Application
  Go To Register Page