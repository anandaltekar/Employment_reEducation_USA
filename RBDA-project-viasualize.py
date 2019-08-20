import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cols = [
        'goods_producing', 'durable_goods', 'education_and_health_services', 'financial_activities',
        'information', 'mining_and_logging', 'nondurable_goods', 'other_services', 'private_service_providing',
        'professional_and_business_services', 'retail_trade', 'service_providing',
        'trade_transportation_utilities', 'transportation_and_wearhousing'
    ]
dfrm_one = pd.read_csv("results/employment_forecasts/tables/construction_allEmployees.csv")
name_one = 'Goods-Producing'

dfrm_two = pd.read_csv("results/employment_forecasts/tables/durable_goods_allEmployees.csv")
name_two = "Durable Goods"

dfrm_three = pd.read_csv("results/employment_forecasts/tables/education_and_health_services_allEmployees.csv")
name_three = 'Education & Health Services'

dfrm_four = pd.read_csv("results/employment_forecasts/tables/financial_activities_allEmployees.csv")
name_foufive = 'Financial Activities'

dfrm_five = pd.read_csv("results/employment_forecasts/tables/information_allEmployees.csv")
name_five = 'Information'

dfrm_six = pd.read_csv("results/employment_forecasts/tables/mining_and_logging_allEmployees.csv")
name_six = 'Mining & Logging'

dfrm_seven = pd.read_csv("results/employment_forecasts/tables/nondurable_goods_allEmployees.csv")
name_seven = 'Non-Durable Goods'

dfrm_eight = pd.read_csv("results/employment_forecasts/tables/other_services_allEmployees.csv")
name_eight = 'Other Services'

dfrm_nine = pd.read_csv("results/employment_forecasts/tables/private_service_providing_allEmployees.csv")
name_nine = 'Private Service Providing'

dfrm_ten = pd.read_csv("results/employment_forecasts/tables/professional_and_business_services_allEmployees.csv")
name_ten = 'Professional & Business Services'

dfrm_eleven = pd.read_csv("results/employment_forecasts/tables/retail_trade_allEmployees.csv")
name_eleven = 'Retail Trade'

dfrm_twelve = pd.read_csv("results/employment_forecasts/tables/service_providing_allEmployees.csv")
name_twelve = 'Service Providing'

dfrm_thirteen = pd.read_csv("results/employment_forecasts/tables/trade_transportation_utilities_allEmployees.csv")
name_thirteen = 'Trade, Transportation & Utilities'

dfrm_fourteen = pd.read_csv("results/employment_forecasts/tables/transportation_and_wearhousing_allEmployees.csv")
name_fourteen = 'Transportation & Wearhousing'

frames = [ dfrm_one, dfrm_two, dfrm_three, dfrm_four, dfrm_five, dfrm_six, dfrm_seven, dfrm_eight, dfrm_nine, dfrm_ten, dfrm_eleven, dfrm_twelve, dfrm_thirteen, dfrm_fourteen]

for df in frames:
    df = df.set_index('Timestamp')
    df.set_index('Timestamp').plot()
    #print (df)



# fig = plt.figure(figsize=(15,7))
# fig.subtitle("Employment Treds 2007-2018, Forcast:2019", fontsize=20)
# ax1 = fig.add_subplot(231)
# ax1.set_title("")
