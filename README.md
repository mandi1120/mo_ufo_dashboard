# Missouri UFO Sightings Dashboard  
A Power BI report built on data from [National UFO Reporting Center]( https://nuforc.org/)  
Created 2/18/23  

#### Dashboard:  
![Dashboard](supporting_files/Dashboard.png)  

#### Detail View:
![Detail](supporting_files/Detail.png)  

## Overview:
I find the topic of UFO's intriguing, so I chose to use reported UFO sightings as a way to demonstrate my skills in data cleansing, python, and Power BI development. The result, pictured above and detailed below, is an accurate example of a report that I would create professionally. 

#### Dashboard:
The Dashboard provides insights into the NUFORC data through visualizations.  

After some initial exploratory data analysis, I identified several questions that someone with an interest in the topic may ask, then set out to answer these questions through visuals.

- What UFO shape is seen most often?
- What UFO shape has the longest average sighting duration?
- What general time of day do most sightings take place?
- Which cities have the most sightings?
- Which months/years have had the most sightings? 

The resulting dashboard provides these insights, and can be filtered in various ways for further analysis.

Visuals:
- Summary Cards:  
    - Total Sightings
    - Total Cities with Sightings
    - Average Duration for All Sightings
- Charts:  
    - Sightings by Time of Day
        - This column chart summarizes the sightings by time of day (morning, afternoon, evening, overnight). 
    - Average Duration of UFO Sightings by Shape
        - This scatter chart visualizes the average duration of sightings, broken out by the observed shape of the UFO.
    - UFO Hot Spots
        - This heat map allows the user to observe areas with greater propensities for sightings.
    - Observed Shape
        - This bar chart provides insight into the shapes most frequently reported. Categories in dark blue represent the top 50% of sightings.
    - UFO Sightings Trend 
        - This line chart visualizes sightings over time.  The user can also drill down to view the chart by month.
- Slicers:  
    - Timeframe (year, month)
    - Time of Day (early morning, morning, afternoon, evening, late night)
    - City
    - Shape

#### Report Detail:
The Report Detail page provides the detailed submission for each sighting.  

## Development Approach:
The following steps were taken to cleanse the data and apply some standardization to city names to generate coordinates for mapping, before being loaded into Power BI for further cleansing and development.  
    
1. Data was manually copied from https://nuforc.org/webreports/ndxlMO.html and saved in excel.  
2. Cities were copied into a new csv file, some initial standardization was done, and duplicates were removed.  
3. The geocode python script was run to get coordinates by city in the cities_output.csv file.  
4. The coordinates and standardized cities were pulled into the data file using vlookup formulas with wildcard matching.  
5. Several formulas were used to extract the duration amount from the duration text field, which was then converted into seconds.  
6. The xlsx data file was loaded into Power BI.  
7. Additional data cleansing was done in Power Query, including changing column types as needed (text to dates, whole numbers), standardizing capitalization, extracting datetime into year, date, and time columns, removing errors, filtering to needed timeframe.  
8. A calculated calendar table was created, and calculated columns for year, month, day were added, using DAX.  
9. Visuals were developed.  
  
#### Enhancement Opportunities:
The following are areas for improvement with future updates:
- Automate data refresh - write a python script to scrape the data from the webpage.
- Improve geocode script - many cities did not pull coordinates due to misspellings or unrecognized formatting.
- Improve extraction of duration time - write a python script to replace formulas to extract numbers from text.
  
Logo and header image are credited to NUFORC.org  








