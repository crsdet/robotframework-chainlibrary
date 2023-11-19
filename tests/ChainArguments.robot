*** Settings ***
Documentation    Chain Arguments Tests
Library          String
Library          FakerLibrary
Library          ChainLibrary


*** Test Cases ***
Test Original String Is Not Altered
    ${original}        Set Variable         My name is __NAME__ and I am __AGE__ years old.
    ${name}            Name
    ${age}             Random Int           18             100
    ${age}             Convert To String    ${age}
    ${replaced}        Chain Arguments      Replace String
    ...    ${original}    __NAME__    ${name}
    ...    AND
    ...    %              __AGE__     ${age}
    Should Be Equal    ${original}          My name is __NAME__ and I am __AGE__ years old.
    Should Be Equal    ${replaced}          My name is ${name} and I am ${age} years old.

Test Same String Is Replaced Multiple Times
    ${original}        Set Variable       My name is __FIRST_NAME__ __LAST_NAME__, but you can call me __FIRST_NAME__.
    ${first_name}      First Name
    ${last_name}       Last Name
    ${replaced}        Chain Arguments    Replace String
    ...    ${original}    __FIRST_NAME__    ${first_name}
    ...    AND
    ...    %              __LAST_NAME__     ${last_name}
    Should Be Equal    ${replaced}        My name is ${first_name} ${last_name}, but you can call me ${first_name}.

Test None Existing String Is Ignored
    ${original}           Set Variable                  My name is __LAST_NAME__, __FIRST_NAME__ __LAST_NAME__.
    ${first_name}         First Name
    ${last_name}          Last Name
    ${age}                Random Int                    18             100
    ${age}                Convert To String             ${age}
    ${replaced}           Chain Arguments               Replace String
    ...    ${original}    __FIRST_NAME__    ${first_name}
    ...    AND
    ...    %              __LAST_NAME__     ${last_name}
    ...    AND
    ...    %              __AGE__           ${age}
    Should Be Equal       ${replaced}                   My name is ${last_name}, ${first_name} ${last_name}.
    Should Not Contain    ${replaced}                   ${age}
