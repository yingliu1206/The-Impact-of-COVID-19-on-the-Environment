#!/usr/bin/env python3
# -*- coding: utf-8 -*-        
import requests
import sys
import pandas as pd
            
            
def main():
    
    # Users enter the zip code for the first time.
    Zipcode=input("Enter Zip Code: ")

    orig_stdout = sys.stdout
    f=open("Part2_OUTFILE.txt", "w")
    sys.stdout = f
    
    ScrapeAirNow1(Zipcode)
    
    sys.stdout = orig_stdout
    
    f.close()

    # Continue or break?
    answer = input("Would you like to search again?: (yes/no)").lower()
    while True:
        if answer == 'yes':
           play = True
           break
        elif answer == 'no':
             play = False
             break
        else:
             answer = input('Incorrect option. Type "yes" to try again or "no" to leave": ').lower()
    
    # Users continue to enter zip code.
    play = True
    while play:
        
        # Enter the Zip Code.
        Zipcode=input("Enter Zip Code: ")
    
        orig_stdout = sys.stdout
        f=open("Part2_OUTFILE.txt", "a")
        sys.stdout = f
        
        ScrapeAirNow2(Zipcode)
    
        sys.stdout = orig_stdout
        f.close()
        
        # Continue or break?
        answer = input("Would you like to search again?: (yes/no)").lower()
        while True:
            if answer == 'yes':
               play = True
               break
            elif answer == 'no':
                 play = False
                 break
            else:
                 answer = input('Incorrect option. Type "yes" to try again or "no" to leave": ').lower()
    

def ScrapeAirNow1(Zipcode):

    date= '2020-07-20'
    # Setup parameters for API call
    URLPost = {'API_KEY': 'D3307BEF-E937-48EB-86BC-099763B1732B',
                    'zipCode': Zipcode,
                    #date format 2020-07-20
                    'date': date,
                    'distance': '25',
                    'format': 'application/json'}
    
    endpoint = "http://www.airnowapi.org/aq/forecast/zipCode/"
       
        
    response=requests.get(endpoint, URLPost)
    #txt = response.text
    #print(txt)
        
    # Get the json response and pull out fields to print
    jsontxt = response.json()
    for list in jsontxt:
        #print("List is ", list)
        AQIType = list['ParameterName']
        AQIValue = str(list['AQI'])
        State = list['StateCode']
        City = list['ReportingArea']
        DateFor=list['DateForecast']
        df = pd.DataFrame({'Zip Code': [Zipcode],
                           'City': [City],
                           'State': [State],
                           'Date': [DateFor],
                           'AQIType': [AQIType],
                           'AQIValue': [AQIValue]})
        print(df)


def ScrapeAirNow2(Zipcode):

    date= '2020-07-20'
    # Setup parameters for API call
    URLPost = {'API_KEY': 'D3307BEF-E937-48EB-86BC-099763B1732B',
                    'zipCode': Zipcode,
                    #date format 2020-07-20
                    'date': date,
                    'distance': '25',
                    'format': 'application/json'}
    
    endpoint = "http://www.airnowapi.org/aq/forecast/zipCode/"
       
        
    response=requests.get(endpoint, URLPost)
    #txt = response.text
    #print(txt)
        
    # Get the json response and pull out fields to print
    jsontxt = response.json()
    for list in jsontxt:
        #print("List is ", list)
        AQIType = list['ParameterName']
        AQIValue = str(list['AQI'])
        State = list['StateCode']
        City = list['ReportingArea']
        DateFor=list['DateForecast']
        df = pd.DataFrame({'Zip Code': [Zipcode],
                           'City': [City],
                           'State': [State],
                           'Date': [DateFor],
                           'AQIType': [AQIType],
                           'AQIValue': [AQIValue]})
        print(df.append(df))
    
main()
               
