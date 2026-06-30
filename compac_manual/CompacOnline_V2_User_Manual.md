# CompacOnline V2 User Manual

![Compac Logo](images/page01_img01.png)

**Version No:** 1.0.1
**Date:** 29th December 2025

---

## Conditions of Use

**Compac Industries Ltd.**
52 Walls Road. Penrose. Auckland 1061. New Zealand.
PO Box 12 417. Penrose. Auckland 1642. New Zealand.
Tel: +64 9 579 2094 Fax: +64 9 579 0635 info@compac.co.nz
www.compac.co.nz

- Read this manual completely before working on, or making adjustments to, the CompacOnline website.
- Along with any warnings, instructions, and procedures in this manual, you should also observe any other common sense procedures that are generally applicable to websites of this type.
- Compac Industries Limited accepts no liability for loss of profits, loss of products, and loss of time, resulting from failure to follow any warnings, instructions, and procedures in this manual, or any other common sense procedures generally applicable to software of this type, whether incurred by the user or their employees, the installer, the commissioner, a service technician, or any third party.
- Unless otherwise noted, references to brand names, product names, or trademarks constitute the intellectual property of the owner thereof.
- Every effort has been made to ensure the accuracy of this document. However, it may contain technical inaccuracies or typographical errors. Compac Industries Limited assumes no responsibility for and disclaims all liability of such inaccuracies, errors, or omissions in this publication.
- Compac Industries Limited reserves the right to change the specifications of its products or the information in this manual without necessarily notifying its users.

**Manufactured By:**
52 Walls Road, Penrose, Auckland 1061, New Zealand
P.O. Box 12-417, Penrose, Auckland 1641, New Zealand
Phone: + 64 9 579 2094
Fax: + 64 9 579 0635
www.compac.co.nz

Copyright ©2015 Compac Industries Limited, All Rights Reserved

---

## Document Control

### Revision History

| Version | Date       | Author(s)  | Revision Notes                                                                                  |
|---------|------------|------------|-------------------------------------------------------------------------------------------------|
| 1.0.0   | 23/08/2024 | R Comision | New Manual                                                                                      |
| 1.0.1   | 29/12/2025 | W Zheng    | Added Document Control and Contents table. Updated screenshots and Transactions and Cards pages. |

---

## Contents

- [Overview](#overview)
- [Registration](#registration)
- [Logging on](#logging-on)
- [Home Page](#home-page)
- [Sites Page](#sites-page)
- [Transactions Page](#transactions-page)
- [Products Page](#products-page)
- [Price Schedule Page](#price-schedule-page)
- [Card Management](#card-management)
- [User Management](#user-management)
- [Monitor Page](#monitor-page)

---

## Overview

This document provides a high-level overview of CompacOnline V2 and is intended to assist users in navigating the portal.

Access to CompacOnline V2 requires valid login credentials. The availability of features described in this document may vary depending on the access level assigned by Compac and your Administrator. For further information, please contact your Compac representative.

---

## Registration

Users who are added to CompacOnline will receive an invitation email to set up their account. Follow the link in the email to complete the registration process.

---

## Logging on

After completing registration, access CompacOnline by visiting [https://portal.compaconline.com/](https://portal.compaconline.com/) and logging in with your credentials.

![Sign in screen](images/page08_img01.png)

Contact your Compac Representative if SSO (Single Sign On) is required to be set up to access CompacOnline Portal.

---

## Home Page

Once logged in, you will be presented with the Home page. Options are found on the left-hand side of the page.

![Home page dashboard](images/page09_img01.png)

- **Home** – This is reserved for future Dashboard development.
- **Sites** – displays all Sites listed under the current Organisation
- **Transactions** – displays all transactions processed through this Organisation
- **Products** – displays all Products available to be used under the current Organisation
- **Price Schedule** – displays all Price Schedules available under the current Organisation
- **Card Management**
  - **BIN Ranges** – displays all BIN Ranges that can be configured under the current Organisation
  - **Cards** – displays individual card that can be processed through CompacOnline (Account Cards)
- **User Management**
  - **Users** – displays all current users that have access to the Organisation and the permission group the user is allocated to. You will not see the permission groups users are assigned to, if they have higher permissions than you.
  - **Permission Groups** – displays the permission groups created and individual permissions enabled for the user. You can only see permission groups that have the same or less permissions than you.
- **Monitor**
  - **Events** – displays all events/notification triggered from a site of the current Organisation
  - **Activity Logs** – displays all activity and configuration changes made by users within the Organisation
  - **Alerts**
    - **Alert History** – displays all alert history
    - **Alert Rules** – displays a list of all alerts created
    - **User Groups** – displays a list of User Groups created for Alerts
- **Compac Pay**
  - **Organisation** – this enables Mobile App function for the organisation
  - **Sites** – this contains Windcave Mobile merchant details for each site

---

## Sites Page

Sites created under the Organisation is listed on this page. To view or edit site specific information and configuration, select the site required.

> **Note:** Editing the site config will trigger a config/systems download to the device.

![Sites list](images/page11_img01.png)

Click on the status button of a site will display the high-level status of the Terminal, Pumps, Tanks and Forecourt Controller.

![Site status panel](images/page11_img02.png)

Under Sites, the following options are available:

![Sites sub-menu](images/page12_img01.png)

### Site Details

This page lists the site details: *Site Name, Currency, Address, Tax Rate and Tax Identifier*.

![Create Site form](images/page12_img02.png)

### Terminals

Displays a list of terminals connected to site.

![Terminals list](images/page12_img03.png)

Selecting the terminal will open the configuration page. Selecting the *Show* button will show more information of the status of the terminal.

![Terminal status expanded](images/page13_img01.png)

Selecting the Windcave status will show the status of each Windcave hardware connected to the unit.

![Windcave status](images/page13_img02.png)

Selecting the 3 dots on the side of each terminal will bring up the Operations menu related to that specific terminal. You may see different options based on the permissions you are assigned with.

![Terminal options menu](images/page13_img03.png)

Under "Operations", you may see more options based on your permission levels:

![Terminal operations menu](images/page14_img01.png)

### Pumps & Hoses

Displays all pumps and hoses configured for this site.

![Pumps & Hoses list](images/page14_img02.png)

Pump configuration can be viewed by selecting each pump number.

![Pump Details - Basic](images/page15_img01.png)

![Pump Details - Hoses](images/page15_img02.png)

### Tanks

Displays the Tank/s configured for site.

![Tanks list](images/page16_img01.png)

Each tank listed is linked to a Product configured for the Organisation. Tank details can be viewed by selecting each tank. Details include *Tank Number, Product, Capacity and Gauge*.

### Price Sign

Displays the Price Sign configured for the site.

![Price Signs list](images/page16_img02.png)

Price Sign details can be viewed by selecting the Price Sign.

![Price Sign Details](images/page17_img01.png)

### Forecourt Controllers

Displays the forecourt controller that your Compac OPT is connected to.

![Forecourt Controllers](images/page17_img02.png)

### Receipt Templates

Displays the receipt template of each BIN Range.

![Receipt Templates list](images/page17_img03.png)

![Receipt Template editor](images/page18_img01.png)

Each receipt template corresponds to a BIN Range that is available under the Organisation.

The following features can be added on receipts:

- **Headers and Footers** – configured for site name and addresses, can also be customised
- **Cents Per Unit** – enabling this will print the unit price in cents
- **Eftpos and/or Credit Card disclaimer** – standard authorisation disclaimer can be added for bank card transactions

---

## Transactions Page

This page will display all transactions happened under the current Organisation. This will include the transactions processed using Mobile App. App transactions can be identified with a different reference number. E.G.: `CP2339`.

![Transactions list](images/page19_img01.png)

- **Authorisation and Completion** on a transaction can be viewed individually by selecting the corresponding transaction.

![Transaction detail expanded](images/page19_img02.png)

Selecting the *View Receipt* will display the printed receipt of the transaction.

### Example of Using Filters to narrow down specific transactions

Suppose you want to check all the transactions taken by card `7885360087654321` during this week on site 'Site5'.

- Select the Organisation **Compac Testing** which 'Site5' belongs to.

![Organisations list](images/page20_img01.png)

- On the Sidebar, select **Transactions**

![Sidebar with Transactions selected](images/page20_img02.png)

- Select **Filters** on the top right of the transaction page to set the filter. In the filter, select the correct site name, Date Range and input the card number then click on 'Apply'.

![Filters panel](images/page20_img03.png)

- Now all the transactions you want to check are listed as following screen shot.

![Filtered transactions](images/page21_img01.png)

Transactions can be exported from CompacOnline. To export transactions, select **Export** from the top right corner of the page.

There are currently 3 types of exports available. Transaction export is only available in CSV format. Transaction Totals Card Scheme and Transaction Totals Product can be exported in CSV or PDF format.

Transaction export has columns selection whereas the other two reports don't. Transaction export also has more filter options than the other two reports.

![Export type selector](images/page21_img02.png)

Enter and configure the report as required using the following:

- **Name**: Give your exported transaction file a name
- **Filters**: Use this option to filter and narrow down the criteria of the transactions. Select **Edit**.
  - **Sites**: Select a site, or leave blank for all sites (multi site filter not supported)
  - **Type**: Select a Transaction Type or leave blank to select all
  - **Date Range**: Select the date range from the list or leave blank to capture all transactions
    - For *Custom* date, specific date/time is required
  - **Date Range Type**: Select either *Transaction Time* or *Transaction Upload Time*
    - *Transaction Time*: Only transactions that occurred in the specified date range will be included in the report
    - *Transaction Upload Time*: Only transactions that were uploaded in the specified date range will be included in report. This option is useful for ensuring no transactions are missed when there is a delay in uploading them
  - **State**: Select a transaction state or leave blank to select all (multi selection of transaction state not supported at this stage)
  - **Reference**: Enter the reference number or leave blank
  - **Acquirer**: Select an Acquirer or leave blank to select all Acquirers
  - **BIN Range**: Select a BIN Range or leave blank to select all BINs
  - **Card Type**: Select a Card Type or leave blank to select all
  - **PAN**: Enter PAN or leave to select all
  - **Card Tags**: Select a Card Tag and specify the value or leave blank to select all

Select **Apply** to apply the filters.

> **NOTE**: Select **Reset** to reset the filter values and select *Apply* to save, if you don't want the browser to save this filter option for next time use.

![Export filters](images/page22_img01.png)

- **Columns**: Here you can add the columns required on the report. To change the order of columns, simply drag and drop them. The leftmost column will be displayed as the first column in the generated report file. Click on the "setup" icon for Date Time Site Local Column to change the time format.

![Columns selection](images/page23_img01.png)

To add columns, select **+ Add Columns**. Select the missing columns and select Add.

![Add Columns modal](images/page23_img02.png)

Select **Export** to start exporting the transactions.

---

## Products Page

This page will display all current products that have been added to the Organisation.

![Products list](images/page24_img01.png)

To view the details of each product, select the corresponding product. The product details includes *Unit of Measure* and *Product Code*.

---

## Price Schedule Page

This page contains the price schedule of each product. Price schedules can be applied to one or multiple sites within the Organisation.

![Price Schedules list](images/page25_img01.png)

Each price schedule can be applied to a single or multiple sites within the Organisation, a site can only have one price schedule linked to it.

![Price Schedule Details](images/page25_img02.png)

---

## Card Management

### BIN Ranges

This page displays the current card bin range that the Organisation can process.

![BIN Ranges list](images/page26_img01.png)

Specific routing and processing rules e.g. Offline acceptance, auth limits and prompts can be configured here, please contact Compac Industries to arrange this.

### Cards

This page displays individual cards that can be processed through CompacOnline (Account Cards). Cards that are processed through an acquirer e.g. Windcave or WEX can not be added.

![Cards list](images/page26_img02.png)

Each card can be configured to a site, restrict product and/or have a set pin.

Account cards can be added individually using *Create New* button or through *Bulk* upload function to CompacOnline.

#### Create New

Each card can be configured to a specific site, multiple sites or all sites under the Organization. Card can be configured to be restricted to products, to an expiry date, to a PIN. If PIN needs to be reset by user at terminal, this can be configured. Card related details can be entered under Card "Tags".

![Create Card form](images/page27_img01.png)

#### Bulk Card Upload

1. Click on **Card Management / Cards**

![Card Management sidebar](images/page27_img02.png)

2. On the right hand side click **Bulk**

![Bulk button](images/page27_img03.png)

3. On the right hand side click **Start New**

![Bulk Operations - Start New](images/page28_img01.png)

4. Click on the **Import Cards Template CSV**.

![New Operation - Import](images/page28_img02.png)

5. Fill out the required fields for all cards you want to import.

![Template CSV filled](images/page28_img03.png)

6. Open a new Excel sheet. Click on "Data" then select "Get Data From Text/CSV"

![Excel Get Data from Text/CSV](images/page29_img01.png)

7. Select the updated card file and Click on "Transform Data".

![Power Query - Transform Data](images/page29_img02.png)

8. Change the format of the Pan column to "text" and replace the current data in that column.

![Power Query - Pan column to text](images/page29_img04.png)

9. Close and Load the file. Save it as CSV.

![Saved CSV preview](images/page29_img03.png)

10. Upload the modified csv file.

![Upload modified CSV](images/page30_img01.png)

11. Click on **Start** and then view progress. Once all cards are uploaded, it will display under the Completed Operations. Click on down-arrow to view details.

![Bulk Operations - Completed](images/page31_img01.png)

---

## User Management

### Permission Groups

Permission Group defines whether this group of users have access to specific functions. You can set up different permission groups based on the different operation requirements for your users. For example, your service and maintenance team may need to have access to the status of the site, pumps and tanks. Your pricing team may need to only have access to the site and pump prices, not others. Your fuel scheduling team or company may only need to have access to your tank data.

Click on **Create New** to generate new permission group.

![Create Permission Group form](images/page32_img01.png)

There are large number of refined permissions available in this list. There is an option to upload from a file, if ticking box one by one is too time consuming.

### Users

This page displays all local *Users* created for the *Site*.

![Users search](images/page31_img02.png)

To create a new user, select *Create User* and enter all required details.

![Create User form](images/page32_img02.png)

Mobile number is only required if this user needs to receive Txt Alert. Otherwise leave it blank.

Permission Group needs to be created before user is invited, as user needs to be assigned to an appropriate permission group.

Click on **Save** once all required fields are filled out. New user will receive an invitation email with a link to set up their portal password.

![Users list](images/page33_img02.png)

### Inviting a Guest User

Select the drop down option:

![Create New / Invite Guest dropdown](images/page32_img03.png)

![Invite Guest form](images/page33_img03.png)

This function will enable users that already has access to other sites in the Organisation to be added to the new site as a guest user.

---

## Monitor Page

### Events

All events and notifications triggered from a site will be available on this page e.g. Terminal Configuration changes, card swipes, Online/Offline states.

![Events list](images/page34_img01.png)

Use the *Search* field or the filter to find specific events.

When using the filters, the *Clear* option has to be selected to reset the filters.

### Activity Logs

Activities relating to an organisation or a site will be listed on this page.

![Activity Logs](images/page34_img02.png)

### Alerts

Selecting this page displays all alert history triggered for an organisation or site/s.

![Alert History](images/page34_img03.png)

To set up an alert, a user group must be created before an *Alert Rule* can be configured. Select *User Groups* and *Create New*.

![Create User Group](images/page34_img04.png)

Enter the *Name* and add *Users* to the user group and select *Save*.

Now to add a specific alert, select *Alert Rules* and select *Create New*.

![Alert Rules - Create New](images/page33_img01.png)

![Create Alert Rule form](images/page35_img01.png)

Add the required details e.g. Site; Triggers and the notification method and select Save. Once an alert rule is triggered, a notification will be sent through email or sms.

---

*End of CompacOnline V2 User Manual*
