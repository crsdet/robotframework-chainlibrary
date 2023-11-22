# RobotFramework-ChainLibrary

[![GitHub Actions status](https://github.com/crsdet/robotframework-chainlibrary/actions/workflows/tests.yml/badge.svg)](https://github.com/crsdet/robotframework-chainlibrary/actions) [![Version](https://img.shields.io/pypi/v/robotframework-chainlibrary.svg?label=version)](https://pypi.python.org/pypi/robotframework-chainlibrary) [![License](https://img.shields.io/pypi/l/robotframework-chainlibrary.svg)](https://github.com/crsdet/robotframework-chainlibrary/blob/main/LICENSE)

**RobotFramework-ChainLibrary** is a [Robot Framework](https://robotframework.org) library for running keywords in a chain. The purpose is to streamline the execution of common operations by providing a condensed syntax that allows users to perform tasks with fewer lines of code.

## Installation

You can install robotframework-chainlibrary via [pip](https://pip.pypa.io/en/stable):

~~~sh
pip install robotframework-chainlibrary
~~~

## Usage

Documentation can be found at <https://crsdet.github.io/robotframework-chainlibrary>.

~~~robotframework
*** Settings ***
Library    ChainLibrary


*** Test Cases ***
Test Generate Random Int And Set It On A Test Variable
    ${num}    Chain Keywords
    ...    Random Int    18    100
    ...       AND
    ...    Set Test Variable    $RANDOM_NUMBER
    Variable Should Exist    ${RANDOM_NUMBER}
    Should Be Equal    ${num}    ${RANDOM_NUMBER}

Test Replace Last Returned Value
    ${num}    Chain Keywords
    ...    Random Int    18    100
    ...       AND
    ...    Set Test Variable    $RANDOM_NUMBER
    ...       AND
    ...    Evaluate      $_ + 10
    ...       AND
    ...    Set Test Variable    $RANDOM_NUMBER_PLUS_10
    Variable Should Exist    ${RANDOM_NUMBER}
    Variable Should Exist    ${RANDOM_NUMBER_PLUS_10}
    Should Be Equal    ${RANDOM_NUMBER + 10}    ${RANDOM_NUMBER_PLUS_10}
    Should Be Equal    ${num}    ${RANDOM_NUMBER_PLUS_10}

Test Last Returned Value Remains If Previous Keyword Does Not Return A Value
    ${num}    Chain Keywords
    ...    Random Int    18     100
    ...       AND
    ...    Log
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

RobotFramework-ChainLibrary is open source software provided under the [Apache License 2.0](https://github.com/crsdet/robotframework-chainlibrary/blob/main/LICENSE).
