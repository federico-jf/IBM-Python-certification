import csv, sqlite3
con = sqlite3.connect("Test3.db")
cur = con.cursor()

!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///Test3.db

import pandas
df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv")
df.to_sql("CENSUS_DATA", con, if_exists='replace', index=False,method="multi")

df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv")
df.to_sql("CHICAGO_CRIME_DATA", con, if_exists='replace', index=False, method="multi")

df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False, method="multi")

%sql SELECT name FROM sqlite_master WHERE type='table'

# number of columns
%sql SELECT count(name) FROM PRAGMA_TABLE_INFO ('CHICAGO_PUBLIC_SCHOOLS_DATA');

# list of columns and data type
%sql SELECT name, type, length(type) FROM PRAGMA_TABLE_INFO ('CHICAGO_PUBLIC_SCHOOLS_DATA');

# number of elementary schools
%sql SELECT count(*) FROM CHICAGO_PUBLIC_SCHOOLS_DATA where "Elementary, Middle, or High School"='ES';

# highest safety score
%sql SELECT MAX(Safety_Score) FROM CHICAGO_PUBLIC_SCHOOLS_DATA;

# schools with highets satefy score
%sql SELECT Name_of_School, Safety_Score FROM CHICAGO_PUBLIC_SCHOOLS_DATA WHERE Safety_Score = 99;

# top 10 schools with highest average student attendance
%sql SELECT Name_of_School, Average_Student_Attendance FROM CHICAGO_PUBLIC_SCHOOLS_DATA order by Average_Student_Attendance desc nulls last LIMIT 10;

# 5 shcools with lowest average student attendance sorted in ascending order
%sql SELECT Name_of_School, Average_Student_Attendance FROM CHICAGO_PUBLIC_SCHOOLS_DATA order by Average_Student_Attendance LIMIT 5;

# remove the percentage sign from the result above
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance,'%','') FROM CHICAGO_PUBLIC_SCHOOLS_DATA order by Average_Student_Attendance LIMIT 5;

# schools with avg student attendance lower than 70% 
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance,'%','') FROM CHICAGO_PUBLIC_SCHOOLS_DATA WHERE Average_Student_Attendance <70;

# Total College Enrollment for each Community Area
%sql SELECT Community_Area_Name, SUM(College_Enrollment) AS TOTAL_ENROLLMENT FROM CHICAGO_PUBLIC_SCHOOLS_DATA group by Community_Area_Name;

# 5 commungty areas with the least total college enrollment sorted in ascending
%sql SELECT Community_Area_Name, SUM(College_Enrollment) AS TOTAL_ENROLLMENT FROM CHICAGO_PUBLIC_SCHOOLS_DATA \
group by Community_Area_Name \
order by TOTAL_ENROLLMENT asc \
LIMIT 5;

#5 schools with lowest safety score
%sql SELECT Name_of_School, Safety_Score FROM CHICAGO_PUBLIC_SCHOOLS_DATA \
WHERE Safety_Score !='None'\
order by Safety_Score asc \
LIMIT 5;

# hardship index for community area which has a college enrollment of 4368

%sql SELECT Hardship_Index FROM CENSUS_DATA CD, CHICAGO_PUBLIC_SCHOOLS_DATA CPS
WHERE CD.community_area_number = CPS.community_area_number
and College_Enrollment = 4368;

# hardship index for the community with the highest value for college enrollment
%sql SELECT community_area_number, community_area_name, hardship_index FROM CENSUS_DATA \
WHERE community_area_number in \
(select community_area_number from CHICAGO_PUBLIC_SCHOOLS_DATA order by College_Enrollment desc limit 1);




############### FINAL ASSIGNMENT

# Total number of crimes
%sql SELECT count(*) FROM CHICAGO_CRIME_DATA;

# List of community area names and numbers with per capita income less than 11000
%sql SELECT COMMUNITY_AREA_NAME, COMMUNITY_AREA_NUMBER FROM CENSUS_DATA WHERE PER_CAPITA_INCOME <11000;

# List all case numbers for crimes involving minors
%sql SELECT CASE_NUMBER, DESCRIPTION FROM CHICAGO_CRIME_DATA where "PRIMARY_TYPE" = 'LIQUOR LAW VIOLATION';

# List all kidnapping crimes involving a child
%sql SELECT CASE_NUMBER, PRIMARY_TYPE, DESCRIPTION FROM CHICAGO_CRIME_DATA where "PRIMARY_TYPE" = 'KIDNAPPING' AND "DESCRIPTION" LIKE '%child%';

# List the kind of crimes that were recorded at schools (No repetitions)

%sql SELECT DISTINCT PRIMARY_TYPE FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%';

# List the type of schools along with the average safety score for each type
%sql SELECT "Elementary, Middle, or High School" AS School_Type, AVG(SAFETY_SCORE) AS Average_Safety_Score FROM CHICAGO_PUBLIC_SCHOOLS GROUP BY "Elementary, Middle, or High School";

# List 5 community areas wiith highest % of households below poverty line
%sql SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CENSUS_DATA order by PERCENT_HOUSEHOLDS_BELOW_POVERTY desc nulls last LIMIT 5;

# Which community area is most crime prone? Display the community numer only
%sql SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(*) DESC LIMIT 1;

# Use subquery to find the name of the community area with highest hardship index
%sql SELECT community_area_name FROM CHICAGO_PUBLIC_SCHOOLS_DATA 
WHERE community_area_number IN 
(SELECT community_area_number FROM CENSUS_DATA ORDER BY hardship_index DESC LIMIT 1);

# or
%sql SELECT community_area_name
FROM CENSUS_DATA
WHERE hardship_index = (
    SELECT MAX(hardship_index)
    FROM CENSUS_DATA
);

# Use subquery to find the name of the community area with most number of crimes

%sql SELECT community_area_name
FROM CENSUS_DATA
WHERE community_area_number = (
    SELECT community_area_number
    FROM (
        SELECT community_area_number, COUNT(*) AS num_crimes
        FROM CHICAGO_CRIME_DATA
        GROUP BY community_area_number
        ORDER BY num_crimes DESC
        LIMIT 1
    ) AS subquery
);

