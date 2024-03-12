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