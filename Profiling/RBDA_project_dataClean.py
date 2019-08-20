import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import pickle
from RBDA_project_dataX import pickle_file1

infile = open(pickle_file1, 'rb')
supersectors = pickle.load(infile)
infile.close()

def getCES(df):
    df = df.reset_index().drop(['index', 'id'], axis=1)
    df = df.loc[df['series_id'].str.slice(start=0, stop=3) == 'CES']
    df = df.loc[df['series_id'].str.slice(start=5, stop=11) == '000000']
    df.loc[df.period == 'M01', 'period'] = '01'
    df.loc[df.period == 'M02', 'period'] = '02'
    df.loc[df.period == 'M03', 'period'] = '03'
    df.loc[df.period == 'M04', 'period'] = '04'
    df.loc[df.period == 'M05', 'period'] = '05'
    df.loc[df.period == 'M06', 'period'] = '06'
    df.loc[df.period == 'M07', 'period'] = '07'
    df.loc[df.period == 'M08', 'period'] = '08'
    df.loc[df.period == 'M09', 'period'] = '09'
    df.loc[df.period == 'M10', 'period'] = '10'
    df.loc[df.period == 'M11', 'period'] = '11'
    df.loc[df.period == 'M12', 'period'] = '12'

    df['Timestamp'] = df.period + "-" + df.year.map(str)
    #df['timeStamp'] = df[['period', 'year']].apply(lambda x: '-'.join(x), axis = 1)
    return df

def allEmployees(df):
    df = df.loc[df['series_id'].str.slice(start=11, stop=13) == '01']
    return df

def avgWeeklyHrs(df):
    df = df.loc[df['series_id'].str.slice(start=11, stop=13) == '02']
    return df

def avgWeeklyEarning(df):
    df = df.loc[df['series_id'].str.slice(start=11, stop=13) == '11']
    return df

goods_producing = supersectors['06']
goods_producing_CES = getCES(goods_producing)
goods_producing_allEmployees = allEmployees(goods_producing_CES)
goods_producing_avgWeeklyHrs = avgWeeklyHrs(goods_producing_CES)
goods_producing_avgWeeklyEarning = avgWeeklyEarning(goods_producing_CES)

service_providing = supersectors['07']
service_providing_CES = getCES(service_providing)
service_providing_allEmployees = allEmployees(service_providing_CES)
service_providing_avgWeeklyHrs = avgWeeklyHrs(service_providing_CES)
service_providing_avgWeeklyEarning = avgWeeklyEarning(service_providing_CES)

private_service_providing = supersectors['08']
private_service_providing_CES = getCES(private_service_providing)
private_service_providing_allEmployees = allEmployees(private_service_providing_CES)
private_service_providing_avgWeeklyHrs = avgWeeklyHrs(private_service_providing_CES)
private_service_providing_avgWeeklyEarning = avgWeeklyEarning(private_service_providing_CES)

other_services = supersectors['80']
other_services_CES = getCES(other_services)
other_services_allEmployees = allEmployees(other_services_CES)
other_services_avgWeeklyHrs = avgWeeklyHrs(other_services_CES)
other_services_avgWeeklyEarning = avgWeeklyEarning(other_services_CES)

mining_and_logging = supersectors['10']
mining_and_logging_CES = getCES(mining_and_logging)
mining_and_logging_allEmployees = allEmployees(mining_and_logging_CES)
mining_and_logging_avgWeeklyHrs = avgWeeklyHrs(mining_and_logging_CES)
mining_and_logging_avgWeeklyEarning = avgWeeklyEarning(mining_and_logging_CES)

construction = supersectors['20']
construction_CES = getCES(construction)
construction_allEmployees = allEmployees(construction_CES)
construction_avgWeeklyHrs = avgWeeklyHrs(construction_CES)
construction_avgWeeklyEarning = avgWeeklyEarning(construction_CES)

manufacturing = supersectors['30']
manufacturing_CES = getCES(manufacturing)
manufacturing_allEployees = allEmployees(manufacturing_CES)
manufacturing_avgWeeklyHrs = avgWeeklyHrs(manufacturing_CES)
manufacturing_avgWeeklyEarning = avgWeeklyEarning(manufacturing_CES)

durable_goods = supersectors['31']
durable_goods_CES = getCES(durable_goods)
durable_goods_allEmployees = allEmployees(durable_goods_CES)
durable_goods_avgWeeklyHrs = avgWeeklyHrs(durable_goods_CES)
durable_goods_avgWeeklyearning = avgWeeklyEarning(durable_goods_CES)

nondurable_goods = supersectors['32']
nondurable_goods_CES = getCES(nondurable_goods)
nondurable_goods_allEmployees = allEmployees(nondurable_goods_CES)
nondurable_goods_avgWeeklyHrs = avgWeeklyHrs(nondurable_goods_CES)
nondurable_goods_avgWeeklyEarning = avgWeeklyEarning(nondurable_goods_CES)

trade_transportation_utilities = supersectors['40']
trade_transportation_utilities_CES = getCES(trade_transportation_utilities)
trade_transportation_utilities_allEmployees = allEmployees(trade_transportation_utilities_CES)
trade_transportation_utilities_avgWeeklyHrs = avgWeeklyHrs(trade_transportation_utilities_CES)
trade_transportation_utilities_avgWeeklyEarning = avgWeeklyEarning(trade_transportation_utilities_CES)

wholesale_trade = supersectors['41']
wholesale_trade_CES = getCES(wholesale_trade)
wholesale_trade_allEmployees = allEmployees(wholesale_trade_CES)
wholesale_trade_avgweeklyHrs = avgWeeklyHrs(wholesale_trade_CES)
wholesale_trade_avgWeeklyEarning = avgWeeklyEarning(wholesale_trade_CES)

retail_trade = supersectors['42']
retail_trade_CES = getCES(retail_trade)
retail_trade_allEmployees = allEmployees(retail_trade_CES)
retail_trade_avgWeeklyHrs = avgWeeklyHrs(retail_trade_CES)
retail_trade_avgWeeklyEarning = avgWeeklyEarning(retail_trade_CES)

transportation_and_wearhousing = supersectors['43']
transportation_and_wearhousing_CES = getCES(transportation_and_wearhousing)
transportation_and_wearhousing_allEmployees = allEmployees(transportation_and_wearhousing_CES)
transportation_and_wearhousing_avgWeeklyHrs = avgWeeklyHrs(transportation_and_wearhousing_CES)
transportation_and_wearhousing_avgweeklyEarning = avgWeeklyEarning(transportation_and_wearhousing_CES)

utilities = supersectors['44']
utilities_CES = getCES(utilities)
utilities_allEmployees = allEmployees(utilities_CES)
utilities_avgWeeklyHrs = avgWeeklyHrs(utilities_CES)
utilities_avgWeeklyEarning = avgWeeklyEarning(utilities_CES)

information = supersectors['50']
information_CES = getCES(information)
information_allEmployees = allEmployees(information_CES)
information_avgWeeklyHrs = avgWeeklyHrs(information_CES)
information_avgWeeklyEarning = avgWeeklyEarning(information_CES)

financial_activities = supersectors['55']
financial_activities_CES = getCES(financial_activities)
financial_activities_allEmployees = allEmployees(financial_activities_CES)
financial_activities_avgWeeklyHrs = avgWeeklyHrs(financial_activities_CES)
financial_activities_avgWeeklyEarning = avgWeeklyEarning(financial_activities_CES)

professional_and_business_services = supersectors['60']
professional_and_business_services_CES = getCES(professional_and_business_services)
professional_and_business_services_allEmployees = allEmployees(professional_and_business_services_CES)
professional_and_business_services_avgWeeklyHrs = avgWeeklyHrs(professional_and_business_services_CES)
professional_and_business_services_avgweeklyEarning = avgWeeklyEarning(professional_and_business_services_CES)

education_and_health_services = supersectors['65']
education_and_health_services_CES = getCES(education_and_health_services)
education_and_health_services_allEmployees = allEmployees(education_and_health_services_CES)
education_and_health_services_avgWeeklyHrs = avgWeeklyHrs(education_and_health_services_CES)
education_and_health_services_avgweeklyEarning = avgWeeklyEarning(education_and_health_services_CES)

leisure_and_hospitality = supersectors['70']
leisure_and_hospitality_CES = getCES(leisure_and_hospitality)
leisure_and_hospitality_allEmployees = allEmployees(leisure_and_hospitality_CES)
leisure_and_hospitality_avgWeeklyHrs = avgWeeklyHrs(leisure_and_hospitality_CES)
leisure_and_hospitality_avgWeeklyEarning = avgWeeklyEarning(leisure_and_hospitality_CES)

list_of_datasets = [
    goods_producing_allEmployees,#00
    goods_producing_avgWeeklyHrs,#01
    goods_producing_avgWeeklyEarning,#02
    service_providing_allEmployees,#03
    service_providing_avgWeeklyHrs,#04
    service_providing_avgWeeklyEarning,#05
    private_service_providing_allEmployees,#06
    private_service_providing_avgWeeklyHrs,#07
    private_service_providing_avgWeeklyEarning,#08
    other_services_allEmployees,#09
    other_services_avgWeeklyHrs,#10
    other_services_avgWeeklyEarning,#11
    mining_and_logging_allEmployees,#12
    mining_and_logging_avgWeeklyHrs,#13
    mining_and_logging_avgWeeklyEarning,#14
    construction_allEmployees,#15
    construction_avgWeeklyHrs,#16
    construction_avgWeeklyEarning,#17
    manufacturing_allEployees,#18
    manufacturing_avgWeeklyHrs,#19
    manufacturing_avgWeeklyEarning,#20
    durable_goods_allEmployees,#21
    durable_goods_avgWeeklyHrs,#22
    durable_goods_avgWeeklyearning,#23
    nondurable_goods_allEmployees,#24
    nondurable_goods_avgWeeklyHrs,#25
    nondurable_goods_avgWeeklyEarning,#26
    trade_transportation_utilities_allEmployees,#27
    trade_transportation_utilities_avgWeeklyHrs,#28
    trade_transportation_utilities_avgWeeklyEarning,#29
    wholesale_trade_allEmployees,#30
    wholesale_trade_avgweeklyHrs,#31
    wholesale_trade_avgWeeklyEarning,#32
    retail_trade_allEmployees,#33
    retail_trade_avgWeeklyHrs,#34
    retail_trade_avgWeeklyEarning,#35
    transportation_and_wearhousing_allEmployees,#36
    transportation_and_wearhousing_avgWeeklyHrs,#37
    transportation_and_wearhousing_avgweeklyEarning,#38
    utilities_allEmployees,#39
    utilities_avgWeeklyHrs,#40
    utilities_avgWeeklyEarning,#41
    information_allEmployees,#42
    information_avgWeeklyHrs,#43
    information_avgWeeklyEarning,#44
    financial_activities_allEmployees,#45
    financial_activities_avgWeeklyHrs,#46
    financial_activities_avgWeeklyEarning,#47
    professional_and_business_services_allEmployees,#48
    professional_and_business_services_avgWeeklyHrs,#49
    professional_and_business_services_avgweeklyEarning,#50
    education_and_health_services_allEmployees,#51
    education_and_health_services_avgWeeklyHrs,#52
    education_and_health_services_avgweeklyEarning,#53
    leisure_and_hospitality_allEmployees,#54
    leisure_and_hospitality_avgWeeklyHrs,#55
    leisure_and_hospitality_avgWeeklyEarning,#56
]

pickle_file2 = 'list_of_datasets'
outfile = open(pickle_file2, 'wb')
pickle.dump(list_of_datasets, outfile)
outfile.close()
