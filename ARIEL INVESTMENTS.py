import pandas as pd
#ARIEL INVESTMENTS
df_2018_08_10 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675318000125/xslForm13F_X01/Form13FTableExport.xml")
df_2018_05_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675318000110/xslForm13F_X01/Form13FTableExport3312018.xml")
df_2018_02_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675318000102/xslForm13F_X01/Form13FTable12312017.xml")
df_2017_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675317000169/xslForm13F_X01/Form13FTableExport.xml")
df_2017_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675317000155/xslForm13F_X01/Form13FTableExport.xml")
df_2017_05_11 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675317000136/xslForm13F_X01/Form13FTableExport.xml")
df_2017_02_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675317000120/xslForm13F_X01/Form13FTableExport.xml")
df_2016_11_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675316000353/xslForm13F_X01/Form13FTableExport.xml")
df_2016_08_15 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675316000331/xslForm13F_X01/Form13FTableExport.xml")
df_2016_05_13 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675316000315/xslForm13F_X01/form13f-tableexport.xml")
df_2016_02_12 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675316000273/xslForm13F_X01/form13ftableexport.xml")
df_2015_11_13 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675315000169/xslForm13F_X01/Form13FTableExport.xml")
df_2015_08_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675315000158/xslForm13F_X01/Form13FTableExport.xml")
df_2015_05_14 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675315000142/xslForm13F_X01/Form13FTableExport.xml")
df_2015_02_13 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675315000069/xslForm13F_X01/Form13FTableExport.xml")
df_2014_11_12 = pd.read_html("https://www.sec.gov/Archives/edgar/data/936753/000093675314000150/xslForm13F_X01/Form13FTableExport.xml")

df_df = [df_2018_08_10,df_2018_05_14,df_2018_02_14,df_2017_11_14,df_2017_08_14,df_2017_05_11,
         df_2017_02_14,df_2016_11_14,df_2016_08_15,df_2016_05_13,df_2016_02_12,df_2015_11_13,
         df_2015_08_14,df_2015_05_14,df_2015_02_13,df_2014_11_12]

df_names = ["df_2018_08_10","df_2018_05_14","df_2018_02_14","df_2017_11_14","df_2017_08_14","df_2017_05_11",
         "df_2017_02_14","df_2016_11_14","df_2016_08_15","df_2016_05_13","df_2016_02_12","df_2015_11_13",
         "df_2015_08_14","df_2015_05_14","df_2015_02_13","df_2014_11_12"]


df_df2 =[]
for i in df_df:
    df_df2.append(i[-1].iloc[2:,:])

title = ["Name of issuer","Title of class","CUSIP","Value (x$1000)","SHR/PRN AMT","SH/PRN",
         "PUT/CALL","Investment Descretion","Other Managers","Voting Sole","Authority Share","NONE"]

for i in df_df2:    
    i.iloc[[0],:] = title
    
for i in df_df2:
    i = pd.DataFrame(i)

for i,e in enumerate(df_df2):
    df = pd.DataFrame(e)
    df.to_csv("C:\\Users\\Public\\Downloads\\"+df_names[i]+".csv")