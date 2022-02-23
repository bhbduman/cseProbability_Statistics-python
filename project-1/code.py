import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt 

df = pd.read_csv('owid-covid-data.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df.head())

#df.info()
countries_list= df['location'].tolist()
countries_set = set(countries_list)
#print(countries_set)
print("1. How many countries the dataset has ?")
print(len(countries_set))
print("----------------------------------------")


contry_groupby = df.groupby(['location'])
date_earliest_each = contry_groupby.agg(Earliest_Date=('date',np.min))
#date_earliest = date_earliest_each.agg(Minumum_Date=('date',))
print("2. When is the earliest date data are taken for a country? Which country is it ?")
print(date_earliest_each[date_earliest_each.eq(date_earliest_each.min()).any(1)])
print("----------------------------------------")


totalcases_each= contry_groupby.agg(q3_Total_Cases= ('total_cases',np.max))
print("3. How many cases are confirmed for each country so far? Print pairwise results of country and total cases.")
print(totalcases_each)
print("----------------------------------------")


totaldeaths_each= contry_groupby.agg(q4_Total_Deaths= ('total_deaths',np.max))
print("4. How many deaths are confirmed for each country so far? Print pairwise results of country and total deaths.")
print(totaldeaths_each)
print("----------------------------------------")


reproduction_each= contry_groupby.agg(q5_minimum=('reproduction_rate', np.min), q5_maximum=('reproduction_rate', np.max), q5_average=('reproduction_rate', np.mean), q5_variation=('reproduction_rate', np.var))
print("5. What are the average, minimum, maximum and variation values of the reproduction rates for each country ?")
print(reproduction_each)
print("----------------------------------------")


icupatients_each= contry_groupby.agg(q6_minimum=('icu_patients', np.min), q6_maximum=('icu_patients', np.max), q6_average=('icu_patients', np.mean), q6_variation=('icu_patients', np.var))
print("6. What are the average, minimum, maximum and variation values of the icu patients (intensive care unit patients) for each country?")
print(icupatients_each)
print("----------------------------------------")


hosp_patients= contry_groupby.agg(q7_minimum=('hosp_patients', np.min), q7_maximum=('hosp_patients', np.max), q7_average=('hosp_patients', np.mean), q7_variation=('hosp_patients', np.var))
print("7. What are the average, minimum, maximum and variation values of the hosp patients (hospital patients) for each country?")
print(hosp_patients)
print("----------------------------------------")


weekly_icu_admissions= contry_groupby.agg(q8_minimum=('weekly_icu_admissions', np.min), q8_maximum=('weekly_icu_admissions', np.max), q8_average=('weekly_icu_admissions', np.mean), q8_variation=('weekly_icu_admissions', np.var))
print("8. What are the average, minimum, maximum and variation values of the weekly icu (intensive care unit) admissions for each country?")
print(weekly_icu_admissions)
print("----------------------------------------")


weekly_hosp_admissions= contry_groupby.agg(q9_minimum=('weekly_hosp_admissions', np.min), q9_maximum=('weekly_hosp_admissions', np.max), q9_average=('weekly_hosp_admissions', np.mean), q9_variation=('weekly_hosp_admissions', np.var))
print("9. What are the average, minimum, maximum and variation values of the weekly hospital admissions for each country?")
print(weekly_hosp_admissions)
print("----------------------------------------")


new_tests= contry_groupby.agg(q10_minimum=('new_tests', np.min), q10_maximum=('new_tests', np.max), q10_average=('new_tests', np.mean), q10_variation=('new_tests', np.var))
print("10. What are the average, minimum, maximum and variation values of new tests per day for each country?")
print(new_tests)
print("----------------------------------------")


total_tests= contry_groupby.agg(q11_total_test=('total_tests', np.max))
print("11. How many tests are conducted in total for each country so far?")
print(total_tests)
print("----------------------------------------")


positive_rate= contry_groupby.agg(q12_minimum=('positive_rate', np.min), q12_maximum=('positive_rate', np.max), q12_average=('positive_rate', np.mean), q12_variation=('positive_rate', np.var))
print("12. What are the average, minimum, maximum and variation values of the positive rates of the tests for each country?")
print(positive_rate)
print("----------------------------------------")


tests_per_case= contry_groupby.agg(q13_minimum=('tests_per_case', np.min), q13_maximum=('tests_per_case', np.max), q13_average=('tests_per_case', np.mean), q13_variation=('tests_per_case', np.var))
print("13. What are the average, minimum, maximum and variation values of the tests per case for each country?")
print(tests_per_case)
print("----------------------------------------")


people_vaccinated= contry_groupby.agg(q14_People_Fully_Vaccianated= ('people_vaccinated',np.max))
print("14. How many people are vaccinated by at least one dose in each country?")
print(people_vaccinated)
print("----------------------------------------")

people_fully_vaccinated= contry_groupby.agg(q15_People_Fully_Vaccianated= ('people_fully_vaccinated',np.max))
print("15. How many people are vaccinated fully in each country?")
print(people_fully_vaccinated)
print("----------------------------------------")

total_vaccinations = contry_groupby.agg(q16_total_vaccinations= ('total_vaccinations',np.max))
print("16. How many vaccinations are administered in each country so far?")
print(total_vaccinations)
print("----------------------------------------")


info = contry_groupby.agg(q17_population= ('population',np.max), q17_median_age= ('median_age',np.max), q17_aged_65_older= ('aged_65_older',np.max),q17_aged_70_older= ('aged_70_older',np.max),q17_gdp_per_capita= ('gdp_per_capita',np.max),q17_cardiovasc_death_rate= ('cardiovasc_death_rate',np.max),q17_diabetes_prevalence= ('diabetes_prevalence',np.max),q17_female_smokers= ('female_smokers',np.max),q17_male_smokers= ('male_smokers',np.max),q17_handwashing_facilities= ('handwashing_facilities',np.max),q17_hospital_beds_per_thousand= ('hospital_beds_per_thousand',np.max),q17_life_expectancy= ('life_expectancy',np.max), q17_human_development_index= ('human_development_index',np.max), )
print("17. List information about population, median age, # of people aged 65 older, # of people aged 70 older, economic performance, death rates due to heart disease, diabetes prevalence,  of female smokers,  of male smokers, handwashing facilities, hospital beds per thousand people, life expectancy and human development index.")
print(info)
print("----------------------------------------")

file= open("output.txt","w")
print("18. Summarize all the results that you obtain by the first 17 questions (except question 2).")
result = pd.concat([totalcases_each, totaldeaths_each,reproduction_each ,icupatients_each ,hosp_patients ,weekly_icu_admissions ,weekly_hosp_admissions ,new_tests ,total_tests ,positive_rate ,tests_per_case ,people_vaccinated ,people_fully_vaccinated,total_vaccinations,info ], axis=1)
print(result)
file.write(result.to_string())
file.close()
print("----------------------------------------")
