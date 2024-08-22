
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url] 



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">End-to-End Business Analytics: Building a Data Warehouse and Dynamic Dashboard Solution</h3>

  <p align="center">
    The project includes ETL process, Datawarehouse design, Pull data from a data warehouse to BI platformo & design an interactive and insightful dashboards for business users
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#folders">Folders structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    <li>
        <a href="data-pipeline-diagram"> Data Pipeline Diagram</a>
    <li>
        <a href="dashboards"> Dashboards</a>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

This project leverages a real-world Brazilian e-commerce dataset provided by **O'list** to analyze and visualize sales performance metrics. The dataset, comprising over 100,000 orders from 2016 to 2018, offers insights into overall sales & orders performance.

**Data Processing and Analysis**

To prepare the data for analysis, I performed the following steps:

1. Consolidation: Combined the 9 CSV files into a unified dataset.
2. Normalization: Standardized data formats and cleaned inconsistencies to ensure data quality.
3. Data Warehousing: Populated a Snowflake data warehouse with a predesigned schema for efficient querying and analysis.

**Visualization and Insights**

Using Power BI, I developed interactive dashboards that showcase key sales/orders metrics including:

- Sales Performance: Monthly Transactions, Revenue, Average Order Value & Freight Value Per Order.
- Delivery Performance: Total Late Deliveries, On-time Delivery Rate, Average Days of Delivery and Average NPS. 

These visualizations provide valuable insights for business stakeholders to make data-driven decisions and identify opportunities for growth.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![MySQL][MySQL]][MySQL-url]
* [![Vue][Vue.js]][Vue-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Folder Structure 

In the repo, there are 3 folders:
<ol> 
<li> Olist: Dataset source - 9 csv files.
<li> Scripts: Contains 4 files, 3 .sql files and 1 .py file
<ul> 
    <li> OLTP_tables_create: Online Transaction Processing Tables.
    <li> DWH_tables_create: Define Dimension and Fact tables.
    <li> views_create: Define views in order to efficiently read performance if concurrent readingn occurs. <em>(However, I will not use these views to pull from data from PowerBI)</em> 
    <li> transform_load_scripts: the script to join between tables and populate the Dim/Fact Tables. This file will be read by the file load_script.py 
</ul>
<li> diagrams: diagrams of OLTP and DWH in database.
</ol>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Prerequisites

## Data Pipeline Diagram









<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/abi-vu/
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[MySQL]: https://shields.io/badge/MySQL-lightgrey?logo=mysql&style=plastic&logoColor=white&labelColor=blue
[MySQL-url]: https://www.mysql.com/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
