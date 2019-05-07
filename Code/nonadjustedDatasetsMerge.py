import pandas as pd

"reading csv files and creating dataframes"
bank_prime_loan_rate = pd.read_csv("1959_2018_Monthly_Bank_Prime_Loan_Rate_NSA_FRED.csv", names=["date", "bank_prime_loan_rate"])
bank_prime_loan_rate = bank_prime_loan_rate.drop(bank_prime_loan_rate.index[0])

cpi_fuels_utilities = pd.read_csv("1959_2018_Monthly_CPI_Fuels_Utilities_NSA_FRED.csv", names=["date", "cpi_fuels_utilities"])
cpi_fuels_utilities = cpi_fuels_utilities.drop(cpi_fuels_utilities.index[0])

cpi_new_vehicles = pd.read_csv("1959_2018_Monthly_CPI_New_Vehicles_NSA_FRED.csv", names=["date", "cpi_new_vehicles"])
cpi_new_vehicles = cpi_new_vehicles.drop(cpi_new_vehicles.index[0])

cpi_purchasing_power_dollar = pd.read_csv("1959_2018_Monthly_CPI_Purchasing_Power_Dollar_NSA_FRED.csv", names=["date", "cpi_purchasing_power_dollar"])
cpi_purchasing_power_dollar = cpi_purchasing_power_dollar.drop(cpi_purchasing_power_dollar.index[0])

cpi_urban_clerical = pd.read_csv("1959_2018_Monthly_CPI_Urban_Clerical_Purchasing_Power_Consumer_Dollar_NSA_FRED.csv", names=["date", "cpi_urban_clerical"])
cpi_urban_clerical = cpi_urban_clerical.drop(cpi_urban_clerical.index[0])

currency_circulation = pd.read_csv("1959_2018_Monthly_Currency_Circulation_Outstanding_NSA_FRED.csv", names=["date", "currency_circulation"])
currency_circulation = currency_circulation.drop(currency_circulation.index[0])

federal_minimum_wage = pd.read_csv("1959_2018_Monthly_CPI_Fed_Min_Wage_NSA_FRED.csv", names=["date", "federal_minimum_wage"])
federal_minimum_wage = federal_minimum_wage.drop(federal_minimum_wage.index[0])

m1_money_stock = pd.read_csv("1959_2018_Monthly_M1_Money_Stock_NSA_FRED.csv", names=["date", "m1_money_stock"])
m1_money_stock = m1_money_stock.drop(m1_money_stock.index[0])

m2_money_stock = pd.read_csv("1959_2018_Monthly_M2_Money_Stock_NSA_FRED.csv", names=["date", "m2_money_stock"])
m2_money_stock = m2_money_stock.drop(m2_money_stock.index[0])

m2_own_rate = pd.read_csv("1959_2018_Monthly_M2_Own_Rate_NSA_FRED.csv", names=["date", "m2_own_rate"])
m2_own_rate = m2_own_rate.drop(m2_own_rate.index[0])

total_consumer_credit = pd.read_csv("1959_2018_Monthly_Consumer_Credit_Outstanding_NSA_FRED.csv", names=["date", "consumer_credit"])
total_consumer_credit = total_consumer_credit.drop(total_consumer_credit.index[0])

unemployment_rate = pd.read_csv("1959_2018_Monthly_Unemployment_Rate_20_Over_NSA_FRED.csv", names=["date", "unemployment_rate"])
unemployment_rate = unemployment_rate.drop(unemployment_rate.index[0])

employees_payroll = pd.read_csv("1959_2018_Monthly_All_Employees_Total_Payroll_NSA_FRED.csv", names=["date", "employees_payroll"])
employees_payroll = employees_payroll.drop(employees_payroll.index[0])

cpi_commodities = pd.read_csv("1959_2018_Monthly_CPI_Commodities_NSA_FRED.csv", names=["date", "cpi_commodities"])
cpi_commodities = cpi_commodities.drop(cpi_commodities.index[0])

cpi_core_urban_consumers = pd.read_csv("1959_2018_Monthly_CPI_Core_All_Urban_Consumers_NSA_FRED.csv", names=["date", "cpi_core_urban_consumers"])
cpi_core_urban_consumers = cpi_core_urban_consumers.drop(cpi_core_urban_consumers.index[0])

cpi_core_urban_consumers_exclude_food_energy = pd.read_csv("1959_2018_Monthly_CPI_Core_All_Urban_Consumers_Exclude_Food_Energy_NSA_FRED.csv", names=["date", "cpi_core_urban_consumers_exclude_food_energy"])
cpi_core_urban_consumers_exclude_food_energy = cpi_core_urban_consumers_exclude_food_energy.drop(cpi_core_urban_consumers_exclude_food_energy.index[0])

cpi_fuels_transportation = pd.read_csv("1959_2018_Monthly_CPI_Fuels_Transportation_NSA_FRED.csv", names=["date", "cpi_fuels_transportation"])
cpi_fuels_transportation = cpi_fuels_transportation.drop(cpi_fuels_transportation.index[0])

cpi_rent_primary = pd.read_csv("1959_2018_Monthly_CPI_Rent_Primary_Residence_NSA_FRED.csv", names=["date", "cpi_rent_primary"])
cpi_rent_primary = cpi_rent_primary.drop(cpi_rent_primary.index[0])

monetary_base = pd.read_csv("1959_2018_Monthly_Monetary_Base_NSA_FRED.csv", names=["date", "monetary_base"])
monetary_base = monetary_base.drop(monetary_base.index[0])

savings_deposits = pd.read_csv("1959_2018_Monthly_Savings_Deposits_Total_NSA_FRED.csv", names=["date", "savings_deposits"])
savings_deposits = savings_deposits.drop(savings_deposits.index[0])

owned_housing_units = pd.read_csv("1959_2018_Monthly_Total_New_Privately_Owned_Housing_Units_Started_NSA_FRED.csv", names=["date", "owned_housing_units"])
owned_housing_units = owned_housing_units.drop(owned_housing_units.index[0])

"merging datasets"
merge = pd.merge(bank_prime_loan_rate, owned_housing_units, how="outer", on=["date"])
merge = pd.merge(merge, cpi_fuels_transportation, how="outer", on=["date"])
merge = pd.merge(merge, cpi_fuels_utilities, how="outer", on=["date"])
merge = pd.merge(merge, cpi_new_vehicles, how="outer", on=["date"])
merge = pd.merge(merge, cpi_purchasing_power_dollar, how="outer", on=["date"])
merge = pd.merge(merge, monetary_base, how="outer", on=["date"])
merge = pd.merge(merge, cpi_urban_clerical, how="outer", on=["date"])
merge = pd.merge(merge, cpi_rent_primary, how="outer", on=["date"])
merge = pd.merge(merge, currency_circulation, how="outer", on=["date"])
merge = pd.merge(merge, federal_minimum_wage, how="outer", on=["date"])
merge = pd.merge(merge, m1_money_stock, how="outer", on=["date"])
merge = pd.merge(merge, m2_money_stock, how="outer", on=["date"])
merge = pd.merge(merge, m2_own_rate, how="outer", on=["date"])
merge = pd.merge(merge, cpi_core_urban_consumers, how="outer", on=["date"])
merge = pd.merge(merge, cpi_core_urban_consumers_exclude_food_energy, how="outer", on=["date"])
merge = pd.merge(merge, cpi_commodities, how="outer", on=["date"])
merge = pd.merge(merge, employees_payroll, how="outer", on=["date"])
merge = pd.merge(merge, total_consumer_credit, how="outer", on=["date"])
merge = pd.merge(merge, unemployment_rate, how="outer", on=["date"])
merge = pd.merge(merge, savings_deposits, how="outer", on=["date"])

"dropping all CPI data except for cpi_core_urban_consumers and cpi_core_urban_consumers_exclude_food_energy"
merge = merge.drop(["cpi_fuels_utilities",
                    "cpi_new_vehicles",
                    "cpi_purchasing_power_dollar",
                    "cpi_urban_clerical",
                    "cpi_commodities",
                    "cpi_fuels_transportation",
                    "cpi_rent_primary"], axis=1)

"convert each month into a dataset"
for i in range(1, 13):
    this_month_df = pd.DataFrame.copy(merge)
    this_month_str = str(i)

    if len(this_month_str) == 1:
        this_month_str = "0" + this_month_str

    for index_drop, row in this_month_df.iterrows():
        row_month = row['date'].split("-")[1]
        if row_month != this_month_str:
            this_month_df.drop(index=index_drop, inplace=True)

    path = r"NonAdjustedMonthlyDataset_" + this_month_str + ".csv"
    this_month_df.to_csv(path, index=None, header=True)

"converting entire dataset to csv"
merge.to_csv(r"NonAdjustedMonthlyDataset.csv", index=None, header=True)
