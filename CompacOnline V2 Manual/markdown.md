
![image](Compac_front_page.png)

<font size ="7">

# CompacOnline V2 <BR>User Manual

<font size ="3">

Updated 16 September, 2026 

![image](CompacOnlineV2_image.png)


# Conditions of Use

- Please read this manual completely before working on, or making adjustments to, the CompacOnline website.

- Along with any warnings, instructions, and procedures in this manual, you should also observe any other common sense procedures that
are generally applicable to websites of this type.

- Compac Industries Limited accepts no liability for loss of profits, loss of products, and loss of time, resulting from failure to follow any warnings, instructions, and procedures in this manual, or any other common sense procedures generally applicable to software of this type, whether incurred by the user or their employees, the installer, the commissioner, a service technician, or any third party.

- Unless otherwise noted, references to brand names, product names, or trademarks constitute the intellectual property of the owner
thereof.

- Every effort has been made to ensure the accuracy of this document. However, it may contain technical inaccuracies or typographical
errors. Compac Industries Limited assumes no responsibility for and disclaims all liability of such inaccuracies, errors, or omissions in this publication.

- Compac Industries Limited reserves the right to change the specifications of its products or the information in this manual without necessarily notifying its users.


**Manufactured by:** <BR>
52 Walls Road, Penrose, Auckland 1061, New Zealand <BR>
P.O. Box 12-417, Penrose, Auckland 1641, New Zealand <BR>
Phone: + 64 9 579 2094 <BR>
Fax: + 64 9 579 0635 <BR>
www.compac.co.nz <BR> 
Copyright ©2015 Compac Industries Limited, All Rights Reserved

<BR>

## Table of Contents

[**1.0 Overview**](#10-overview)

[**2.0 Registration**](#20-registration)

[**3.0 Logging on**](#30-logging-on)

[**4.0 Home Page**](#40-home-page)

[**5.0 Sites Page**](#50-sites-page)

[5.1 Site Details](#51-site-details)

[5.2 Terminals](#52-terminals) 

[5.3 Pumps & Hoses](#53-pumps--hoses)

[5.4 Tanks](#54-tanks)

[5.5 Price Sign](#55-price-sign)

[5.6 Forecourt Controllers](#56-forecourt-controllers)

[5.7 Receipt Templates](#57-receipt-templates)




[**6.0 Transaction Page**](#60-transactions-page)

[**7.0 Products Page**](#70-products-page)

[**8.0 Price Schedule Page**](#80-card-management)

[**9.0 Card Management**](#90-card-management)

[9.1 Create Card](#91-create-card)

[9.2 Bulk Card Upload](#92-bulk-card-upload)

[**10.0 User Management**](#100-user-management)

[10.1 Permission Groups](#101-permission-groups)

[10.2 Users](#102-users)

[**11.0 Monitor Page**](#110-monitor-page)

[11.1 Events](#111-events)

[11.2 Activity Logs](#112-activity-logs)

[11.3 Alerts](#112-activity-logs)

[**12.0 Operator IDs**](#120-operator-ids)

[12.1 Adding Operator ID](#121-adding-operator-id)

[12.2 Bulk Operations](#122-bulk-operations)

[12.3 Adding Operator ID/Code prompt](#123-adding-operator-idcode-prompt)

[12.4 Viewing Transactions with Operator ID/Code](#124-viewing-transactions-with-operator-idcode)

[**13.0 Appendix**](#130-appendix)

[13.1 Declined PIN OnlineAuth Response Codes](#131-declined-pin-onlineauth-response-codes)

# 1.0 Overview
This document provides a high-level overview of CompacOnline V2 and is intended to assist users in navigating the portal.<BR>

Access to CompacOnline V2 requires valid login credentials. The availability of features described in this document may vary depending on the access level assigned by Compac and your Administrator. For further information, please contact your Compac representative.

<BR>

# 2.0 Registration
Users who are added to CompacOnline will receive an invitation email to set up their account. Follow the link in the email to complete the registration process.

<BR>

# 3.0 Logging on
After completing registration, access CompacOnline by visiting https://portal.compaconline.com/ and log in with your credentials.

![image](11.1.1_V2_login.png)

Contact your Compac Representative if SSO(Single Sign On) is required to be set up to access CompacOnline Portal.<BR>
<BR>

# 4.0 Home Page
Once logged in, you will be presented with the Home page. Options are found on the left-hand side of the page.

![image](11.1.2_V2_home_page.png)

- Home – This is reserved for future Dashboard development.

- Sites – displays all Sites listed under the current Organisation

- Transactions – displays all transactions processed through this Organisation

- Products – displays all Products available to be used under the current Organisation

- Price Schedule – displays all Price Schedules available under the current Organisation

- Card Management

   - BIN Ranges – displays all BIN Ranges that can be configured under the current Organisation

   - Cards – displays individual card that can be processed through CompacOnline (Account Cards)

- User Management

   - Users – displays all current users that have access to the Organisation and the permission group the user is allocated to. You will not see the permission groups users are assigned to, if they have higher permissions than you.

   - Permission Groups – displays the permission groups created and individual permissions enabled for the user. 
You can only see permission groups that have the same or less permissions than you.

- Monitor

   - Events – displays all events/notification triggered from a site of the current Organisation

   - Activity Logs – displays all activity and configuration changes made by users within the Organisation

- Alerts

   - Alert History – displays all alert history

   - Alert Rules – displays a list of all alerts created

   - User Groups – displays a list of User Groups created for Alerts

- Compac Pay

   - Organisation – this enables Mobile App function for the organisation

   - Sites – this contains Windcave Mobile merchant details for each site

<BR>

 # 5.0 Sites Page

Sites created under the Organisation is listed on this page. To view or edit site specific information and configuration, select the site required.
Note: Editing the site config will trigger a config/systems download to the device.

![image](11.1.3_V2_Sites_sites_page.png)

Click on the status button ![image](11.1.4_V2_Sites_status_icon.png) of a site will display the high-level status of the Terminal, Pumps, Tanks and Forecourt Controller.

![image](11.1.5_V2_Sites_sample_site.png)

Under Sites, the following options are available:

![image](11.1.6_V2_Sites_side_bar_menu.png)

<font size ="1">

# 5.1 Site Details

<font size ="3">

This page lists the site details: Site Name, Currency, Address, Tax Rate and Tax Identifier.

![image](11.1.7_V2_Sites_create_site.png)

<BR>

<font size ="1">

# 5.2 Terminals 

<font size ="3">

Displays a list of terminals connected to site

![image](11.1.8_V2_Sites_terminals_1.png)

<BR>

Selecting the terminal will open the configuration page. Selecting the Show button will show more information of the status of the terminal.

![image](11.1.9_V2_Sites_terminals_2.png)

<BR>

Selecting the Windcave status will show the status of each Windcave hardware connected to the unit.

![image](11.1.10_V2_Sites_windcave_status.png)

<BR>

Selecting the 3 dots on the side of each terminal will bring up the Operations menu related to that specific terminal. You may see different options based on the permissions you are assigned with.

![image](11.1.11_V2_Sites_operations.png)

<BR>

Under “Operations”, you may see more options based on your permission levels

![image](11.1.12_V2_Sites_ops_options.png)

<BR>

<font size ="1">

# 5.3 Pumps & Hoses

<font size ="3">

Displays all pumps and hoses configured for this site

![image](11.1.13_V2_Sites_pumps_hoses.png)

<BR>

Pump configuration can be viewed by selecting each pump number.

![image](11.1.14_V2_Sites_pump_details_1.png)

![image](11.1.15_V2_Sites_pump_details_2.png)

<BR>

<font size ="1">

# 5.4 Tanks

<font size ="3">

Displays the Tank/s configured for site

![image](11.1.16_V2_Sites_tanks.png)

Each tank listed is linked to a Product configured for the Organisation. Tank details can be viewed by selecting each tank. Details include *Tank Number, Product, Capacity and Gauge.*

<BR>

<font size ="1">

# 5.5 Price Sign

<font size ="3">

Displays the Price Sign configured for the site

![image](11.1.17_V2_Sites_price_sign.png)

Price Sign details can be viewed by selecting the Price Sign

<BR>

![imge](11.1.18_V2_Sites_price_sign_details.png)

<BR>

<font size ="1">

# 5.6 Forecourt Controllers

<font size ="3">

Displays the forecourt controller that your Compac OPT is connected to.

![image](11.1.19_V2_Sites_forecourt_control.png)

<BR>

<font size ="1">

# 5.7 Receipt Templates

<font size ="3">

Displays the receipt template of each BIN Range

![image](11.1.20_V2_Sites_receipt_template.png)

<BR>

![image](11.1.21_V2_Sites_sample_receipt.png)

Each receipt template corresponds to a BIN Range that is available under the Organisation.<BR>

The following features can be added on receipts:

   - Headers and Footers – configured for site name and addresses, can also be customised

   - Cents Per Unit – enabling this will print the unit price in cents

   - Eftpos and/or Credit Card disclaimer – standard authorisation disclaimer can be added for bank card transactions

<BR>
<BR>

# 6.0 Transactions Page

This page will display all transactions happened under the current Organisation. This will include the transactions processed using Mobile App. App transactions can be identified with a different reference number. E.G.: CP2339.

![image](11.2.1_V2_Transactions_all_transactions.png)

<BR>

- Authorisation and Completion on a transaction can be viewed individually by selecting the corresponding transaction.

![image](11.2.2_V2_Transactions_auth_complete.png)

Selecting the View Receipt will display the printed receipt of the transaction.<BR> 

**Example of Using Filters to narrow down specific transactions**<BR>
Suppose you want to the check all the transactions taken by card 7885360087654321 during this week on site ‘Site5’.

<BR>

- Select the Organisation **Compac Testing** which ‘Site5’ belongs to.

![image](11.2.3_V2_Transactions_select_org.png)

- On the Sidebar, select **Transactions**

![image](11.2.4_V2_Transactions_sidebar.png)

<BR>

- Select ![image](11.2.5_V2_Transactions_filter_icon.png) on the top right of the transaction page to set the filter.<BR>
In the filter, select the correct site name, Date Range and input the card number then click on ‘Apply’.

![image](11.2.6_V2_Transactions_trans_filter.png)

- Now all the transactions you want to check are listed as following screen shot.

![image](11.2.7_V2_Transactions_list.png)

Transactions can be exported from CompacOnline. To export transactions, select ![image](11.2.8_V2_Transactions_export_icon.png) from the top right corner of the page.

There are currently 3 type of exports available.<BR>
- Transaction export is only available in CSV format.<BR>
- Transaction Totals Card Scheme and Transaction Totals Product can be exported in CSV or pdf format.<BR>
- Transaction export has columns selection whereas the other two reports don't.<BR>
- Transaction export also has more filter options than the other two reports.

![image](11.2.9_V2_Transactions_export.png)

Enter and configure the report as required using the following:
-    **Name:** Give your exported transaction file a name

![image](11.2.10_V2_Transactions_report_name.png)

   - **Filters:** Use this option to filter and narrow down the criteria of the transactions.<BR>

Select ![image](11.2.11_V2_Transactions_edit_icon.png)

   - **Sites:** Select a site, or leave blank for all sites (muklti site filter is not supported)

   - **Type:** Select a Transaction Type or leave blank to select all 

   - **Date Range:** Select the date range from the list or leave blank to capture all transactions
      - For *Custom* date, a specific date and time is required

   - **Date Range Type:** Select either *Transaction Time* or *Transaction Upload Time*

      - *Transaction Time:* Only transactions that occurred in the specified date range will be included in the report

      - *Transaction Upload Time:* Only transactions that were uploaded in the specified date range will be included in report. This option is useful for ensuring no transactions are missed when there is a delay in uploading them

- **State:** Select a transaction state or leave blank to select all (multi selection of transaction state not supported at this stage)

- **Reference:** Enter the reference number or leave blank

- **Acquirer:** Select an Acquirer or leave blank to select all Acquirers

- **BIN Range:** Select a BIN Range or leave blank to select all BINs

- **Card Type:** Select a Card Type or leave blank to select all

- **PAN:** Enter PAN or leave to select all

- **Card Tags:** Select a Card Tag and specify the value or leave blank to select all

Select **Apply** to apply the filters.<BR>

**NOTE:** Select **Reset** to reset the filter values and select *Apply* to save, if you don't want the browser to save this filter option for next time use.

![image](11.2.12_V2_Transactions_filters.png)

- **Columns:** Here you can add the columns required on the report. To change the order of columns, simply drag and drop them.<BR>
    The leftmost column will be displayed as the first column in the generated report file.<BR>
    Click on the "setup" icon for Date Time Site Local Column to change the time format

![image](11.2.13_V2_Transactions_columns13.png)

To add columns, select ![image](11.2.14_V2_Transactions_add_icon.png) Select the missing columns and select Add

![image](11.2.15_V2_Transactions_add_column.png)

Select **Export** to start exporting the transactions.
<BR>
<BR>

# 7.0 Products Page

This page will display all current products that have been added to the Organisation

![image](11.3.1_V2_Products_current_products.png)

To view the details of each product, select the corresponding product. The product details includes *Unit of Measure* and *Product Code*.

<BR>
<BR>

# 8.0 Price Schedule Page

This page contains the price schedule of each product.<BR>
Price schedules can be applied to one or multiple sites within the Organisation.

Each price schedule can be applied to a single or multiple sites within the Organisation, a site can only have one price schedule linked to it.

![image](11.4.1_V2_Price_schedule.png)

Each price schedule can be applied to a single or multiple sites within the Organisation, a site can only have one price schedule linked to it.

![image](11.4.2_V2_Price_schedule_details.png)

<BR>
<BR>

# 9.0 Card Management

- **BIN Ranges** - This page displays the current card bin range that the Organisation can process.

![image](11.5.1_V2_Cards_bin_ranges.png)

Specific routing and processing rules e.g. Offline acceptance, auth limits and prompts can be configured here.<BR>
Please contact Compac Industries to arrange this.

- **Cards** - This page displays individual cards that can be processed through CompacOnline (Account Cards).<BR>
Cards that are processed through an acquirer e.g. Windcave or WEX can not be added.

![image](11.5.2_V2_Cards_cards.png)

Each card can be configured to a site, restrict product and/or have a set pin. <BR>

Account cards can be added individually using *Create New* button or through Bulk upload function to CompacOnline.

   - Create New – Each card can be configured to a specific site, multiple sites or all sites under the Organization. Card can be configured to be restricted to products, to an expiry date, to a PIN. If PIN needs to be reset by user at terminal, this can be configured. Card related details can be entered under Card “Tags”.

<BR>

<font size ="1">

# 9.1 Create Card <BR>

<font size ="3">

To create or add a Card, the user must have sufficient permissions enabled.<BR>

**Adding a Card in CompacOnline V2**
1.	Log in to CompacOnline portal
2.	From the sidebar, select Card Management and select Cards from the drop down list
3.	Under Cards, select **Create New** button

![image](11.5.3_V2_Cards_create_card.png)

4.	 Enter the required details:<BR>

- **BIN Range** - select the BIN Range this card will belong to<BR>
- **PAN** - Once the BIN Range is selected, enter the remainder of the card number<BR>
- **Sites** - select the sites this card will be accepted<BR>
- **Allowed Products** - select the products that this card is linked to applicable BIN Range<BR>
- **Expiry Date** - set the expiry date of the card<BR>
- **PIN Configuration** - select Add PIN to enable PIN for this card<BR>

![image](11.5.4_V2_Cards_pin.png)

- PIN field - Enter desired PIN for the card. If the PIN field is left empty, The *Reset On Next Use* must be enabled<BR>

- Reset On Next Use - this option will reset the current PIN of the card for the cardholder to enter a new PIN. If PIN already set, have to enter original PIN before setting new PIN. Unless, when editing a card, the pin already exists and is not changed in the same action as reset on next use is selected, the user will be able to set the new pin without knowing the previous pin<BR>

**Note**: In V2, there is no limit on how many times an incorrect PIN is used. The transaction will always decline with Incorrect PIN if an incorrect pin is used.<BR>

•	**Enabled** - Option to enable the card<BR>

5.	Select **Save** button to save

<font size ="1">

<BR> 

# 9.2 Bulk Card Upload <BR>

<font size ="3">

![image](11.5.5_V2_Cards_side_menu.png)

On the right hand side click Bulk

![image](11.5.6_V2_Cards_select_bulk.png)

On the right hand side click Start New

![image](11.5.7_V2_Cards_start_new_bulk.png)

Click on the Import Cards Template CSV.

![image](11.5.8_V2_Cards_new_operation.png)

Fill out the required fields for all cards you want to import.

![image](11.5.9_V2_Cards_fill_in_fields.png)

Open a new Excel sheet. Click on "Data" then select "Get Data From Text/CSV"

![image](11.5.10_V2_Cards_data_from_csv.png)

Select the updated card file and Click on "Transform Data".

![image](11.5.11_V2_Cards_transform_data.png)

Change the format of the Pan column to "text" and replace the current data in that column.

![image](11.5.12_V2_Cards_format_pan.png)

Close and Load the file. Save it as CSV.

![image](11.5.13_V2_Cards_save_as_csv.png)

Upload the modified csv file

![image](11.5.14_V2_Cards_new_operation.png)

Click on Start and then view progress. Once all cards are uploaded, it will display under the Completed Operations.<BR>
Click on down-arrow to view details.

![image](11.5.15_V2_Cards_completed_ops.png)

<BR>

# 10.0 User Management 

<font size ="1">

# 10.1 Permission Groups

<font size ="3">

Permission Group defines whether this group of users have access to specific functions.<BR>
You can set up different permission groups based on the different operation requirements for your users. For example.<BR>
Your service and maintenance team may need to have access to the status of the site, pumps and tanks.<BR>
Your pricing team may need to only have access to the site and pump prices, not others.<BR>
Your fuel scheduling team or company may only need to have access to your tank data.

Click on Create New to generate new permission group.

![image](11.6.1_V2_Users_create_permission.png)

There are large number of refined permissions available in this list.<BR>
There is an option to upload from a file, if ticking box one by one is too time consuming.

<font size ="1">

# 10.2 Users 

<font size ="3">

This page displays all local *Users* created for the *Site*

![image](11.6.2_V2_Users_search.png)

To create a new user, select Create User and enter all requried details

![image](11.6.3_V2_Users_create_user.png)

**Mobile number is only required if this use11.6.4_V2_users.pngr needs to receive Txt Alert. Otherwise leave it blank.<BR>

Permission Group needs to be created before user is invited, as user needs to be assigned to an appropriate permission group.<BR>

Click on *Save* once all required fields are filled out. New user will receive an invitation email with a link to set up their portal password.

![image](11.6.4_V2_Users_users.png)

Inviting a *Guest* user, select the drop down option

![image](11.6.5_V2_Users_create_guest.png)

![image](11.6.6_V2_Users_invite_guest.png)

This function will enable users that already has access to other sites in the Organisation be added to the new site as a guest user.

<BR>

# 11.0 Monitor Page

<font size ="1">

# 11.1 Events

<font size ="3">

All events and notifications triggered from a site will be available on this page e.g. Terminal Configuration changes, <BR>
card swipes and Online/Offline states.

![image](11.7.1_V2_Monitor_events.png)

![image](11.7.2_V2_Monitor_events_log.png)

Use the *Search* field or the filter to find specific events.
When using the filters, the *Clear* option has to be selected to reset the filters

<font size ="1">

# 11.2 Activity Logs

<font size ="3">

Activities relating to an organisation or a site will be listed on this page

![image](11.7.3_V2_Monitor_activity_logs.png)

<font size ="1">

# 11.3 Alerts

<font size ="3">

Selecting this page displays all alert history triggered for an organisation or site/s.

![image](11.7.4_V2_Monitor_alert_history.png)

To set up an alert, a user group must be created before an *Alert Rule* can be configured.<BR>
Select *User Groups* and *Create New*.

![image](11.7.5_V2_Monitor_user_groups.png)

![image](11.7.6_V2_Monitor_create_user_group.png)

Enter the *Name* and add *Users* to the user group and select *Save*

Now to add a specific alert, select "Alert Rules" and select "Create New".

![image](11.7.7_V2_Monitor_alert_rules.png)

![image](11.7.8_V2_Monitor_create_alert_rule.png)

Add the required details e.g. Site; Triggers and the notification method and select Save.<BR>
Once an alert rule is triggered, a notification will be sent through email or sms.

<BR>

# 12.0 Operator IDs

<BR>

<font size ="1">

# 12.1 Adding Operator ID

<font size ="3">

•	Under *Card Management*, select *Operators*

![image](11.8.1_V2_Operator_ID-1.png)

•	Select *Create New*

![image](11.8.2_V2_Operator_ID_create_new-1.png)

•	Under *Create Operator page*, enter in the required details below:

- **Name**: Enter the Operator Name

- **Code**: Enter the Operator Code (Please note, all units having a Windcave SKP pinpad, only numeric values are accepted).

- **Sites**: Select the site/s that this operator code applies to

- **Enabled**: Select this to enable the operator code

Select Save to save the changes.

<BR>

<font size ="1">

# 12.2 Bulk Operations

<font size ="3"> 

This function is to import/delete and export Operator IDs

•	Under *Operators*, select **Bulk** and select **Start New**

![image](11.8.3_V2_Operator_bulk_new-1.png)

•	**Bulk Import**<BR>

o	To import, select **Import** and upload the csv file.<BR>

o	Select *Start* to begin the upload<BR>

o	Select *Confirm* on the pop up message<BR>

o	Select *View Progress* to view status of the upload<BR>

![image](11.8.4_V2_Operator_bulk_import-1.png)

o	Check Completed Operations once the file has been processed

![image](11.8.5_V2_Operator_bulk_complete-1.png)

o	Select More for a detailed view on the status of each operator id.

•	**Bulk Delete**<BR>

o	To delete, select **Delete** and upload the csv file. 

o	Select *Start* to begin the upload

o	Select *Confirm* on the pop up message

o	Select *View Progress* to view status of the upload

![image](11.8.6_V2_Operator_bulk_delete-1.png)

o	Check Completed Operations once the file has been processed

![image](11.8.7_V2_Operator_bulk-delecte_check-1.png)

o	Select *More* for a detailed view on the status of each operator id.

• **Export**

o	To export all operator Ids that have been added previously, select **Export**.<BR>

o	Select *Start* to begin the export

![image](11.8.8_V2_Operator_export-1.png)

o	Once completed, select *Download* to view the file. 
 
*Import and Delete* templates can be downloaded from the Operations page.

<BR>

<font size ="1">

# 12.3 Adding Operator ID/Code prompt<BR>

<font size ="3">

•	To add the Operator ID/Code prompt, Under *Card Management*, select **BIN Ranges**

![image](11.8.9_V2_Operator_code_prompt-1.png)

•	Under **BIN Ranges**, select the bin range name where Operator ID/Code is required<BR>

•	Select **Edit**<BR>

•	Select **Card Processing Rules**<BR>

![image](11.8.10_V2_Operator_edit_bin_range-1.png)

•	Select the site/s that the Operator Id/Code applies to.<BR>

If the Operator Id/Code only applies to a single site, rather create a new Processing Rule to prevent the Operator Id/Code prompt from applying to other sites.

![image](11.8.11_V2_Operator_edit_bin_range_2-1.png)

•	Select **Cached Cards** (for Offline card file)<BR>

•	Under **Prompts**, select **Operator Code** (under *Required*  or *Optional*) to be include as a prompt<BR>

•	For Required prompts: Operator Code input is required, can not be by-passed<BR>

For Optional prompts: Operator Code can be by-passed by pressing ENTER during the prompt.<BR>
•	Select Next or Save
 
Once the prompt is added and the updates are downloaded (BIN Range), the prompt will appear when the card is presented/swiped.
 
Some Operator Id/Code prompts will differ depending on the display.<BR>
Below are some examples of display hardware and the Operator ID/Code prompt:<BR>

•	Windcave SKP: **Load Operator ID and ENTER**<BR>

•	Touchscreen display: **Enter Operator Code**<BR>

•	Storm keypad/display (version 0.0.15.0) : **Enter Operator Code**<BR>

•	Dot matrix display: **Enter Operator Code**<BR>

<BR>

<font size ="1">

# 12.4 Viewing Transactions with Operator ID/Code

<font size ="3">

Transactions with Operator Id/Code can be viewed on **Transactions** page.<BR>
Both the authorisation and completion will contain the Operator Id/Code.

![image](11.8.12_V2_Operator_transactions-1.png)

The data is also available on **Transaction Exports.**<BR>

To include in the transaction exports, add in the Operator Id/Code and Name to the export columns.

![image](11.8.13_V2-Operator_transaction_exports-1.png)

Sample export csv file

![image](11.8.14_V2_Operator_sample_export-1.png)

<BR>

# 13.0 Appendix


<font size ="1">

# 13.1 Declined PIN OnlineAuth Response Codes

<font size ="3">















