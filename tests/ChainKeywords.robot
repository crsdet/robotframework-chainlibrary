*** Settings ***
Documentation    Chain Keywords Tests
Library          String
Library          FakerLibrary
Library          ../src/ChainLibrary/ChainLibrary.py    separator=${SEPARATOR}


*** Variables ***
${SEPARATOR}    AND


*** Test Cases ***
Test Keywords Can Be Chained - Log Random String
    Chain Keywords    Generate Random String    AND    Log

Test Keywords Can Be Chained - Int To String
    ${str_number}    Chain Keywords
    ...    Random Int    18    100
    ...    AND
    ...    Convert To String
    Should Be String    ${str_number}

Test Keywords Can Be Chained - Catenate Strings
    Chain Keywords
    ...    Generate Random String
    ...    AND
    ...    Catenate    SEPARATOR=${SPACE}    Random String:
    ...    AND
    ...    Log

Test Last Returned Value Remains If Previous Keyword Does Not Return A Value
    ${num}    Chain Keywords
    ...    Random Int    18     100
    ...    AND
    ...    Log
    ...    AND
    ...    Set Test Variable    $RANDOM_NUMBER
    Should Be Equal    ${num}    ${RANDOM_NUMBER}

Test ${SEPARATOR} Is The Only Valid Separator
    ${result}    Run Keyword And Return Status
    ...    Chain Keywords
    ...    Random Int    18    100
    ...    ->
    ...    Convert To String
    Should Not Be True    ${result}

Test ${SEPARATOR} Cannot Be First Argument
    Run Keyword And Expect Error    ${SEPARATOR} must have a keyword before and after.
    ...    Chain Keywords
    ...    AND
    ...    Random Int    18    100

Test ${SEPARATOR} Cannot Be Last Argument
    Run Keyword And Expect Error    ${SEPARATOR} must have a keyword before and after.
    ...    Chain Keywords
    ...    Random Int    18    100
    ...    AND
    ...    Convert To String
    ...    AND

Test ${SEPARATOR}s Cannot Be Together
    Run Keyword And Expect Error    ${SEPARATOR} must have a keyword before and after.
        ...    Chain Keywords
        ...    Random Int    18    100
        ...    AND
        ...    AND
        ...    Convert To String
