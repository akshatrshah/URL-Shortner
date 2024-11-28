# URL-Shortner 🔗

[![GitHub Release](https://img.shields.io/github/v/release/fantastic-riddles/URL-Shortner?style=plastic)](https://github.com/fantastic-riddles/URL-Shortner/releases)
[![GitHub Tag](https://img.shields.io/github/v/tag/fantastic-riddles/URL-Shortner?style=plastic)](https://github.com/fantastic-riddles/URL-Shortner/releases)
[![GitHub forks](https://img.shields.io/github/forks/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/network)
[![GitHub stars](https://img.shields.io/github/stars/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/graphs/contributors)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/blob/develop/LICENSE)

<!-- [![Build](https://github.com/fantastic-riddles/URL-Shortner/actions/workflows/unit_test.yaml/badge.svg)](https://github.com/fantastic-riddles/URL-Shortner/actions/workflows/unit_test.yaml) -->

<!-- [![Linting Check](https://github.com/fantastic-riddles/URL-Shortner/actions/workflows/linting_workflow.yml/badge.svg)](https://github.com/fantastic-riddles/URL-Shortner/actions/workflows/linting_workflow.yml) -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14026734.svg)](https://doi.org/10.5281/zenodo.14026734)

[![GitHub issues](https://img.shields.io/github/issues/fantastic-riddles/URL-Shortner)](https://github.com/fantastic-riddles/URL-Shortner/issues)
[![codecov](https://codecov.io/gh/fantastic-riddles/URL-Shortner/graph/badge.svg?token=5Q5FTFG82W)](https://codecov.io/gh/fantastic-riddles/URL-Shortner)

[![Documentation Badge](https://img.shields.io/badge/API_Documentation-pdoc-blue.svg)](https://lemon-desert-093c6c80f.2.azurestaticapps.net/)
[![Documentation Badge](https://img.shields.io/badge/APP_Documentation-compodoc-blue.svg)](https://victorious-sky-08a81ed0f.2.azurestaticapps.net/)

---
# Txtly URL-Shortener  
---

**Welcome to Txtly URL-Shortener by Group 21!**  

Inspired by the groundwork laid by Group 5, we’ve taken the core functionality of a URL shortener and enhanced it with powerful new features to provide a seamless and user-friendly experience. Txtly is designed to make URL management simple, customizable, and insightful.  

---
## About the Project  
---

Managing URLs can be a hassle, especially when they are long, complex, or need frequent updates. Txtly solves this by offering a feature-rich platform that lets you create short, memorable links that are easy to share and customize. Whether you need to personalize URLs, track their performance, or handle multiple links at once, Txtly provides the tools to do it all in one place.  

With Txtly, you can create branded links that align with your identity, update the destination of a URL without changing the link, and monitor link performance with our robust analytics dashboard. For users managing large volumes of links, our bulk upload feature allows for efficient handling of multiple URLs at once. All of this is backed by secure, user-specific account management, ensuring that only you can modify your links.  

Txtly isn’t just a URL shortener—it’s a comprehensive link management solution tailored for modern needs. Whether you’re a business professional, content creator, or casual user, Txtly empowers you to take full control of your URLs.  



https://github.com/user-attachments/assets/851e115f-19e7-43c7-9f98-48b024901422

---
🚀 Key Features
---

🔗 Customizable Short URLs
Stand out with custom URL stubs! Now, you can create branded, memorable links that align perfectly with your identity and boost user engagement.

📊 Comprehensive URL Analytics
Get insights on link performance! URL-Shortner’s analytics track clicks and other metrics to help you understand your audience and fine-tune your campaigns.

📋 Bulk URL Upload
Manage large volumes of URLs with ease using our bulk upload feature. Simply upload a CSV file or comma-separated list of URLs and let URL-Shortner do the rest!

🔒 Secure & Reliable URL Management
We prioritize your data’s security. With encrypted management for all URLs, your links are safe and fully manageable at any time. Delete, update, or redirect URLs as needed.

## ✨ Key Enhancements in Txtly URL-Shortener  

Building on the solid foundation laid by Group 5, we’ve integrated advanced features and improvements to elevate the URL-shortening experience:  

### 🔗 Customizable Short URLs  
- Empower your links with custom stubs for branding and better recognition.  
- Tailor URLs to reflect your identity and enhance user engagement.  

### 📊 Advanced URL Analytics  
- Gain detailed insights into link performance.  
- Track metrics such as click counts and user behavior, and export data for deeper analysis.  

### 📋 Bulk URL Management  
- Save time with our bulk upload feature!  
- Easily upload multiple URLs using a CSV file or comma-separated list and manage them from a centralized dashboard.  

### 🔒 Secure and Account-Linked URL Ownership  
- Protect your URLs with user-specific accounts.  
- Only logged-in users can edit, update, or delete their created links, ensuring security and ownership.  

### 🖌️ Revamped UI/UX  
- Navigate with ease using our sleek and intuitive interface, designed for seamless usability.  

### ♻️ Dynamic URL Updates  
- Keep your short URLs relevant by updating their destinations without changing the link.  
- Ensure a consistent and reliable user experience.  

These enhancements aim to make Txtly the go-to solution for modern, flexible, and secure URL management!


---
### Install
---

1. Go to url_shortner_server
2. do pip install -r requirements.txt
3. do python manage.py runserver
4. go to http://127.0.0.1:8000/

You can then go ahead and sign up by giving basic details. We do not ask for credit cards, or any other PII as your data is precious!

![signup](https://github.com/user-attachments/assets/36cc4825-5486-40d1-a80a-c86dc6540b5f)

Enter the long version of the URL you want to generate a short version and click **Generate**. You also have the capability to create a custom URL for your application. We have included standards and protection to avoid SQL Injection attacks.
![Screenshot (47)](https://github.com/user-attachments/assets/a1d9c42f-17bb-4f06-ae6c-20f7b43fd168)

You will be redirected to a page listing all the URLs you have made and you can see which URL you made earlier
![Screenshot (50)](https://github.com/user-attachments/assets/205d2d78-d7a0-44fd-884e-ba8ea78729e1)

You can also delete individual or all the URLs from the listing page. 
![delete URLs](https://github.com/user-attachments/assets/d954481f-67c6-4e69-ac34-2e5ad3888829)

We have also added a new feature! You can analyze how much your short URLs are being used for better analysis and tracking. Additionally, you can also export the statistics of the clicks for all the URLs in a CSV file.
![Screenshot (49)](https://github.com/user-attachments/assets/7cb1d42c-9458-4a93-a856-43f66cd3d768)


You no longer need to remember the special code that our beloved previous contributors had! Since you have an account you 
can always manage your URLs!

---

## We love our contributors ❤️❤️

Make a [pull request](https://github.com/fantastic-riddles/URL-Shortner/compare) to help contribute.

We reference our UI from Zenblog.

This project is built upon the earlier project - [previous version](https://github.com/AkashSarda3/URL-Shortner)
