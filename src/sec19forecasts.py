
"""
Section definitions for ProfileMeister
Contains descriptions of all profile sections
"""

sections = [



    {
        "number": 19,
        "title": "Near Term Prospects",
        "specs": "Forecast the Company's financial performance for the current financial year\\n"
                "Include consolidated revenue, EBITDA, operating profit, net income, and relevant margins\\n"
                "Provide segment-level forecasts for key business segments\\n"
                "Incorporate year-to-date performance and forecasts for remaining quarters\\n"
                "Analyze key performance drivers, market conditions, and company-specific factors\\n"
                "Explain the rationale for expected performance, referencing historical trends and current developments\\n"
                "Compare forecasts to historical performance trends and management guidance if available\\n"
                "All forecasts should reflect the most likely scenario based on available information\\n"
                "All data points must reference the specific point in time or time period they relate to\\n"
                "Always underpin observations with numbers, facts, data, or comparisons\\n"
                "Include precise footnotes with exact sources, document references, page numbers, and sections for each data point",
        "schema": {
            "forecast_overview": {
                "description": None,
                "forecast_period": None,
                "basis_of_forecast": None,
                "source_ref": None
            },
            "ytd_performance": {
                "period_covered": None,
                "key_metrics": [],
                "source_ref": None
            },
            "consolidated_forecast": {
                "annual_metrics": [],
                "quarterly_breakdown": {
                    "quarters": [],
                    "metrics": []
                },
                "source_ref": None
            },
            "segment_forecasts": [],
            "forecast_drivers": {
                "market_conditions": [],
                "company_specific_factors": {
                    "positive_factors": [],
                    "negative_factors": []
                },
                "source_ref": None
            },
            "management_guidance_comparison": {
                "guidance_metrics": [],
                "source_ref": None
            },
            "footnotes": []
        },
        "template": {
            "forecast_overview": {
                "description": "Based on year-to-date performance and expected market conditions, the Company is projected to deliver moderate revenue growth with margin improvement in FY 2025. The forecast reflects the ongoing evolution of the business mix toward higher-margin software and service offerings, partially offset by pricing pressure in traditional hardware segments.",
                "forecast_period": "Full Fiscal Year 2025 (January 1, 2025 - December 31, 2025)",
                "basis_of_forecast": "Q1 2025 reported results plus forecasts for Q2-Q4 2025",
                "source_ref": "ref1"
            },
            "ytd_performance": {
                "period_covered": "Q1 2025 (January 1, 2025 - March 31, 2025)",
                "key_metrics": [
                    {
                        "name": "Revenue",
                        "value": 1248.5,
                        "unit": "million USD",
                        "yoy_change": 14.8,
                        "unit": "%",
                        "comparison_to_plan": {
                            "value": 102.5,
                            "unit": "% of Q1 2025 plan",
                            "source_ref": "ref2"
                        },
                        "source_ref": "ref2"
                    },
                    {
                        "name": "EBITDA",
                        "value": 287.2,
                        "unit": "million USD",
                        "yoy_change": 20.2,
                        "unit": "%",
                        "comparison_to_plan": {
                            "value": 105.3,
                            "unit": "% of Q1 2025 plan",
                            "source_ref": "ref2"
                        },
                        "source_ref": "ref2"
                    },
                    {
                        "name": "EBITDA Margin",
                        "value": 23.0,
                        "unit": "%",
                        "yoy_change": 1.0,
                        "unit": "percentage points",
                        "source_ref": "ref2"
                    },
                    {
                        "name": "Operating Profit",
                        "value": 212.3,
                        "unit": "million USD",
                        "yoy_change": 22.5,
                        "unit": "%",
                        "source_ref": "ref2"
                    },
                    {
                        "name": "Operating Margin",
                        "value": 17.0,
                        "unit": "%",
                        "yoy_change": 1.1,
                        "unit": "percentage points",
                        "source_ref": "ref2"
                    },
                    {
                        "name": "Net Income",
                        "value": 152.8,
                        "unit": "million USD",
                        "yoy_change": 24.5,
                        "unit": "%",
                        "source_ref": "ref2"
                    },
                    {
                        "name": "Net Margin",
                        "value": 12.2,
                        "unit": "%",
                        "yoy_change": 0.9,
                        "unit": "percentage points",
                        "source_ref": "ref2"
                    }
                ],
                "source_ref": "ref2"
            },
            "consolidated_forecast": {
                "annual_metrics": [
                    {
                        "name": "Revenue",
                        "fy_2024A": {
                            "value": 4572.3,
                            "unit": "million USD",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 5248.5,
                            "unit": "million USD",
                            "yoy_change": 14.8,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "basis_of_estimate": "Extrapolated from Q1 2025 growth rate with adjustments for seasonal patterns, pricing trends, and capacity expansion timelines",
                        "source_ref": "ref3"
                    },
                    {
                        "name": "EBITDA",
                        "fy_2024A": {
                            "value": 1028.8,
                            "unit": "million USD",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 1218.8,
                            "unit": "million USD",
                            "yoy_change": 18.5,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "basis_of_estimate": "Calculated based on projected segment mix and margin trends, incorporating operational efficiency initiatives and planned investments",
                        "source_ref": "ref3"
                    },
                    {
                        "name": "EBITDA Margin",
                        "fy_2024A": {
                            "value": 22.5,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 23.2,
                            "unit": "%",
                            "yoy_change": 0.7,
                            "unit": "percentage points",
                            "source_ref": "ref3"
                        },
                        "basis_of_estimate": "Improvement driven by increasing share of software and service revenue, offset by hardware margin pressure and growth investments",
                        "source_ref": "ref3"
                    },
                    {
                        "name": "Operating Profit",
                        "fy_2024A": {
                            "value": 777.3,
                            "unit": "million USD",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 920.5,
                            "unit": "million USD",
                            "yoy_change": 18.4,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "basis_of_estimate": "Projected based on EBITDA forecast with estimated depreciation and amortization reflecting recent capital expenditure patterns",
                        "source_ref": "ref3"
                    },
                    {
                        "name": "Operating Margin",
                        "fy_2024A": {
                            "value": 17.0,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 17.5,
                            "unit": "%",
                            "yoy_change": 0.5,
                            "unit": "percentage points",
                            "source_ref": "ref3"
                        },
                        "source_ref": "ref3"
                    },
                    {
                        "name": "Net Income",
                        "fy_2024A": {
                            "value": 576.1,
                            "unit": "million USD",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 683.0,
                            "unit": "million USD",
                            "yoy_change": 18.6,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "basis_of_estimate": "Calculated based on operating profit forecast, current debt levels, effective tax rate of 22.5%, and absence of significant one-time items",
                        "source_ref": "ref3"
                    },
                    {
                        "name": "Net Margin",
                        "fy_2024A": {
                            "value": 12.6,
                            "unit": "%",
                            "source_ref": "ref3"
                        },
                        "fy_2025E": {
                            "value": 13.0,
                            "unit": "%",
                            "yoy_change": 0.4,
                            "unit": "percentage points",
                            "source_ref": "ref3"
                        },
                        "source_ref": "ref3"
                    }
                ],
                "quarterly_breakdown": {
                    "quarters": [
                        {
                            "name": "Q1 2025",
                            "period": "January 1 - March 31, 2025",
                            "status": "Actual (Reported)",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "Q2 2025",
                            "period": "April 1 - June 30, 2025",
                            "status": "Forecast",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "Q3 2025",
                            "period": "July 1 - September 30, 2025",
                            "status": "Forecast",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "Q4 2025",
                            "period": "October 1 - December 31, 2025",
                            "status": "Forecast",
                            "source_ref": "ref4"
                        }
                    ],
                    "metrics": [
                        {
                            "name": "Revenue",
                            "unit": "million USD",
                            "q1_2025A": 1248.5,
                            "q2_2025E": 1285.3,
                            "q3_2025E": 1320.8,
                            "q4_2025E": 1393.9,
                            "fy_2025E": 5248.5,
                            "q1_yoy": 14.8,
                            "q2_yoy": 14.3,
                            "q3_yoy": 15.2,
                            "q4_yoy": 14.8,
                            "fy_yoy": 14.8,
                            "unit": "%",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "EBITDA",
                            "unit": "million USD",
                            "q1_2025A": 287.2,
                            "q2_2025E": 295.6,
                            "q3_2025E": 304.1,
                            "q4_2025E": 331.9,
                            "fy_2025E": 1218.8,
                            "q1_yoy": 20.2,
                            "q2_yoy": 16.8,
                            "q3_yoy": 17.9,
                            "q4_yoy": 19.0,
                            "fy_yoy": 18.5,
                            "unit": "%",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "EBITDA Margin",
                            "unit": "%",
                            "q1_2025A": 23.0,
                            "q2_2025E": 23.0,
                            "q3_2025E": 23.0,
                            "q4_2025E": 23.8,
                            "fy_2025E": 23.2,
                            "source_ref": "ref4"
                        },
                        {
                            "name": "Operating Profit",
                            "unit": "million USD",
                            "q1_2025A": 212.3,
                            "q2_2025E": 220.8,
                            "q3_2025E": 227.4,
                            "q4_2025E": 260.0,
                            "fy_2025E": 920.5,
                            "q1_yoy": 22.5,
                            "q2_yoy": 17.2,
                            "q3_yoy": 16.5,
                            "q4_yoy": 18.2,
                            "fy_yoy": 18.4,
                            "unit": "%",
                            "source_ref": "ref4"
                        },
                        {
                            "name": "Net Income",
                            "unit": "million USD",
                            "q1_2025A": 152.8,
                            "q2_2025E": 160.5,
                            "q3_2025E": 168.2,
                            "q4_2025E": 201.5,
                            "fy_2025E": 683.0,
                            "q1_yoy": 24.5,
                            "q2_yoy": 17.8,
                            "q3_yoy": 16.8,
                            "q4_yoy": 17.2,
                            "fy_yoy": 18.6,
                            "unit": "%",
                            "source_ref": "ref4"
                        }
                    ],
                    "source_ref": "ref4"
                },
                "source_ref": "ref3"
            },
            "segment_forecasts": [
                {
                    "segment": "Industrial Automation",
                    "metrics": [
                        {
                            "name": "Revenue",
                            "fy_2024A": {
                                "value": 2514.8,
                                "unit": "million USD",
                                "percentage_of_total": 55.0,
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 2886.7,
                                "unit": "million USD",
                                "percentage_of_total": 55.0,
                                "yoy_change": 14.8,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "key_growth_drivers": [
                                "Strong demand in discrete manufacturing sector (forecast 8.5% growth in 2025)",
                                "New product launches in Q2 and Q3 2025",
                                "Expansion of Asia-Pacific manufacturing capacity by Q3 2025"
                            ],
                            "growth_constraints": [
                                "Pricing pressure from regional competitors (-2.8% YoY in Q1 2025)",
                                "Supply chain constraints for specialized components"
                            ],
                            "source_ref": "ref5"
                        },
                        {
                            "name": "EBITDA",
                            "fy_2024A": {
                                "value": 578.4,
                                "unit": "million USD",
                                "margin": 23.0,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 678.4,
                                "unit": "million USD",
                                "margin": 23.5,
                                "unit": "%",
                                "yoy_change": 17.3,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "margin_drivers": [
                                "Increased software component in product mix",
                                "Manufacturing efficiency initiatives (+0.8 percentage points impact)",
                                "Partial offset from price pressure (-0.5 percentage points impact)"
                            ],
                            "source_ref": "ref5"
                        }
                    ],
                    "source_ref": "ref5"
                },
                {
                    "segment": "Process Control Systems",
                    "metrics": [
                        {
                            "name": "Revenue",
                            "fy_2024A": {
                                "value": 1280.2,
                                "unit": "million USD",
                                "percentage_of_total": 28.0,
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 1469.6,
                                "unit": "million USD",
                                "percentage_of_total": 28.0,
                                "yoy_change": 14.8,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "key_growth_drivers": [
                                "Increased capital investment in process industries (+7.2% in 2025)",
                                "Energy efficiency regulatory requirements driving upgrades",
                                "Cross-selling to Industrial Automation customers"
                            ],
                            "growth_constraints": [
                                "Project delays in chemical and petrochemical sectors",
                                "Competitive pressure in mid-market segment"
                            ],
                            "source_ref": "ref5"
                        },
                        {
                            "name": "EBITDA",
                            "fy_2024A": {
                                "value": 268.8,
                                "unit": "million USD",
                                "margin": 21.0,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 316.0,
                                "unit": "million USD",
                                "margin": 21.5,
                                "unit": "%",
                                "yoy_change": 17.6,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "margin_drivers": [
                                "Increased service attachment rates (+0.7 percentage points impact)",
                                "Product cost optimization initiatives (+0.3 percentage points)",
                                "Investments in software capabilities (-0.5 percentage points)"
                            ],
                            "source_ref": "ref5"
                        }
                    ],
                    "source_ref": "ref5"
                },
                {
                    "segment": "Service & Support",
                    "metrics": [
                        {
                            "name": "Revenue",
                            "fy_2024A": {
                                "value": 777.3,
                                "unit": "million USD",
                                "percentage_of_total": 17.0,
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 892.2,
                                "unit": "million USD",
                                "percentage_of_total": 17.0,
                                "yoy_change": 14.8,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "key_growth_drivers": [
                                "Expanding installed base (+8.5% YoY)",
                                "Increased service contract attach rates (44% vs. 42% in FY 2024)",
                                "Remote diagnostics subscription launch in Q2 2025"
                            ],
                            "growth_constraints": [
                                "Service technician shortage in high-growth regions",
                                "Delayed expansion of Asia-Pacific service network"
                            ],
                            "source_ref": "ref5"
                        },
                        {
                            "name": "EBITDA",
                            "fy_2024A": {
                                "value": 181.6,
                                "unit": "million USD",
                                "margin": 23.4,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "fy_2025E": {
                                "value": 224.5,
                                "unit": "million USD",
                                "margin": 25.2,
                                "unit": "%",
                                "yoy_change": 23.6,
                                "unit": "%",
                                "source_ref": "ref5"
                            },
                            "margin_drivers": [
                                "Shift toward higher-margin subscription services (+1.2 percentage points)",
                                "Increased remote service capabilities (+0.8 percentage points)",
                                "Investments in service network expansion (-0.2 percentage points)"
                            ],
                            "source_ref": "ref5"
                        }
                    ],
                    "source_ref": "ref5"
                }
            ],
            "forecast_drivers": {
                "market_conditions": [
                    {
                        "factor": "Industrial Capital Expenditure Growth",
                        "description": "Global industrial capex forecast to grow 6.8% in 2025, led by automation and digitalization investments",
                        "impact": "Positive - Supports overall revenue growth across segments",
                        "source_ref": "ref6"
                    },
                    {
                        "factor": "Manufacturing Reshoring Trends",
                        "description": "Ongoing reshoring of manufacturing to North America and Europe, with 15% increase in new facility announcements for 2025",
                        "impact": "Positive - Particularly beneficial for the Company's strong presence in these regions",
                        "source_ref": "ref6"
                    },
                    {
                        "factor": "Energy Efficiency Regulations",
                        "description": "Implementation of stricter energy efficiency standards in major markets by mid-2025",
                        "impact": "Positive - Drives demand for the Company's energy optimization technology",
                        "source_ref": "ref6"
                    },
                    {
                        "factor": "Rising Labor Costs",
                        "description": "Manufacturing labor costs projected to increase 5-7% globally in 2025",
                        "impact": "Positive - Accelerates automation adoption to reduce labor dependency",
                        "source_ref": "ref6"
                    },
                    {
                        "factor": "Competitive Pricing Pressure",
                        "description": "Intensifying price competition in Asia-Pacific region and mid-market segments",
                        "impact": "Negative - Creating margin pressure in hardware product lines",
                        "source_ref": "ref6"
                    }
                ],
                "company_specific_factors": {
                    "positive_factors": [
                        {
                            "factor": "New Product Introductions",
                            "description": "Launch of next-generation automation platform scheduled for Q3 2025",
                            "estimated_impact": "3-4 percentage points of incremental growth in H2 2025",
                            "source_ref": "ref6"
                        },
                        {
                            "factor": "Asia-Pacific Manufacturing Expansion",
                            "description": "Singapore facility expansion expected to reach 65% capacity increase by Q3 2025",
                            "estimated_impact": "2-3 percentage points of incremental growth in regional sales in H2 2025",
                            "source_ref": "ref6"
                        },
                        {
                            "factor": "Software and Services Mix Shift",
                            "description": "Continued shift toward higher-margin software and service revenue",
                            "estimated_impact": "0.7 percentage points of EBITDA margin improvement in FY 2025",
                            "source_ref": "ref6"
                        },
                        {
                            "factor": "Operational Excellence Program",
                            "description": "Company-wide cost optimization initiative targeting 2% reduction in COGS",
                            "estimated_impact": "0.5 percentage points of EBITDA margin improvement in FY 2025",
                            "source_ref": "ref6"
                        }
                    ],
                    "negative_factors": [
                        {
                            "factor": "Software Development Capacity Constraints",
                            "description": "Continued challenges in technical talent acquisition impacting digital product roadmap",
                            "estimated_impact": "1-2 percentage points lower software revenue growth than planned",
                            "source_ref": "ref6"
                        },
                        {
                            "factor": "Service Network Limitations in Emerging Markets",
                            "description": "Service technician shortages and coverage gaps in high-growth regions",
                            "estimated_impact": "3-5 percentage points lower service contract attach rates in emerging markets",
                            "source_ref": "ref6"
                        },
                        {
                            "factor": "Hardware Margin Pressure",
                            "description": "Pricing pressure from regional competitors requiring tactical discounting",
                            "estimated_impact": "0.5 percentage points negative impact on overall gross margin",
                            "source_ref": "ref6"
                        }
                    ]
                },
                "source_ref": "ref6"
            },
            "management_guidance_comparison": {
                "guidance_metrics": [
                    {
                        "metric": "Revenue Growth",
                        "management_guidance": {
                            "value": {
                                "low": 10.5,
                                "high": 14.8,
                                "unit": "%",
                                "source_ref": "ref7"
                            },
                            "date_provided": "February 15, 2024",
                            "source_ref": "ref7"
                        },
                        "current_forecast": {
                            "value": 14.8,
                            "unit": "%",
                            "vs_guidance": "At high end of range",
                            "source_ref": "ref7"
                        },
                        "variance_explanation": "Strong Q1 2025, continued momentum in software and service segments, and successful product launches support high-end achievement",
                        "source_ref": "ref7"
                    },
                    {
                        "metric": "EBITDA Margin",
                        "management_guidance": {
                            "value": {
                                "low": 22.8,
                                "high": 23.5,
                                "unit": "%",
                                "source_ref": "ref7"
                            },
                            "date_provided": "February 15, 2024",
                            "source_ref": "ref7"
                        },
                        "current_forecast": {
                            "value": 23.2,
                            "unit": "%",
                            "vs_guidance": "Within range, slightly above midpoint",
                            "source_ref": "ref7"
                        },
                        "variance_explanation": "Favorable product mix and operational efficiency gains partially offset by competitive pricing pressure and growth investments",
                        "source_ref": "ref7"
                    },
                    {
                        "metric": "Capital Expenditure",
                        "management_guidance": {
                            "value": {
                                "low": 330.0,
                                "high": 350.0,
                                "unit": "million USD",
                                "source_ref": "ref7"
                            },
                            "date_provided": "February 15, 2024",
                            "source_ref": "ref7"
                        },
                        "current_forecast": {
                            "value": 345.0,
                            "unit": "million USD",
                            "vs_guidance": "Within range, toward high end",
                            "source_ref": "ref7"
                        },
                        "variance_explanation": "Accelerated investments in Asia-Pacific manufacturing capacity and digital infrastructure modernization",
                        "source_ref": "ref7"
                    }
                ],
                "source_ref": "ref7"
            },
            "footnotes": [
                {
                    "id": "ref1",
                    "document": "Financial Forecast Summary",
                    "date": "May 2025",
                    "page": "3-5",
                    "section": "FY 2025 Outlook"
                },
                {
                    "id": "ref2",
                    "document": "Q1 2025 Earnings Release",
                    "date": "April 25, 2025",
                    "page": "1-3",
                    "section": "Financial Highlights"
                },
                {
                    "id": "ref3",
                    "document": "Annual Financial Projections",
                    "date": "May 2025",
                    "page": "8-12",
                    "section": "Consolidated Forecast"
                },
                {
                    "id": "ref4",
                    "document": "Quarterly Forecast Model",
                    "date": "May 2025",
                    "page": "4-7",
                    "section": "Quarterly Breakdown"
                },
                {
                    "id": "ref5",
                    "document": "Segment Analysis and Forecast",
                    "date": "May 2025",
                    "page": "10-18",
                    "section": "Business Segment Projections"
                },
                {
                    "id": "ref6",
                    "document": "Market and Company Analysis",
                    "date": "May 2025",
                    "page": "5-15",
                    "section": "Growth Drivers and Constraints"
                },
                {
                    "id": "ref7",
                    "document": "Management Guidance Analysis",
                    "date": "May 2025",
                    "page": "2-4",
                    "section": "Guidance Comparison"
                }
            ]
        }
    }
]