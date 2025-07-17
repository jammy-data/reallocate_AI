import streamlit as st

def render(kpis):
    kpi_names = [f"KPI {k['id']}: {k['name']}" for k in kpis]
    selected = st.selectbox("Select a KPI", kpi_names)
    
    for kpi in kpis:
        label = f"KPI {kpi['id']}: {kpi['name']}"
        if selected == label:
            st.write(kpi["description"])
            st.line_chart(data=None)  # Replace with real KPI plot
