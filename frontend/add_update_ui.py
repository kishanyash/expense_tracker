import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

API_URL = "http://localhost:8000"

# add_update_ui.py
import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"

def add_update_tab():
    st.header("➕ Add / Update Expense")

    # Inputs
    expense_date = st.date_input("Expense Date", value=date.today())
    amount = st.number_input("Amount", min_value=0.0)
    category = st.text_input("Category")
    notes = st.text_area("Notes")

    # Save button
    if st.button("Save Expense"):
        payload = [{
            "amount": amount,
            "category": category,
            "notes": notes
        }]
        try:
            response = requests.post(f"{API_URL}/expenses/{expense_date}", json=payload)
            if response.status_code == 200:
                st.success("✅ Expense saved successfully!")
            else:
                st.error(f"❌ Failed to save expense: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")


            # Prepare data
            data = {
                "Category": list(analytics_data.keys()),
                "Total": [analytics_data[category]["total"] for category in analytics_data],
                "Percentage": [analytics_data[category]["percentage"] for category in analytics_data]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage", ascending=False)
            
            total_expenses = df['Total'].sum()
            days_analyzed = (end_date - start_date).days + 1
            daily_average = total_expenses / days_analyzed if days_analyzed > 0 else 0

            # Summary metrics
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("### 📈 Summary Metrics")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    "💰 Total Expenses",
                    f"${total_expenses:.2f}",
                    help="Total amount spent in the selected period"
                )
            
            with col2:
                st.metric(
                    "📂 Categories",
                    len(analytics_data),
                    help="Number of expense categories used"
                )
            
            with col3:
                st.metric(
                    "📅 Days Analyzed",
                    days_analyzed,
                    help="Number of days in the selected period"
                )
            
            with col4:
                st.metric(
                    "📊 Daily Average",
                    f"${daily_average:.2f}",
                    help="Average daily spending"
                )
            
            st.markdown('</div>', unsafe_allow_html=True)

            # Charts section
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
                st.markdown("### 📊 Expense Distribution")
                
                # Create pie chart
                fig_pie = px.pie(
                    df_sorted, 
                    values='Total', 
                    names='Category',
                    title="Spending by Category",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                fig_pie.update_layout(
                    showlegend=True,
                    height=400,
                    font=dict(size=12)
                )
                st.plotly_chart(fig_pie, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
                st.markdown("### 📈 Category Breakdown")
                
                # Create horizontal bar chart
                fig_bar = px.bar(
                    df_sorted, 
                    x='Total', 
                    y='Category',
                    orientation='h',
                    title="Spending Amount by Category",
                    color='Total',
                    color_continuous_scale='Viridis'
                )
                fig_bar.update_layout(
                    height=400,
                    yaxis={'categoryorder': 'total ascending'},
                    font=dict(size=12)
                )
                st.plotly_chart(fig_bar, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Detailed breakdown
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("### 📋 Detailed Breakdown")
            
            # Format the dataframe for display
            display_df = df_sorted.copy()
            display_df["Total"] = display_df["Total"].apply(lambda x: f"${x:.2f}")
            display_df["Percentage"] = display_df["Percentage"].apply(lambda x: f"{x:.1f}%")
            
            # Add category icons
            category_icons = {
                "Rent": "🏠",
                "Food": "🍽️", 
                "Shopping": "🛍️",
                "Entertainment": "🎬",
                "Other": "📝"
            }
            
            display_df["Category"] = display_df["Category"].apply(
                lambda x: f"{category_icons.get(x, '📝')} {x}"
            )
            
            # Display as a styled table
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Category": st.column_config.TextColumn("Category", width="medium"),
                    "Total": st.column_config.TextColumn("Amount", width="small"),
                    "Percentage": st.column_config.TextColumn("Percentage", width="small")
                }
            )
            st.markdown('</div>', unsafe_allow_html=True)

            # Insights section
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("### 💡 Insights")
            
            # Generate insights
            top_category = df_sorted.iloc[0]
            lowest_category = df_sorted.iloc[-1]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"""
                **🔝 Highest Spending Category**
                
                {category_icons.get(top_category['Category'], '📝')} **{top_category['Category']}** accounts for 
                **{top_category['Percentage']:.1f}%** of your total expenses 
                (${top_category['Total']:.2f})
                """)
            
            with col2:
                st.info(f"""
                **📉 Lowest Spending Category**
                
                {category_icons.get(lowest_category['Category'], '📝')} **{lowest_category['Category']}** accounts for 
                **{lowest_category['Percentage']:.1f}%** of your total expenses 
                (${lowest_category['Total']:.2f})
                """)
            
            # Budget recommendations
            if total_expenses > 0:
                st.markdown("### 💰 Budget Recommendations")
                
                if top_category['Percentage'] > 50:
                    st.warning(f"⚠️ **{top_category['Category']}** represents over 50% of your spending. Consider reviewing this category for potential savings.")
                
                if daily_average > 100:
                    st.warning(f"⚠️ Your daily average spending (${daily_average:.2f}) is quite high. Consider setting a daily budget limit.")
                else:
                    st.success(f"✅ Your daily average spending (${daily_average:.2f}) looks reasonable!")
            
            st.markdown('</div>', unsafe_allow_html=True)

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Network error: {str(e)}")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")