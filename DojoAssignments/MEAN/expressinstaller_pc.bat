ECHO calling npm init -y
CALL npm init -y
@echo off
SET /P packages= "Enter 1 for custom installation or press enter for default installation: "

IF "%packages%"==""(ECHO //default installation\\)

IF "%packages%"=="1"(ECHO //custom installation\\)
