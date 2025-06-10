# Solar Panel Performance Optimization

This competition was hosted on HackerEarth. Unfortunately, I missed the start and end dates of the competition. I thought why not give it a try.

## Problem Statement

As solar energy systems become increasingly popular in sustainable energy infrastructures, maintaining high performance and reducing downtime is essential. Traditional maintenance methods for photovoltaic (PV) systems are often reactive, leading to energy loss and increased costs. The goal of this project is to develop a Machine Learning model that predicts performance degradation and potential failures in solar panels.

### 1. Task

Develop a Machine Learning model that predicts performance degradation and potential failures in solar panels using historical and real-time sensor data, enabling predictive maintenance and optimal energy output.

### 2. Dataset Description

| Column             | Description                                                                                                   |
|:-------------------|:--------------------------------------------------------------------------------------------------------------|
| id                 | Represents the unique identification of the row.                                                              |
| temperature        | Represents ambient air temperature (C), which affects panel output efficiency.                                |
| irradiance         | Represents the amount of solar energy received per unit area (W/m), which directly impacts energy generation. |
| humidity           | Represents moisture content in the air, which may impact panel performance over time.                             |
| panel_age          | Represents the age of the solar panel in years, older panels degrade in performance.                          |
| maintenance_count  | Represents the number of previous maintenance activities recorded.                                            |
| soiling_ratio      | Represents a reduction in efficiency due to dust or debris on the panel surface (0.01.0).                           |
| voltage            | Represents voltage output measured from the panel (V), derived from irradiance.                               |
| current            | Represents current output from panel (A), which varies with irradiance and panel health.                  |
| module_temperature | Represents the temperature of the panel surface, distinct from the ambient temperature                        |
| cloud_coverage     | Represents sky coverage by clouds (percentage), which affects irradiance reaching the panel                   |
| wind_speed         | Represents wind speed in m/s, may aid in the cooling of panels, and affects temperature.                      |
| pressure           | Represents atmospheric pressure at the location of the panel in hPa.                                          |
| string_id          | Represents an identifier for a string/group of panels (for example A1, B2).                                  |
| error_code         | Represents error codes logged from panel diagnostics (for example E00, E01, E02).                            |
| installation_type  | Represents the type of mounting setup - fixed, tracking, or dual-axis.                                        |
| efficiency         | Represents the target variable representing the final energy output efficiency of the panel.                  |

