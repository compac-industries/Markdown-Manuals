

![image](Compac_front_page.png)

<font size ="6">

# CompacOnsite User Manual

<font size ="3">

# Conditions of Use

- Read this manual completely before working on, or making adjustments to CompacOnsite.

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

Version 1.0.1<BR>

Original publication date: 20th February 2019



## Table of Contents

<font size ="5">

[**1.0 Logging In**](#10-logging-in)

<font size ="3">

<font size ="5">

[**2.0 Users**](#20-users)

<font size ="3">

<font size ="5">

[**3.0 Standard User Options**](#30-standard-user-options)

<font size ="3">

[3.1 Transactions](#31-transactions)

[3.2 Tanks](#32-tanks)

[3.4 Cards](#34-cards)

[3.5 User IDs](#35-user-ids)

[3.6 CompacOnSite Logins](#36-compaconsite-logins)

<font size ="5">

[**4.0 Administrator Options**](#40-administrator-options)

<font size ="3">

[4.1 Pricing](#41-pricing)

[4.2 Settings](#42-settings)

<font size ="5">

[**5.0 Technician Options**](#50-technician-options)

<font size ="3">

[5.1 Dispenser Setup](#51-dispenser-setup)

[5.2 Vega Tank Strapping](#52-vega-tank-strapping)

[5.3 Fuel Management System Setup](#53-fuel-management-system-setup)

<BR>

# 1.0 Logging In

CompacOnsite allows remote access of sites 24/7. From CompacOnsite, transactions, tanks,
pricing and more can be managed quickly and easily.

To access CompacOnsite, the device ID is needed. The following should be entered into an
internet browser, replacing device ID with the specific ID of the unit. Refer to Local Setup for
instructions on finding the Device ID.<BR>

https://________.compaconsite.com

The standard passwords are shown below.

**IMPORTANT NOTES:**

**For the security of the site, ensure the passwords are changed once the unit is installed.**

**Access to online data is heavily dependent on the unit being powered on and connected
to the internet.<BR>
Ensure the unit is online in order to have full access to all site data.**

|Username |Password |
|---------|---------|
|user     |c0mpac5KUser |
|admin    |c0mpac5KAdmin |
|tech     |c0mpac5KTech |



After logging in, the CompacOnSite home screen will appear. See Logins for managing logins.

![image](16.1.1_COS_home1.png)

# 2.0 Users

There are three different user options when logging into Compac Onsite; standard, technician
and administrator.<BR>
Each user can access different functionalities.<BR>
Standard users can access all basic functionalities, such as tanks, cards and transactions.<BR>
Admin users can also access these, as well as being able to access the system settings and reboot.<BR>
The technician can access all these options, as well as being able to access set up options which are needed when setting up
the site.

![image](16.1.2_COS_home2.png)

# 3.0 Standard User Options

Users have access to all the following basic functionalities.

# 3.1 Transactions

![image](16.1.3_COS_trans1.png)

**NOTE:** Table columns shown on page can be expanded.

The Transactions page shows the transactions of fuel into the tank.<BR>
The Transactions storage is limited. When Transaction storage is at 100%, the user will have to Export CSV.<BR>
This will store the data locally onto your device while making the transactions data overwritable once more
transactions are recorded.

![image](16.1.4_COS_trans2.png)

**NOTE:** *Select Refresh before adding more transactions.*

Transactions that have not been exported will be viewed in the screen as a default.<BR>
To show exported transactions untick ‘Only load new transactions’.

# 3.2 Tanks
s
The Tanks section indicates product details and volume of fuel in the tank.

![image](16.1.5_COS_tanks.png)

Deliveries indicate when the last transaction of fuel from the tank occurred, including the tank
number and date time.<BR>
The data in this section can be downloaded by pressing Download.<BR>
Select Refresh to view new data. For Technican Only tank settings, see Dispenser Setup.

**NOTE:** *A reboot is required for any changes to be applied. This may take up to 30s.*

# 3.3 Events

Events are notable events that occur with the pumps.

|Event |Description |
|------|------------|
|Pump Snapshot |Accumulative amount of fuel pumped from selected pump, logged at the
midnight instant daily|
|Tank Snapshot |Dip of fuel remaining in the tank, logged at the midnight instant daily
|Controller Power On |The processor turns on
|Time Update |Synchronises time on processor with real online time

Select Download to download the list of events on screen. Select Refresh to load the most
recent events.

![image](16.1.6_COS_events.png)


# 3.4 Cards

In this section, a new card can be created with Create New card. Decide on a card number, PIN
and owner details, then select Submit.

**NOTE:** *For card base management, see Fuel Management System Setup*

**NOTE:** *Ensure Enabled box is ticked to validate card.*

If a mistake has been made, select Edit and edit card details.<BR>
Select the trash can icon if a card is not needed. The maximum Card storage is limited at 200 cards.

![image](16.1.7_COS_events_cards1.png)

![image](16.1.8_COS_events_cards2.png)

# 3.5 User IDs

User IDs consist of any 6 numbers or less.<BR>
Select Edit to Edit User IDs and owner details.<BR>
Tick the enable box to make the User ID valid for use. The trash can icon can be selected to permanently
delete the user.

**NOTE:** *A card can have multiple users.*

Different users will have different User IDs.<BR>
The purpose of this is to know which user has made a transaction, and ensure they are only fuelling when required.

To add a user ID, click Create New User ID.<BR>
To insert large numbers of user, importing a User ID file is recommended. <BR>
Exporting a user ID file exports the data from the website onto your local device.

**NOTE:** *All User ID files created/imported **MUST** be a csv file not an excel file.*

![image](16.1.9_COS_user_ids.png)


# 3.6 CompacOnSite Logins

For the security of the site, the standard passwords should be changed during set up of the unit.<BR>
In case the passwords were not changed during installation, the process is outlined here.<BR>
To change the passwords, go to CompacOnsite Logins, shown on the left options tab.

![image](16.1.10_COS_login_user1.png)

Not all users may be shown depending on the access level of the user. To edit, click Edit.

![image](16.1.11_COS_login_user2.png)

Enter the desired new password, confirm this and press Submit.

# 4.0 Administrator Options

Administrators can access all the above options, as well as being able to reboot the site and
access pricing and settings.

# 4.1 Pricing

From Pricing, the pricing for different products can be viewed and/or changed.

![image](16.1.12_COS_admin-pricing1.png)

The Active Price is the price being used currently for the pumps. To change this, select Set New
Price.

![image](16.1.13_COS_admin-pricing2.png)

Enter the new price for any product and select Change Price.<BR>
This will change the New Price.<BR>
However, the unit will continue to use the Active Price until Use New Prices is selected, under
Price Change.<BR>
Clicking this will change the Active Price and update them to the New Price.

# 4.2 Settings
Settings can be used to set site details. Enter the site details and press submit.

![image](16.1.14_COS_admin-settings.png)

The time zone can also be set. In some cases, timezone will be automatically synced. Enter the
timezone and press submit.

# 4.3 Reboot

You can reboot the site to restart the application.<BR>
Some settings require rebooting to update recent actions.<BR>
The page needs to be refreshed after the Reboot process has been completed.

**NOTE:** *The unit can only be rebooted when no transactions are taking place.*

When someone is refuelling, the C5000 unit cannot be rebooted. The pumps may stop fuelling as
the transaction has been interrupted.


# 5.0 Technician Options

Technician users can access both administrator and standard user options.<BR>
As well as this, they can access site setup options.

# 5.1 Dispenser Setup

Dispenser Setup will bring up a setup menu with four options;

- Products
- Pumps
- Tank Gauging
- Tank Strapping

![image](16.1.15_COS_tech-setup.png)

In the Products tab, the current products can be viewed.

To create a product, Add Product can be selected.<BR>
The product must be named and numbered before it can be saved.<BR>
The following menu will appear.

![image](16.1.16_COS_tech-products.png)

Pressing Submit will add the product.<BR>
When a product is edited the same menu will appear, and the product’s name and number can be changed before resubmitting.
<BR>
To delete a product, select the recycle bin icon in the products table, and click OK on the pop-up.
<BR>
The next tab is the Pumps tab. From this tab, the configuration of the unit (single or dual) can be
chosen, as well as the settings for each pump.

![image](16.1.17_COS_tech-pumps.png)

Depending on the chosen configuration, only one side may be displayed.<BR>

To change the Pump number simply enter the new value and press Update.<BR>

To change the product, meter type or state, select the relevant option from the drop-down
menus and press update.<BR>

The Tank Gauging tab shows which tank gauge is selected for each tank.
<BR>
For the Side B pump, change the State to Enabled for a dual pump.

![image](16.1.18_COS_tech-tanks1.png)

The current settings can be viewed. To edit a row, select Edit.

![image](16.1.19_COS_tech-tanks2.png)

To change a setting, enter the new setting and Submit the new values.<BR>

If a Vega tank gauge is being used, more information is required. The required fields will
automatically appear if a Vega meter is selected.

![image](16.1.20_COS_tech-tanks3.png)

The final tab in Dispenser Setup is the Tank Strapping section.<BR>
This section is only relevant if a Vega meter is fitted. Refer to Vega Tank Strapping for information.

![image](16.1.21_COS_tech-tanks4.png)

To download the tank strapping table, select download current strapping table.<BR>
At the bottom of the page, tables can be uploaded and the table template can be downloaded.<BR>
Use the table ID drop down menu to select the table ID.

# 5.2 Vega Tank Strapping

If a Vega electronic dipstick is being used, a tank strapping table will need to be created to
gauge the amount of liquid in a tank.<BR>
To do this, the tank dipstick will need to be accessed.<BR>
This is a ruler showing volume that is a component of tanks.

To gather values for the tank strapping table:
1. Load a quantity of the product into the tank (eg 50L)
2. Insert a dipstick into the tank so it is perpendicular to the base.
3. Remove the dipstick gently.
4. Use a measuring tape to measure and record the length of wet dipstick onto the table. This
length will correspond to the volume 50L.
5. Load more of the product into the tank (eg +50L=100L)
6. Repeat steps 2 and 4.
7. Repeat steps 5 and 6 for every volume of product. After making a table, reinsert the dipstick
into the tank and then read the volume of fuel in the tank. This is also required on
CompacOnSite.

**NOTE:** *The more readings done on the tank, the more accurate the tank gauging will be.*

![image](16.1.22_COS_tech-tanks5.png)

# 5.3 Fuel Management System Setup

When setting up the unit, the FMS setup tab can be used to set up card records.

Cards can be imported and exported as .csv files.<BR>
This option can be found in this tab.
To add a new card, fill in the required fields and check which prompts are desired.<BR>
Checking Enabled will enable the card. When the card is finished, press Submit.<BR>
Current cards can be viewed in the Card Prefix Table.

|Authentication Mode| Required user action| 
|-------------------|---------------------|
|PIN Pad |Requires users to type in a PIN number/passcode for authentication |
|HID |Requires users to swipe a tag for authentication|
|Card Reader |Requires users to swipe a card into the card reader for authentication|

**NOTE:** *If two of the three boxes are ticked, both authentication modes will be required.*

**NOTE:** *The HID and Card Reader modes cannot both be ticked as they cannot both fit onto a
device's hardware and software.*

![image](16.1.23_COS_tech_fms.png)

To edit a card prefix, click Edit. The following should pop up:

![image](16.1.24_COS_tech_cards.png)

The PAN length is the maximum number of digits the PAN number (Card Number) can be.<BR>
The Access Number is used as an extra step of authentication.<BR>

Here are the boxes that can be ticked/unticked:

|Mode |Action|
|-----|------|
|Hotlist |Checks for BIN Number only, not Card Number. The recommended setting is disabled|
|User ID |Asks for the User ID as an additional step of authentication for the specific user|

|Prompts |Required used action|
|--------|--------------------|
|Expiry Check (only when Card Reader Auth Mode is enabled) |Checks for the expiry month and
year of a card, declines the card if expired |
|Preset |Prompts the user to enter the amount of fuel they want dispensed|
|Odometer |Prompts the user to enter their odometer reading |

