import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Calculus Project", layout="wide")
st.title("Lead Levels Trend Analysis (1990-2021)")

file = st.file_uploader("Upload your data (CSV)", type=["csv"])


if file is not None:
    
    bll = pd.read_csv(file)
    
    #print(bll.groupby(["year", "sex", "location", "age_group"])["mean"].mean())
    #print("-----------------")
    print(bll.groupby(["year", "sex", "location", "age_group"])["mean"].mean().reset_index())
    
    grouped = bll.groupby(["year", "sex", "location", "age_group"])["mean"].mean().reset_index()

    st.subheader("Abstract")
    st.write("""This study examines blood lead levels across different countries and age groups analyzing trends in exposure over time. 
    The data provides insights into demographic and regional variations highlighting patterns in lead accumulation and potential public health implications.
    """)

    def Lreg(grouped, x_data, y_data):
        x = grouped[x_data]
        y = grouped[y_data]
        n = len(grouped)

        sum_x = x.sum()
        sum_y = y.sum()
        sum_x2 = (x ** 2).sum()
        sum_xy = (x * y).sum()
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

        x_bar = sum_x/n
        y_bar=sum_y/n
        b= y_bar-(m*x_bar)
        
        M = "{:.3f}".format(m)
        B = "{:.3f}".format(b)

        st.subheader(f"y= {M}x + {B}")
        return " "    
    
    location = st.selectbox("Select Location",grouped["location"].unique())
    age_group = st.selectbox("Select Age Group (years)",grouped["age_group"].unique())
    sex = st.selectbox("Select Sex",grouped["sex"].unique())

    filtered = grouped[(grouped["location"] == location) &(grouped["age_group"] == age_group) &(grouped["sex"] == sex)]
    
    all = grouped=bll.groupby(["year"])["mean"].mean().reset_index()

    st.markdown("##### The mean is measure in micro-grams of lead per deciliter of blood. The graph illustrates the rate of change of quanity of lead since the 1990's")
   
    st.line_chart( filtered.set_index("year")["mean"])
    st.write("Current Data View")
    st.dataframe(grouped)

    st.header("Mathematical Modeling:")
    st.write("""I used a linear regression model because when I initally viewed the data through a scatter plot
             I assumed a more varied but essentlly downward trend, but I didn't know
             how steep and straight the data would be. A linear model is appropriate for this
             case scenario because of the almost constant rate of change
             the data shows. I created a function within the python program which determined the Bete 0 (y intercept)
             and beta 1 (slope coefficient) for the graph above.
              The functioned I calcualted was... """)
    st.markdown(Lreg(grouped, "year", "mean"))

    st.header("Integration Application:")
    st.write("""The average lead content for the graphs above are depended upon the countries they are from so
    for the intregration applications I will be using the graph below
    because it is the average lead content from every country per year.
    The integrated outcome will result in the total conent of lead
    between the chosen domains.\n
    The linear regression model is f(x) = −0.285x + 580.26
    ∴ ∫f(x)dx = ∫(−0.285x + 580.26) dx ⇒ −0.285 · (x² / 2) + 580.26x ⇒ −0.1425x² + 580.26x + c \n
    ∫f(x)dx = −0.1425x² + 580.26x + c
    For x∈[1990,2010] ⇒ (-.285*(2010)^2)/2+580.26(2010)= 589,616.68 & (-.285*(1990)^2)/2+580.26(1990)= 589,431.164
    ∴ 589,616.68 - 589,431.16 = ∫f(x)dx = 185.522 \n
    ∫f(x)dx = −0.1425x² + 580.26x + c
    For x∈[2015,2021] ⇒ (-.285*(2021)^2)/2+580.26(2021)= 589,670.05 & (-.285*(2015)^2)/2+580.26(2015)= 589,645.22
    ∴ 589,670.05 - 589,645.22 = ∫f(x)dx = 24.823 \n
    ∫f(x)dx = −0.1425x² + 580.26x + c
    For x∈[1990,2021] ⇒ (-.285*(2021)^2)/2+580.26(2021)= 589,670.05 & (-.285*(1990)^2)/2+580.26(1990)= 589,431.16
    ∴ 589,670.05 - 589,431.16 = ∫f(x)dx = 238.882
    185.522µg, 24.823µg, 238.882µg """)
    
    st.line_chart( all.set_index("year")["mean"])
    

    st.header("\n" +"Analysis:")
    st.markdown("""The graph represents the rate at which average blood lead levels change over time
    while the integration of the regression model represents the total change in lead
    exposure over a given interval. Using the linear regression model
    f(x)=−0.285x+580.26, the definite integral quantifies the net amount of lead change
    between selected years. The results show a decrease of approximately 185.522 µg
    of lead between 1990 and 2010, compared to a much smaller decrease of 24.823 µg
    between 2015 and 2021. Over the full interval from 1990 to 2021 the total change is
    238.882 µg. This significant reduction in earlier years followed by a smaller change
    in later years suggests that lead exposure decreased rapidly at first and then began
    to level off. This trend supports the conclusion that public health efforts were most
    impactful earlier (1990s) because it was when we stop the usage of lead for gasoline
    """)
    

    st.subheader("Predicitons:")
    st.markdown("""The linear regression model obtained from the data is
    y=−0.285x+580.26 Substituting x=2025 into the model yields a predicted average blood lead
    concentration of approximately 2.138 µg/dL for adults in the year 2025.
    When this estimate is compared with available empirical data the predicted value is accurate
    suggesting that the regression model provides a reasonable approximation of short term trends.
    Nevertheless, because the model assumes a constant rate of decrease its predictive accuracy is limited for long term
    projections as blood lead levels are expected to approach a lower bound rather than
    decrease indefinitely.
    """)

    st.subheader("Limitations: ")
    st.markdown("""An unfortunate flaw of the linear regression model is that it assumes a constant
    rate of decrease in lead levels for all future predictions. In reality, this pattern is
    unlikely to continue indefinitely, as the data suggests the trend will eventually
    flatten and approach a limiting value. This behavior is not accounted for in a
    linear model. However, the regression can still provide reasonable estimates for
    predictions that are not too far into the future.
    """)

    st.subheader("Impact:")
    st.markdown("""This data allows policymakers and public health organizations to evaluate how well
    current efforts to reduce lead exposure are working and to identify areas where
    additional action may be needed. Also the ability of being able to observe the rate 
    for other countries can prove extremely benificial in determing which country remain
    at dangerous levels whilst who has achieved stable levels. With the addition of agr groups
    we can ensure the safety of children by informing us if current methods are working.
    """)

    st.subheader("Next Steps")
    st.markdown("""The orginal study also provides data for how lead has affected bone structure/integrity
    and IQ shifts due to lead posining meaning there is still so much that can be learn by visualizing this data.
    The objective should be to use more appropriate regression models for these new datasets,
    so that we can achieve greater accuracy for future predictions. Using the predictions from my
    models can explain if our current methologies for treating this global issue
    are effective.""")

    st.markdown("##### References:")
    st.write(""" - [Global Burden Disease study](https://ghdx.healthdata.org/record/ihme-data/gbd-2021-lead-exposure-estimates-1990-2021)
- [Childhood Lead Poisoning Prevention](https://www.cdc.gov/lead-prevention/php/news-features/updates-blood-lead-reference-value.html)
- [Biomonitoring - Lead](https://www.epa.gov/americaschildrenenvironment/biomonitoring-lead)   
 - [Streamlit](https://docs.streamlit.io/get-started/installation)
             """)
else:
    st.info("Please upload a CSV file to generate the trend analysis.")
