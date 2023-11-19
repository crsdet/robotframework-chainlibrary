# RobotFramework-ChainLibrary

[![GitHub Actions status](https://github.com/crsdet/robotframework-chainlibrary/actions/workflows/checks.yml/badge.svg)](https://github.com/crsdet/robotframework-chainlibrary/actions)

**robotframework-chainlibrary** is a [Robot Framework](https://robotframework.org) library that allows to run different keywords in a chain, reducing the amount of keywords used to perform a simple task.

## Installation

You can install robotframework-chainlibrary via [pip](https://pip.pypa.io/en/stable):

~~~sh
pip install robotframework-chainlibrary
~~~

## Usage

Documentation can be found at <https://crsdet.github.io/robotframework-chainlibrary>.

~~~robotframework
*** Settings ***
Library    String
Library    ChainLibrary


*** Variables ***
${EXAMPLE_REPLACE_STRING}    My name is __LAST_NAME__, __FIRST_NAME__ __LAST_NAME__.


*** Test Cases ***
Test Replace String With Different Values
    ${str}    Chain Arguments    Replace String
    ...    ${EXAMPLE_REPLACE_STRING}    __LAST_NAME__     Doe
    ...       AND
    ...    %                            __FIRST_NAME__    John
    Should Be Equal    ${str}    My name is Doe, John Doe.

Test Generate Random String And Log It
    ${str}    Chain Keywords
    ...    Generate Random String
    ...       AND
    ...    Catenate    SEPARATOR=${SPACE}    Random String is:    %.
    ...       AND
    ...    Log
    Should Be Equal    ${str}    Random String is: random_generated_string.

Test Generate Random Int And Set It On A Test Variable
    ${num}    Chain Keywords
    ...    Random Int    1    5
    ...       AND
    ...    Set Test Variable    $RANDOM_NUMBER
    Variable Should Exist    ${RANDOM_NUMBER}
    Should Be Equal    ${num}    ${RANDOM_NUMBER}
~~~

You can also specify a different separator or replace string:

~~~robotframework
*** Settings ***
Library    ChainLibrary    separator=${SEPARATOR}    replace=${REPLACE}


*** Variables ***
${SEPARATOR}    ->
${REPLACE}      %
~~~

## License

RobotFramework-ChainLibrary is open source software provided under the [GPL-3.0 License](https://github.com/crsdet/robotframework-chainlibrary/blob/main/LICENSE).
