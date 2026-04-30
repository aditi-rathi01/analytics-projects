
#                             PROJECT BASED ON [CAR-SHOWROOM-ANALYSIS]

# -------------
# Introduction 
# -------------
# Suppose I am working as a Data Analyst in foriegn automobile company (XYZ) . This company made both Premimun and affordable cars. 
#        The company plans to extend its presence in India opening 20 Showrooms. (10 for each) My  responsibilty as a Data Analyst is to 
#        identify to best location across INDIA. where these showrooms can achieve maximum sales and growth.


# ----------
# OBJECTIVE 
# ----------
#  Which state will have high premium and affordable car demand next?


# -------------------------
# Key Business Questions
# -------------------------
# How does demand for premium vs affordable cars vary acoross states?
# which factors infulence car demand the most? (Income, GDP, Population, etc.)
# Which states are best suited for affordable car showrooms?  
# What business recomandation can be made based on the analysis.


#  -----------------------
#  Data Description 
# ------------------------
# The dataset inculeds the following columns:
# - State 
# - Year
# - GDP 
# - Per Capita Income
# - Population 
# - Car Sales Data
# - Data is collected for top-perfoming states over the last 7 years.


# --------------------
# Tools & Technologies 
# ---------------------
# - Python
# - Pandas
# - NumPy
# - Matplotlib
# - Statistics
# - Excel

# --------------------
# Data cleaning
# --------------------
# - Handling missing values
# - Remove duplicates
# - Ensure consistent state names
# - Covert data types
# - Standrazie unti

# ----------------------------
# Exploratory Data Analysis
# ---------------------------
# - State wise GDP comparison
# - Income distribuiton across states
# - Population analysis.


# --------------------
# Statistical Analyis
# ---------------------
# - Mean, Median, Standard deviation
# - Correlation Analysis
# - Identify relationship between variables.


#-----------------------------------------------
# Project Structure: 
# ----------------------------------------------
#  The project is divided into two parts : 
#       Part 1: Premium Car Analysis
#       Part 2: Affordable Car Analysis



# -------------------------------
# Part 1: Premium Car Analysis 
# ------------------------------



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


Data_2024 =  {
    "States" : ["Maharastra", "Uttar Pardesh", "Gujrat", "Karnatak", "Haryana", "Tamil Nadu", "Telangana", "Rajasthan", "Madhya Pardesh", "Delhi (NCR)", "Kerala", "Andhra Pardesh", "West Bengal", "Punjab", "Bihar"],
    "Approx.PV Sales (units)": [506254, 455530, 354054, 309464, 294331, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan ],
    "Approx. Market Share(%)": [11.8, 10.6, 8.2, 7.2, 6.8, 6.5, 5.6, 4.5, 4, 4, 3.5, 3, 3, 2.5, 2.5]
    
}

df_1 = pd.DataFrame(Data_2024)
#print(df_1)

x = df_1["States"]
y = df_1["Approx. Market Share(%)"]

plt.pie(y, labels= x, startangle= 90, shadow= True, autopct= "%.1f%%")
plt.title("Market_share_states")
#plt.legend()
plt.show()


# We have collected data on Passenger Vehicle (PV) sales across states.

# Now, we focus on the following factors:
# - Identify high competition and market Saturation.
# - Consider future growth.
# - Select atleast top 10 states for future analysis.

# Next Step: 
# We will collect:
# Per capita Income (for premium car analysis)
# Population data (for affordable car analysis).


Data1 = {
    "States": ["Maharastra", "Uttar Pardesh", "Gujrat", "Karnataka", "Haryana", "Tamil Nadu", "Telangana", "Rajasthan", "Madhya Pardesh", "Delhi", "Kerla", "Andhra Pardesh", "West Bengal", "Punjab", "Bihar"],
    "Per_capita_income_2024": [360000, 109000, 370000, 380000, 390000, 362000, 392000, 150000, 143000, 490000, 315000, 266000, 160000, 253000, 80000],
    "Population(millions, 2025-2026)": [129, 242, 71, 68, 30, 76, 38, 82, 89, 23, 35, 53, 100, 31, 132]
}

df_2 = pd.DataFrame(Data1)
print(df_2)

x1 = df_2["States"]
y1 = df_2["Per_capita_income_2024"]
z1 = df_2["Population(millions, 2025-2026)"]

plt.barh(x1, y1, label = "Per Capita Income")
plt.xlabel("States")
plt.ylabel("Per Capita Income")
plt.title("States vs Per Capita Income")
plt.show()


# -------------------------------
# Market Segmentation (Part- 1)
# --------------------------------

# Logic: 
# Premium Segment: States with high per capita income
# Affordable Segment: States with higher population.
# Now, Take out top 10 states on the basis of "Per capita Income" for opening of Premium Segment.


Premium_states = df_2.sort_values(by= "Per_capita_income_2024",ascending= False).head(10)

print("States for Premium showroom Opening: ")
Premium_states = Premium_states[["States", "Per_capita_income_2024"]]
print(Premium_states)


# Writting % urban in the following 10 States.

top_states_df = pd.DataFrame(Premium_states, columns= ["States"])    # To Seprate top 10 states from Dataframe "Premium_states"
top_states_df["Urban %"] = [98, 49, 43, 45, 49, 54, 49, 77, 37, 42]
print(top_states_df)

x = top_states_df["States"]
y = top_states_df["Urban %"]

plt.barh(x, y)
plt.title("Percentage of Urban in States")
plt.xlabel("States")
plt.ylabel("% Urban of in States")
plt.legend()
plt.show()

# -------------------------------------------
# Premium segmentation is based on a composite 
# score
# Combining income, urbanization, and market 
# share.
# This helps identify states with strong purchasing 
# power
# Urban market demand, and existing automobile market 
# presence.
# --------------------------------------------

# Now, merging data from different different DataFrames.

df_all = pd.merge(Premium_states, top_states_df, on= "States")
print(df_all)

# Now, sort Values on te basis of "Per_capita_income" and "% urban" for 7 states.
print("Final 7 States for further use: " )
df_final = df_all.head(7)
print(df_final)

# So, finall top 7 states list:
# - Delhi
# - Telangana
# - Haryana
# - Karnataka
# - Gujrat
# - Tamil Nadu
# - Maharastra

# -------------------------------
# ------------------------------
# Real Business Thinking
# -----------------------------
# Companies don't think:
# -> Where competition is lowest?

# They think:
# -> Where demand is highest?
# ------------------------------


# ----------------------------
# For now, focusing on Delhi, 
# Delhi deserves more weight(Two showrooms) because,
# - Very High income
# - 98 % urban 
# - Strong car demand
# ---------------------------



# Next Step:
# and select the best 2 location for showroom placement.

# ----------------------------
# Due to limited availablity of 
# micro- level data, location selection was based on secondary research and business logic.

# Connaught Place was selected for its high commerical activity,
# central location, and strong brand visibiltiy.

# Vasant kunj was selected due to its affluent residential due to its affluent residential poplulation, mall-driven lifestyle,
# and high purchasing power.
# ---------------------------------------------


# -----------------------------
# For Telangana, 
# Hyderabad, was identified as the primary market due to its economic growth and urbanization.

# Within Hyderabad, Jubilee Hills and Banjara Hills were selected as showroom locations due thier high-inceom population,
# premium lifestyle, and strong commerical presence, making them ideal for premium car demand.
# ---------------------------------


# --------------------------
# For Haryana,
# Gurugram and Faridabad show high income levels and a higher number of showrooms compared to other areas.
# -------------------------


# -----------------------
# For Karnataka
# Bangalore was selected due to its IT-driven econmoy, with Indiranagar choosen for its high-income poplulation, commercail
# activity, and premium lifestyle deamand.
# -----------------------


# ----------------------
# For Gujrat
# Ahmedabad was selected due to its strong business enivorment, with SG Highway chosen for its commerical growth, 
# Conncctivity, and increasing premium demand.
# ---------------------


# -------------------
#  Tamil Nadu
# Chennai was selected due to its strong industrial base, with OMR chosen for its urban growth, IT presence, and rising
# premium demand.
# -------------------

# -----------------
# Maharastra 

# Mumbai was selected due to its financial importance, with Bandra chosen for its premium lifestyle, high-income popluation
# and strong demadn for luxury vehicles.
# -----------------






# --------------------------------
# Part 2: Affordable Car Analysis
# -------------------------------

# For, Affrodable Car Showroom We are working on factor "Popluation".


Affordable_segment = df_2.sort_values(by= "Population(millions, 2025-2026)", ascending= False).head(10)
print("Affordable Segment")

print(df_1.columns)

High_deamand = df_1.sort_values(by= "Approx. Market Share(%)", ascending= False).head(10)
print(High_deamand)


Affordable_seg_df = pd.merge(
    High_deamand[["States","Approx. Market Share(%)"]],
    Affordable_segment[["States", "Population(millions, 2025-2026)"]],
    on= "States",
    how= "inner"
)
print(Affordable_seg_df)


# ------------------------------------------
# So, final List of Afforadable States are:
# ------------------------------------------- 

# - Maharastra
# - Uttar Pardesh
# - Gujrat
# - Tamil Nadu
# - Rajashtan
# - Madhya Pardesh




# ----------------------------
# For Uttar Pardesh , 
# - Lucknow, Kanpur, and Varanasi were selected due to its highest population(~241 million)
# -----------------------------


# -----------------------------
# For Maharashtra,
# Nagpur and Nashik were selected due to its large overall vehicle market size
# High total PV registration, and good potential in Tier-2 industrial areas for affordable cars.
# -----------------------------


# -----------------------------
# For Madhya Pardesh,
# Indore and Bhopal was selected due to its growing population(~89-90 million),
# Rising aspirations in central India, and increasing demand for budget segement vehicles.
# -----------------------------


# ------------------------------
# For Rajasthan
# Jaipur was selected due to its strong industrial ad agricluture base,
# good vehicle volume, and connectivity that supports affordable showroom reach.
# -------------------------------


# ----------------------------
# For Gujrat
# Rajkot was selected due to its string industrial and agricultural base,
# good vehicle volume, and connectivity that supports affordable showroom reach.
# ----------------------------


# ---------------------------
# For Tamil Nadu,
# Coimbatore was selected due to its large manufacturing workforce,
# decent afforable segment demand, and balanced urabn-rural market potential.
# --------------------------





#  This Project succesfully identified suitanle locations for premium and affordable car showroom, ensuring effective market coverage
#  and growth opportuntities. I sincerely appreciate the opportunity to work on this project. as it strengthend my interest in
# applying data-driven approcaches to real-world business problems.

# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

