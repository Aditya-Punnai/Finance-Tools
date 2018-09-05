import pandas as pd
#Berkshire
df_2018_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012318008866/xslForm13F_X01/form13fInfoTable.xml")
df_2018_05_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012318005732/xslForm13F_X01/form13fInfoTable.xml")
df_2018_02_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012318002390/xslForm13F_X01/form13fInfoTable.xml")
df_2017_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012317010896/xslForm13F_X01/form13fInfoTable.xml")
df_2017_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012317007953/xslForm13F_X01/form13fInfoTable.xml")
df_2017_05_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012317005259/xslForm13F_X01/form13fInfoTable.xml")
df_2017_02_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012317002417/xslForm13F_X01/form13fInfoTable.xml")
df_2016_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012316022377/xslForm13F_X01/form13fInfoTable.xml")
df_2016_08_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012316020120/xslForm13F_X01/form13fInfoTable.xml")
df_2016_05_16 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012316017295/xslForm13F_X01/form13fInfoTable.xml")
df_2016_02_16 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012316015025/xslForm13F_X01/form13fInfoTable.xml")
df_2015_11_16 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012315011992/xslForm13F_X01/form13fInfoTable.xml")
df_2015_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012315009404/xslForm13F_X01/form13fInfoTable.xml")
df_2015_05_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012315006438/xslForm13F_X01/form13fInfoTable.xml")
df_2015_02_17 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012315002961/xslForm13F_X01/form13fInfoTable.xml")
df_2014_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012314012218/xslForm13F_X01/form13fInfoTable.xml")
df_2014_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012314009048/xslForm13F_X01/form13fInfoTable.xml")
df_2014_05_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012314006252/xslForm13F_X01/form13fInfoTable.xml")
df_2014_02_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012314002615/xslForm13F_X01/form13fInfoTable.xml")
df_2013_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/1067983/000095012313009777/xslForm13F_X01/form13fInfoTable.xml")

pd.set_option("display.max_rows",500)
pd.set_option("display.max_columns",100)
pd.set_option("display.max_colwidth",20)

df_df = [df_2018_08_14,df_2018_05_15,df_2018_02_14,
         df_2017_11_14,df_2017_08_14,df_2017_05_15,
     df_2017_02_14,df_2016_11_14,df_2016_08_15,df_2016_05_16,
     df_2016_02_16,df_2015_11_16,
     df_2015_08_14,df_2015_05_15,df_2015_02_17,df_2014_11_14,
     df_2014_08_14,df_2014_05_15,
     df_2014_02_14,df_2013_11_14]

df_names= ["df_2018_08_14","df_2018_05_15","df_2018_02_14",
         "df_2017_11_14","df_2017_08_14","df_2017_05_15",
     "df_2017_02_14","df_2016_11_14","df_2016_08_15","df_2016_05_16",
     "df_2016_02_16","df_2015_11_16",
     "df_2015_08_14","df_2015_05_15","df_2015_02_17","df_2014_11_14",
     "df_2014_08_14","df_2014_05_15",
     "df_2014_02_14","df_2013_11_14"]

df_df2 =[]
for i in df_df:
    df_df2.append(i[-1].iloc[2:,:])

title = ["Name of issuer","Title of class","CUSIP","Value (x$1000)","SHR/PRN AMT","SH/PRN",
         "PUT/CALL","Investment Descretion","Other Managers","Voting Sole","Authority Share","NONE"]
for i in df_df2:    
    i.iloc[[0],:] = title
    
for i in df_df2:
    i = pd.DataFrame(i)
df_names= ["df_2018_08_14","df_2018_05_15","df_2018_02_14",
         "df_2017_11_14","df_2017_08_14","df_2017_05_15",
     "df_2017_02_14","df_2016_11_14","df_2016_08_15","df_2016_05_16",
     "df_2016_02_16","df_2015_11_16",
     "df_2015_08_14","df_2015_05_15","df_2015_02_17","df_2014_11_14",
     "df_2014_08_14","df_2014_05_15",
     "df_2014_02_14","df_2013_11_14"]

for i,e in enumerate(df_df2):
    df = pd.DataFrame(e)
    df.to_csv("C:\\Users\\Public\\Downloads\\"+df_names[i]+".csv")



