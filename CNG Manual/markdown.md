
![image](9.1.1_Compac_IRS_frontpage.png)


<font size="5">

# C5000 CNG Dispenser Installation and Service Manual  

updated 29 April 2026
<font size="3">

# Conditions of Use  

Please read this manual completely before working on, or making adjustments to Compac equipment

Compac Industries Limited accepts no liability for personal injury or property damage resulting from working on or adjusting the equipment incorrectly or without authorization.

Along with any warnings, instructions, and procedures in this manual, you should also observe any other common sense procedures that are generally applicable to equipment of this type.

Failure to comply with any warnings, instructions, procedures, or any other common sense procedures may result in injury, equipment damage, property damage, or poor performance of the Compac equipment

The major hazard involved with operating the Compac C4000 processor is electrical shock. This hazard can be avoided if you adhere to the procedures in this manual and exercise all due care.

Compac Industries Limited accepts no liability for direct, indirect, incidental, special, or consequential damages resulting from failure to follow any warnings, instructions, and procedures in this manual, or any other common sense procedures generally applicable to equipment of this type. The foregoing limitation extends to damages to person or property caused by the Compac C4000 processor, or damages resulting from the inability to use the Compac C5K processor, including loss of profits, loss of products, loss of power supply, the cost of arranging an alternative power supply, and loss of time, whether incurred by the user or their employees, the installer, the commissioner, a service technician, or any third party.

Compac Industries Limited reserves the right to change the specifications of its products or the information in this manual without necessarily notifying its users.

Variations in installation and operating conditions may affect the Compac C4000 processor's performance. Compac Industries Limited has no control over each installation's unique operating environment. Hence, Compac Industries Limited makes no representations or warranties concerning the performance of the Compac C4000 processor under the actual operating conditions prevailing at the installation. A technical expert of your choosing should validate all operating parameters for each application.

Compac Industries Limited has made every effort to explain all servicing procedures, warnings, and safety precautions as clearly and completely as possible. However, due to the range of operating environments, it is not possible to anticipate every issue that may arise. This manual is intended to provide general guidance. For specific guidance and technical support, contact your authorised Compac supplier, using the contact details in the Product Identification section.

Only parts supplied by or approved by Compac may be used and no unauthorised modifications to the hardware of software may be made. The use of non-approved parts or modifications will void all warranties and approvals. The use of non-approved parts or modifications may also constitute a safety hazard.

Information in this manual shall not be deemed a warranty, representation, or guarantee. For warranty provisions applicable to the Compac C4000 processor, please refer to the warranty provided by the supplier.

Unless otherwise noted, references to brand names, product names, or trademarks constitute the intellectual property of the owner thereof. Subject to your right to use the Compac C5K processor, Compac does not convey any right, title, or interest in its intellectual property, including and without limitation, its patents, copyrights, and know-how.

Every effort has been made to ensure the accuracy of this document. However, it may contain technical inaccuracies or typographical errors. Compac Industries Limited assumes no responsibility for and disclaims all liability of such inaccuracies, errors, or omissions in this publication.

# Specifications

## Models Covered

> **Note:** Do not use this manual for earlier models. Contact Compac for archived manuals if required.

# Validity

Compac Industries Limited reserves the right to revise or change product specifications at any time. This publication describes the state of the product at the time of publication and may not reflect the product at all times in the past or in the future.

# Manufactured By

The Compac CNG Dispenser is designed and manufactured by Compac Industries Limited

52 Walls Road, Penrose, Auckland 1061, New Zealand

P.O. Box 12-417, Penrose, Auckland 1641, New Zealand

Phone: + 64 9 579 2094

Fax: + 64 9 579 0635

**Email:** [techsupport@compac.co.nz](mailto:techsupport@compac.co.nz)

**Website:** [http://www.compac.co.nz](http://www.compac.co.nz)

Copyright ©2015 Compac Industries Limited, All Rights Reserved

# Document Control

## Document Information

**Manual Title:** C5000 CNG Installation and Service Manual

**Current Revision Author(s):** Trevor Watt

**Original Publication Date:** 22 April 2026

**Authorised By:** Emily Sione

**File Name:** C5000 CNG Installation and Service Manual v.1.0.5




## Table of Contents

<font size ="5">

[**1.0 Safety**](#10-safety)

<font size ="3">

[1.1 System Design](#11-system-design)

[1.2 Mechanical Safety](#12-mechanical-safety)

[1.3 Electrical Safety](#13-electrical-safety)


<font size ="5">

[**2.0 Introduction**](#20-introduction)

<font size ="3">

<font size ="5">

[**3.0 Refuelling Modes**](#30-refuelling-modes)

<font size ="3">

<font size ="5">

[**4.0 Installation**](#40-installation)

<font size ="3">


<font size ="5">

[**5.0 Commissioning - Electrical**](#50-commissioning---electrical)

<font size ="3">


<font size ="5">

[**6.0 Commissioning - Mechanical**](#60-commissioning---mechanical)

<font size ="3">


<font size ="5">

[**7.0 Dispenser set up**](#70-dispenser-set-up)

<font size ="3">

[7.1 Parameter Switch](#71-parameter-switch)

[7.1.1 How to View the Software Version](#711-how-to-view-the-software-version)

[7.1.2 Changing the Pump Number](#712-changing-the-pump-number)

[7.1.3 Unit Price](#713-unit-price)

[7.1.4 Pump settings](#714-pump-settings)

[7.1.5 Minimum Flow Rate](#715-minimum-flow-rate) 

[7.1.6 Maximum Flow Rate](#716-maximum-flow-rate)






<font size ="5">

[**8.0 Operation**](#80-operation)

<font size ="3">


<font size ="5">

[**9.0 Servicing**](#90-servicing)

<font size ="3">

[9.1 Degassing the Dispenser](#91-degassing-the-dispenser)

[9.2 Scheduled Servicing](#92-scheduled-servicing)

[9.3 Checking Dispenser operation](#93-checking-dispenser-operation)

[9.4 Checking that the Solenoid is sealing](#94-checking-that-the-solenoid-is-sealing)

[9.5 Checking the Regulator](#94-checking-that-the-solenoid-is-sealing)

[9.6 Checking the Over Pressure cut off operation](#96-checking-the-over-pressure-cut-off-operation) 

[9.7 Checking for leaks](#97-checking-for-leaks)

[9.7.1 Checking the Refuelling Hose for Leaks](#971-checking-the-refuelling-hose-for-leaks)

[9.8 Checking Isolation Ball Valve operation](#98-checking-isolation-ball-valve-operation)

[9.9 Checking the 3way valve operation](#99-checking-the-3way-valve-operation)  

[9.10 Draining the Filter](#910-draining-the-filter)

[9.10.1 Filter Element Replacement](#9101-filter-element-replacement)

[9.11 Solenoid Valve Seal replacement](#911-solenoid-valve-seal-replacement)

[9.12 Solenoid Coil replacement](#912-solenoid-coil-replacement)

[9.13 Complete Solenoid replacement](#913-complete-solenoid-replacement)

[9.14 Regulator Valve Seal replacement](#914-regulator-valve-seal-replacement)

[9.15 Isolation Valve Seal replacement](#915-isolation-valve-seal-replacement)

[9.16 Bleed Valve Replacement](#916-bleed-valve-replacement)

[9.17 Pressure Relief Valve Replacement](#917-pressure-relief-valve-replacement)

[9.18 KG100 Meter Replacement](#918-kg100-meter-replacement)

[9.19 Refuelling Hose Replacement](#919-refuelling-hose-replacement)

[9.20 Power Supply Fuse Replacement](#920-power-supply-fuse-replacement)

[9.21 Power Supply Replacement](#921-power-supply-replacement)

[9.22 Processor Board Replacement](#922-processor-board-replacement)

[9.23 Temperature Pressure Board Replacement](#923-temperature-pressure-board-replacement) 

[9.24 Dispenser Software Upgrade or Replacement](#924-dispenser-software-upgrade-or-replacement)

<font size ="5">

[**10.0 Dispenser Calibration**](#100-dispenser-calibration)

<font size ="3">

[10.1 Meter Calibration](#101-meter-calibration)

[10.2 Pressure Transducer Calibration](#102-pressure-transducer-calibration) 

[10.3 Ambient Temperature Sensor Calibration](#103-ambient-temperature-sensor-calibration)


# 1.0 Safety

**DANGER PRECAUTIONS**<BR>

You must adhere to the following safety precautions at all times when working on the Compac equipment.<BR>
Failure to observe these safety precautions could result in damage to the dispenser, injury, or death.<BR>
Make sure that you read and understand all safety precautions before operating the Compac equipment<BR>
Failure to take adequate safety precautions could result in explosion, injury and loss of life.

# 1.1 System Design
Ensure the system design does not allow the dispenser inlet pressure to exceed its rating.<BR>
The dispenser does not include any safeties to protect against excessive inlet pressure.<BR>
If necessary, suitable protective devices should be fitted prior to the dispenser inlet.

# 1.2 Mechanical Safety

Observe the following mechanical precautions:<BR>

- Never tighten a fitting under pressure, even if a fitting or joint is leaking. Always depressurise the line first.
- Never disassemble a fitting under pressure. Always depressurise the line first.
- Be very careful when disassembling frozen pipework, as gas pressure may be trapped and suddenly released. Always depressurise the line before using.
- Never reuse any O-ring seals that have been in a high pressure gas atmosphere and then exposed to air. These o-rings swell and cannot be reused. Always make sure you have a new seal kit available to replace the seals before disassembly.
- Make sure that all internal surfaces are cleaned and that sliding surfaces are lightly greased with O-ring lubricant before reassembly. Dust and dirt entering components reduce the life span of the components and can affect operation.
- Ensure the service area is thoroughly cleaned before initiating service on CNG components. Dust and dirt entering the components reduce the life span of the component and affect future operations. 

# 1.3 Electrical Safety

Observe the following electrical precautions:<BR>

- Always turn off the power to the CNG Dispenser before removing the box lid. Never touch wiring or components inside the CNG Dispenser with the power on.
- Never power up the CNG dispenser with the flameproof box lid removed.
- Always turn off the power to the dispenser before upgrading software or replacing components.
- Always take basic anti-static precautions when working on the electronics, i.e., wearing a wristband with an earth strap. 

# 2.0 Introduction

The Compac CNC dispenser is designed to provide safe and reliable dispensing of CNG fuels.<BR>
They are available in either single or dual hose configurations and with different flow rates.<BR> 

Compac CNG dispensers are controlled by a C5000 board which has many programmable features to suit your individual operation.<BR>

This manual contains the information required to operate and maintain your dispenser. Due to ongoing improvements and customised designs, there may be software features that are not available on your particular unit.<BR>

For clarity, this manual will refer to the "Dollars" display. If you do not use dollars please substitute this for your local currency. 

![image](15.2.1_CNG_Laser.png)

# 3.0 Refuelling Modes

# 4.0 Installation

# 5.0 Commissioning - Electrical

This procedure outlines how to perform an electrical operational test before carrying out full mechanical commissioning, making sure that the dispenser is functioning correctly.<BR>
Check for any damage that may have occurred in transit. Check all terminals, plugs, and chips to make sure that they are securely in place.<BR> 

**NOTE:** *Damage to electronics occurs most commonly from vibration and jarring.* 

Before beginning this test, check that no gas pressure has been applied to the dispenser inlets.<BR>
The factory set-up information should be programmed into the dispenser, but all K-factor and Parameter switch settings should be checked and confirmed before commissioning tests are carried out.

To perform an electrical operational test:<BR>

1.	Make sure that the inlet shut-off valves are closed (these are the valves in the inlet lines at the base of the dispenser, but they are not part of the dispenser).

2.	Turn on the power supply to the dispenser. 
The displays and backlighting will illuminate, and the displays read hold.
The dispenser is in a ready state once the hold is finished, and the display shows 0.00.

3.	With the dispenser in a ready state.
Press the Start button. 
The display will show 888888 and the solenoids energise, initiating a fill. On the K factor board check that the output leds T1 T2 and T3 turn on, indicating a signal is being sent to the triacs to open the solenoid valves.
The diagnostic LED (D9) flashes quickly when the start button is pushed or the nozzle removed from the holster to initiate a fill. When the button is released or nozzle returned to the holster it will return to the normal state and flash slowly.

4.	Verify solenoid operation by listening for a click, or by using a screwdriver tip or some other metallic tool to check for a magnetic field present on the solenoid coils.
The solenoids will switch off after 10 seconds. This is a default time-out setting in the software for situations when there is no gas flow registered. 

5.	Press the stop button. The solenoids switch off and the fill ends. 
When you release the stop button, the dispenser resets and returns to a ready state.

# 6.0 Commissioning - Mechanical

At the mechanical commissioning stage, the dispenser should not be pressurised.<BR>

**NOTE:** *If you find any leaks during commissioning, immediately close all the valves and de-gas the dispenser.*<BR>

To perform a mechanical test:
<BR>
1.	Make sure that the inlet shut-off valves are closed. (These are the valves in the inlet lines at the base of the dispenser, but they are not part of the dispenser.)
2.	Check all dispenser fittings, especially the inlet connections, to make sure that they are tight.<BR>

**DANGER:** Always de-gas the lines before tightening any fittings. Never tighten fittings while they are under pressure.<BR>

3.	Check that the outlet supply valve to hose 1 on the side of the dispenser (or hose 2 if you are working on side 2) is closed and the nozzle valve is closed.<BR>

4.	Turn on the dispenser and wait for it to power up.<BR>

The dispenser initially displays **PA:uSE**. When it is ready, **0.00** is displayed.<BR>

5.	Press the START button.<BR>

**NOTE:** *If you are commissioning a dual hose dispenser, press the Start button on either side. This opens the dispenser's solenoids. The dispenser automatically shuts off after approximately one minute if no flow is detected.*<BR>

6.	Slowly open the inlet shut-off valves until the dispenser pressure gauge reads **5 bar**. Close the inlet shut-off valves and listen for leaks. If you hear leakage, shut off the inlets immediately. If the dispenser shuts off during this process, shut off the inlet valves, restart the dispenser, and continue.<BR>

7.	Allow the dispenser to time out on the 1-minute no-flow timer and shut the solenoid valves, or, manually shut it down and close the solenoid valves by pressing the STOP button.<BR>

8.	Press the 5tart button on the dispenser and repeat steps 6 and 7 at **25 bar, 125 bar** and **250 bar**(if applicable).

**NOTE:** *If you are commissioning a dual hose dispenser, only press the Start button for one of the hoses.*<BR>

9.	Press the START button<BR>

10.	Slowly open the outlet isolation valve on the side of the dispenser until the dispenser pressure gauge reads **5 bar**. 
Close the outlet isolation valve and listen for leaks. If you hear leakage, shut the valve immediately.

If the dispenser shuts off during this process, then shut the outlet supply valve, restart the dispenser, and continue.<BR>

11.	Allow the dispenser to time out on the 1-minute no-flow timer and shut the solenoid valves, or, manually shut it down and close the solenoid valves by pressing the STOP button.<BR>

12.	Repeat steps 9 to 11 at **25 bar, 125 bar** and **250 bar**(if applicable).<BR>

Repeat steps 9 to 12 for the second hose on a dual hose dispenser.<BR>

The dispenser and hose(s) are now fully pressurised.<BR>

13.	Use soapy water to check all fittings (including the hose fittings) for leaks.<BR>

**DANGER:** Always de-gas the lines before tightening any fittings. Never tighten fittings while they are under pressure.<BR>

14.	Complete a few fills on a test cylinder, checking for leaks or unusual operation.


# 7.0 Dispenser set up

# 7.1 Parameter Switch

The Parameter switch is located on the K factor board behind the main display and allows you to adjust the unit price, hose number, Pump settings high low cut off and display setting.<BR>

The Parameter switch also enables you to view the Dispenser Software Version and End of Sale Indicators.

![image](15.8.1_CNG_Kfactorboard.png)

Menu Options<BR>

Listed below is the order in which the **Parameter** switch menu options are presented.<BR>
There are different menu options depending on the current setting of the C configuration code.<BR> 
The * indicates that you can achieve the displayed menu option, regardless of what the indicated part is set to.<BR>
You may need to change the C configuration in order to access the parameter code you require.

Setting|Price Display|Litres Display
|------|------|------
Software Version|	P**.**. **      |	P**.**. **
Pump Number|| 	Pna *** or Pnb ***
Pump Settings||		bA **** or bb ****
Low-flow cut off||		LFA***
High-flow cut off||		HFA ***
Heat of compression|| 		hcA**
b Setting||		b****
Slave display||		dS****
Custom display||	dc****
|||dP
|||du
Last Sale|	**. ** |	A ***. * or b ***. *
Electronic Totes|	LA **** or dA ****|L****.**
||Lb **** or dA ****|d****.**


# 7.1.1 How to View the Software Version<BR>

Pressing the parameter switch once will show the software version. 

![image](4.1.1_Parameter_Software_version_PO.png)

The dispenser will then run through a segment test.

# 7.1.2 Changing the Pump Number<BR>

If the parameter switch is continually depressed, the following menu to change the pump number will appear. <BR>
Each side must be numbered between 1-99.

**NOTE:** Entering a pump number 0 will disable the pump.to the pump controller
See Using the Dispenser Menus to edit these settings. Use the procedure for both side A and B.

![image](4.1.2_Parameter_pump_number_PnA.png)

# 7.1.3 Unit Price

The unit price (PA) is used to calculate the total value of the quantity dispensed.<BR>
The unit price can be different on each side of a dual hose dispenser.<BR>
The unit price can be set at the dispenser or set remotely via a POS or controller

![image](4.1.3_Parameter_price_PA.png)

**NOTE:** If the unit price is not set Error 3 will be displayed and the dispenser will not operate.<BR>

To set the unit price:
- Make sure that the dispenser is idle, with the nozzle in its holster.
- Press and release the Parameter switch until the required unit price is displayed (PA).
- Enter in the unit price. 

**NOTE:** Each press of the **Parameter** switch passes you over a digit in a setting, making the digit blink.<BR>
Holding the switch down for more than a second changes whichever digit is currently displayed.<BR>
If you want to pass over a setting without changing any digits, keep pressing and releasing the switch.<BR>

Let the menu time out so that the value and quantity amounts are displayed.

# 7.1.4 Pump settings

The bA setting is where you can set the dispenser in to standalone mode.<BR>
Standalone mode means that the dispenser doesn’t communicate to a controller or POS.<BR>

If the dispenser is in authorisation mode the dispenser will not start even if there is no controller or POS connected.

**Note:** *If the dispenser is communicating to a controller or POS it will not operatate in standalone mode. To put the dispenser in to standalone while still connected to the controller or POS set the **CC** setting to **cc0000** setting*

![image](15.8.2_CNG_bA.png)

# 7.1.5 Minimum Flow Rate  

The minimum flow rate (LFA and LFb) is the low flow cut-off at the end of the fill.<BR> 
LFA is the minimum flow rate of side A of the dispenser.<BR>
LFb is the minimum flow rate of side B of the dispenser.<BR>
These values are adjustable and can be set between 0.5-99 kg⁄min.<BR>

**CAUTION:** Do not set the minimum flow rate so that it is equal to or above the maximum flow rate.<BR>

**To Adjust the Minimum Flow Rate**<BR>

- Make sure that the dispenser is idle, with the nozzle in its holster.
- Press and release the Parameter  switch until the required minimum flow rate is displayed. (LFA or LFb)
- Enter the new minimum flow rate.

**NOTE:** Each press of the Parameter switch passes you over a digit in a setting, making the digit blink.<BR>
Holding the switch down for more than a second changes whichever digit is currently displayed.<BR>
If you want to pass over a setting without changing any digits, keep pressing and releasing the switch.
NOTE: The Compac factory default setting is 1.0 kg⁄min.

Let the menu time out so that the value and quantity amounts are displayed.

![image](4.1.6_Parameter_Low_Flow-Cut_LFA.png)

# 7.1.6 Maximum Flow Rate

The maximum flow rate (HFA and HFb) is the high flow cut-off for when the flow through the dispenser is too high.<BR>

HFA is the maximum flow rate of side A of the dispenser.<BR>
HFb is the maximum flow rate of side B of the dispenser.<BR>

These values are adjustable and can be set between 1-9999 kg⁄min.<BR>

**CAUTION:** Do not set the maximum flow rate so that it is equal to or below the minimum flow rate.

**To Adjust the Maximum Flow Rate**
	
- Make sure that the dispenser is idle, with the nozzle in its holster
- Press and release the Parameter switch until the required maximum flow rate is displayed. (HFA or HFb)
- Enter the new maximum flow rate.

**NOTE:** Each press of the Parameter switch passes you over a digit in a setting, making the digit blink.<BR>
Holding the switch down for more than a second changes whichever digit is currently displayed.<BR>
If you want to pass over a setting without changing any digits, keep pressing and releasing the switch. 

**NOTE:** The Compac factory default setting is 40 kg⁄min for Car Dispensers and 60 kg⁄min for High flow or Bus dispensers.

Let the menu time out so that the value and quantity amounts are displayed.

![image](4.1.7_Parameter_High_Flow_Cut_HFA.png)

# 8.0 Operation

# 9.0 Servicing

# 9.1 Degassing the Dispenser

# 9.2 Scheduled Servicing

<BR>

# 9.3 Checking Dispenser operation

To check that the dispenser is operating correctly:
1.	Fill two gas bottles.
2.	Check that:
-	The bottles fill to the desired pressure.
-	The dispenser fills to the preset value.
-	The displays and gauges are working.

<BR>

# 9.4 Checking that the Solenoid is sealing

-	De-gas the hose by opening the 3 way valve. 
-	When the hose is empty check that the flow has stopped. If the flow does not stop, the seals in the final stage solenoid will need to be replaced.

<BR>

# 9.5 Checking the Regulator

Before you start, make sure you have: 
An 8mm hex key

**NOTE:** When you are undertaking this check, the dispenser must be turned on and pressurised. 
To check the setting and sealing of the regulator:

-	Hang up the nozzle and check that the three-way valve is closed.
-	Press the start button to initiate a fill and open the solenoids.
-	Check that the pressure gauge is at the setpoint reading (typically 200 bar).
-	Check that the pressure gauge reads at a steady state, rather than creeping after a fill. 

If the pressure gauge is not reading the correct setpoint:<BR>

- Insert an 8mm hex key into the top of the regulator body.
- Adjust the pressure up clockwise or down anticlockwise to 200 bar.

If the pressure on the gauge does not remain stable, the regulator valve seal is leaking and will have to be replaced.

![image](15.9.1_CNG_regulator.png)

<BR>

# 9.6 Checking the Over Pressure cut off operation

Checking the Over-Pressure Operation :<BR>

To check the operation of the Overfil Pressure cut off:
-	Access the K-Factor switch on the K-Factor board.
-	Obtain the overfill pressure settings 0pa
-	Set the overfill pressure cut-off point to below the regulator pressure.
-	Set the over pressure time to (deb) 01.0 or 1 second.
-	For example, if the regulator pressure is 220 bar, then set the over-pressure to 100 bar. An exact value is not required; just make sure that the value is significantly lower than the regulator pressure.
-	Start a fill. The dispenser should stop the fill after 1 second.
-	Check the dispenser End of Sale indicator states that the fill has ended because of over-pressure. End of Sale Indicators.
-	Reset the over-pressure cut-off point to its original value.

<BR>

# 9.7 Checking for leaks

Before you start, make sure you have: 
-	Soapy water
To check the dispenser for leaks:

**CAUTION:** Be careful not to spray or drip water into any of the dispenser electronics when checking for leaks.
-	Apply soapy water to all joins in the assemblies and fittings on the inside and outside of the dispenser, including the hose. 

If bubbles form, there is a leak with that assembly or fitting. The fitting may require tightening, or the seals might need to be replaced.

**DANGER:** You must isolate the gas supply and depressurise the dispenser before disassembling any component or adjusting any fitting. Serious injury may result if components are removed while the dispenser is under pressure.

-	Threaded SAE Fittings.
-	Adjustable Threaded SAE Fittings.
-	Compression Fittings.

-	To remedy a leak, refer to the appropriate section, depending on the leak is location.  
-	After checking for leaks, wipe any excess water off the dispenser to prevent corrosion.

# 9.7.1 Checking the Refuelling Hose for Leaks
Before you start, make sure you have:
-	Soapy water

To check the refuelling hose:
-	Visually check the refuelling hose for damage, such as fraying and cuts.
-	Apply soapy water to all valves and connections.

If bubbles form, there is a leak in that assembly or fitting. The fitting may require tightening or the seals might need to be replaced.

**DANGER:** You must isolate the gas supply and depressurise the dispenser before disassembling any component or adjusting any fitting. Serious injury may result if components are removed while the dispenser is under pressure.

Replace the hose if it is damaged or leaking.

<BR>

# 9.8 Checking Isolation Ball Valve operation

Before you start, make sure you have: 
-	Soapy water
To check the operation of the isolation ball valve:
-	Close the isolation valve.
-	Open the dispenser access door.
-	Open the bleed valve on the utility manifold block (where fitted) and bleed the gas from the refuelling hose.
-	Close the bleed valve once the hose is degassed.
-	Start a fill. 

If the pressure gauge starts to move, the isolation ball valve is leaking or passing gas. 
-	Apply soapy water to the valve. 

If bubbles form, there is a leak in the assembly or fitting. The fitting may require tightening, or the seals might need to be replaced.
For servicing refer to Isolation Valve Seal Replacement.

<BR>

# 9.9 Checking the 3way valve operation  

Before you start, make sure you have: 
-	Soapy water
Check the Sealing of the Three-Way Refuelling Valve<BR>

To check the sealing of the three-way refuelling valve, apply soapy water to the valve.<BR>

If bubbles form, there is a leak, in which case you should replace the three-way refuelling valve seals.<BR>

**To check the operation of the three-way refuelling valve:**<BR>

To check the operation of the three-way refuelling valve, do a test fill to check that the valve is filling the vehicle, and venting properly when you disconnect it from the vehicle.<BR>

If bubbles form, there is a leak, in which case you should replace the three-way refuelling valve seals.

<BR>

# 9.10 Draining the Filter

Before you start, make sure you have:
-	A 3/16" hex key
To drain the coalescing filter:
-	De-gas the dispenser.
-	Open the dispenser access doors.
-	Unscrew the drain plug from the bottom of the filter cover.
-	Allow all oil and water to drain from the filter*. 
-	If excessive amounts of oil and water are present, remove and replace the coalescing filters.
-	Screw in the drain plug and repeat steps 1 to 4 for all additional filters.

**NOTE:** Make sure you dispose of any fluids responsibly.

# 9.10.1 Filter Element Replacement
The coalescing filters are designed to trap dirt, moisture, oil, and other debris that may damage the valve seals.
Before you start, make sure you have:
-	A seal kit - Part number FC-FIL-0001
	1 x filter
	1 x filter bowl O-ring seal
-	O-ring lubricant
To remove the coalescing filter:
-	Degas the dispenser.
-	Drain the coalescing filters if they have not been drained already. 
-	Unscrew the filter bowl(s) with a spanner on the 22mm hex nut at the base of the filter bowl.
-	Remove the filter element.
-	Clean all oil and dirt off the components with a clean cloth.
To install the new coalescing filter:
-	Insert the new filter element and lubricated filter bowl O-ring seal. 

**CAUTION:** O-rings that are subjected to natural gas at high pressure swell when exposed to air. Once swollen, they cannot be reused and must be replaced.

![image](15.9.2_CNG_filter.png)

**NOTE:** Always use O-ring lubricant to prevent damage to the O-rings.

-	Screw in the filter bowl(s)
-	Check the dispenser for leaks.

<BR>

# 9.11 Solenoid Valve Seal replacement

These instructions refer to the current Compac S2-350 solenoid valve. The solenoids are available in several types<BR>
Standard and low temperature. Always quote the dispenser serial number when ordering parts and check the model number on the valve body before installation.

Before you start, make sure you have: 
- A seal kit - Part number FC-SK-0001
- 1 x Teflon valve seal
- 1 x solenoid top O-ring seal
- 1 x gas return line O-ring seal<BR>

-	O-ring lubricant
-	Solenoid piston – Part number FC-VLV-PSTN-0001 
-	Solenoid top service kit standard. Part number FC-SVK-0003 (replace valve top if leak detected through stem)
-	Solenoid top service kit - low temperature option (-40 degrees C). Part number FC-SVK-0004 (replace valve top if leak detected through stem).

**CAUTION:** Never remove or service the stem. If it is leaking, it must be replaced using the appropriate top service kit.

**CAUTION:** Cleanliness is essential. When working on the open solenoid assembly, cover the opening with a cloth to prevent dust and dirt from entering.

**CAUTION:** O-rings that are subjected to natural gas swell when exposed to air. Once swollen, they cannot be reused and **must** be replaced.

**CAUTION:** The Nitrile O-rings have a life span of over 10 years from cure date but improper handling of these O-rings before use can shorten their useful life.<BR>
O-rings will deteriorate if exposed to ozone or ultraviolet light so keep in original packaging and away from UV light.<BR>
If unsure about their condition, do not use old O-rings and order new ones. 

**NOTE:** It is not necessary to remove the solenoid body from the dispenser to service the solenoid seals.

To remove the old solenoid valve seals:
-	De-gas the dispenser.
-	Switch off the power supply to the dispenser

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Unscrew the solenoid coil retaining nut and move the coil out of the way.
-	Remove the six cap screws from the solenoid top.

**NOTE:** *Do not remove the angled grub screw from the solenoid top. This is epoxied in place during manufacture and should never be removed.*

-	Remove the solenoid top and remove the old top O-ring seal and gas return O-ring.
-	Remove the solenoid spring.
-	Screw an M6 cap screw into the solenoid piston to withdraw it from the solenoid body.

![image](15.9.3_CNG_piston.png)

-	Taking care not to damage the piston, hold the flat part of the piston with a spanner to prevent rotation, then unscrew the M6 x 12 mm cap screw from the bottom of the piston. This releases the solenoid seal retainer and valve seal.  
-	Discard the old valve seal.
-	Clean all oil and dirt off the components with a clean cloth and check that the bleed hole is not blocked.
-	While the solenoid is apart, inspect the solenoid piston centre seal and piston for wear, scratching or damage. Replace piston if required.

To install new solenoid valve seals:

-	Place the new valve seal and seal retainer on the cap screw.
-	Taking care not to damage the piston, hold the flat part of the piston to prevent rotation, and then screw the M6 cap screw into the bottom of the piston.
-	Insert a new gas return O-ring.
-	Insert the piston back into the solenoid body.
-	Insert the solenoid spring.
-	Replace the solenoid top O-ring seal.
-	Place the solenoid top back on the solenoid body, making sure that the locating dowel is engaged.
-	Screw in and tighten the six cap screws.
-	Replace the solenoid coil.

![image](15.9.4_CNG_solenoid.png)

-	Re-power and re-gas the dispenser then check for leaks and correct operation of the valve

<BR>

# 9.12 Solenoid Coil replacement

Before you start, make sure you have: 
-	Replacement solenoid coil FC-COIL-0005 (Compac S2-350).

**NOTE:** Solenoid coils are not interchangeable between models. Make sure you order the correct one by quoting the dispenser serial number.<BR>
To replace obsolete coils, the entire solenoid will need replacing.

To remove the solenoid coil:
-	De-gas the dispenser.
-	Switch off and isolate the power supply to the dispenser.

DANGER: Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Remove the flameproof box lid to gain access to the C5000 Terminal board. 
-	Disconnect the appropriate solenoid coil wiring from the C5000 Terminal board board.

**CAUTION:** Take basic anti-static precautions by wearing a wristband with an earth strap. 

-	Loosen the gland on the flameproof box that is clamping the solenoid coil lead and pull the lead out of the gland. 

Undo the nut on the top of the solenoid valve that is securing the coil and remove the coil from the top of the valve.

To install the new solenoid coil:
-	To install a new solenoid coil, reverse the procedure above.

**NOTE:** Before replacing the lid on the flameproof box, make sure that the O-ring is not damaged and is seated properly in its groove.<BR>
If the O-ring is damaged and needs replacing, replace it with an O-ring of the same size and specification (176 N70).

<BR>

# 9.13 Complete Solenoid replacement

These instructions refer to the current Compac S2-350 solenoid valve. This replaces all previous solenoids.
Before you start, make sure you have: 
-	Solenoid valve standard 350 bar model (FC-VALVE-0035) or
-	Solenoid valve 350 bar O ring seal option for high oil content gasses (FC-VALVE-0036) or
-	Solenoid valve 350 bar low temperature option (FC-VALVE-0037) 

**NOTE:** Solenoid valves are supplied without coils. If you need the coil it must be ordered as well.<BR>

**CAUTION:** Cleanliness is essential. When working on the open pipes and solenoids, cover the openings with a clean, lint-free cloth to prevent dust and dirt from entering.
To remove the old solenoid valve:
-	De-gas the dispenser.
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Undo the nut and remove the solenoid coil.
-	Undo the gland nuts connecting the solenoid valve to the pipework and manifold and remove valve.

To replace the solenoid valve:
-	Ensuring all surfaces are clean and any sealing plugs are removed from the valve, reconnect the pipework and tighten the gland nuts.
-	Replace the solenoid coil.
-	Repower and re-gas the unit, check for leaks and test for correct operation.

<BR>

# 9.14 Regulator Valve Seal replacement

Before you start, make sure you have: 
- A regulator seal kit - Part Number FC-SK-0002
- 2 x regulator O-ring seals
- 2 x Teflon back-up ring
- 1 x Teflon valve seal
- O-ring lubricant<BR>

To remove the old regulator valve seals:
-	De-gas the dispenser.
-	Open the dispenser access doors.
-	Unscrew the spring tube by placing a 1 ¼" spanner on the machine hex nut at the top of the spring tube.

**NOTE:** Do not unscrew the valve adjustment nut. The spring remains at the set tension. 

-	Unscrew the bottom plug in the regulator body.
-	Using a hex key inserted into the base of the piston to stop the piston from twisting sideways and being damaged, push the piston downwards out the bottom of the regulator body.
-	Hold the piston by the 8mm flat and remove the M6 cap screw from the bottom. 

**NOTE:** The M6 cap screw has a special hole through it. Never substitute it for a normal cap screw.

To install the new regulator valve seals:
-	Install the new valve seal. Make sure that the larger flat side of the seal faces upwards.

![image](15.9.5_CNG_regulator_seal.png)

**NOTE:** *O-rings that are subjected to natural gas at high pressure swell when exposed to air. Once swollen, they cannot be reused and must be replaced.* <BR>

**CAUTION:** The Nitrile O-rings have a life span of over 10 years from cure date but improper handling of these O-rings before use can shorten their useful life.<BR>
O-rings will deteriorate if exposed to ozone or ultraviolet light so keep in original packaging and away from UV light.<BR>
If unsure about their condition, do not use old O-rings and order new ones. 

-	Lever off the two regulator O-rings and two Teflon back-up rings.
-	Install two new regulator O-rings and two new Teflon back-up seals.

The back-up rings go on the outside of the O-rings.<BR>

**NOTE:** Always use O-ring lubricant on the O-rings to increase the service life. 

-	Reassemble the piston.
-	Push the piston back up into the regulator body with a hex key.<BR>

**NOTE:** Keep the piston straight, rotate it clockwise to prevent the new O-ring from catching or ripping. 

-	Screw in the bottom plug.
-	Screw on the spring tube until tight.
Check the setting and sealing of the regulator for correct pressure.

<BR>

# 9.15 Isolation Valve Seal replacement
 
**NOTE:** Please make sure you identify the valve before disassembling it to make sure you have the correct seal kit available. <BR>

This instruction only applies to the Parker make valve

Complete valve is part number FC-Valve-0001

Before you start, obtain the following replacement parts and equipment:
-	FC-SK-0010 Parker Isolation Valve Seal Kit
-	Refer to Spare Parts list for other items that you may need.<BR>

To remove the isolation valve seals: <BR>

**CAUTION:** Take care when disassembling the valve, as a lot of parts look similar.

-	De-pressurise the valve and remove it from the pipework.
-	Remove the handle and panel nut to remove it from the cabinet.
-	Disassemble the valve, as per the drawing below.
-	Undo the packing nut and remove packing washers, packing and stem.
-	Undo the end connectors and remove the seals, seat assembly and ball

Clean all components with a clean dry lint free rag.

**CAUTION:** O-rings that are subjected to Natural Gas at high pressure. Swell when exposed to air. Once swollen they must be replaced.

-	Blow compressed air (100 psi) through all ports to remove any impurities that may damage the seals in operation. 

**CAUTION:** Wear appropriate safety eye wear when using compressed air.

![image](15.9.6_CNG_isovalve.png)

To replace the isolation valve seals:<BR>

**CAUTION:** Take care to keep all parts clean while assembling.

-	Apply a light coating of approved grease to the ball then replace the ball and ball seat sub-assemblies, making sure the slot in the ball is at the top. 
-	Making sure the retainer seal and end connector O ring are in place, screw in the end connectors. Do not tighten yet. 
-	Locate the stem in the ball slot then replace the stem washers, stem packing and packing nut.
-	Open and close the valve a few times to seat the ball valve before tightening the end connectors and packing nut. 
-	Reattach the valve to the cabinet and reconnect the pipework.
-	Reapply gas to the valve and check for leaks.

<BR>

# 9.16 Bleed Valve Replacement
The bleed valve seldom gives problems and is not serviceable.<BR>

For a replacement valve and instructions if required, contact your Compac service agent with your Model and Serial numbers.

<BR>

# 9.17 Pressure Relief Valve Replacement
The pressure relief valve seldom gives problems and is not serviceable. <BR>
For a replacement valve and instructions if required, contact your Compac service agent with your Model and Serial numbers.

<BR>

# 9.18 KG100 Meter Replacement

To remove the meter:
-	Shut off gas supply and degas the meter.
-	Remove the inlet and outlet pipes from the old meter.
-	Unscrew the SAE fittings from the meter inlet and outlet.
-	Take note of the position and orientation of the communications plug then unplug the meter cable from the K-Factor board and cut any cable ties that hold it in place. 
-	Undo the four bolts that hold the meter on the dispenser frame.
-	Remove the old meter.

To replace the meter:
-	Secure the new meter to the dispenser frame using the four bolts.
-	Plug the communications cable into the K-Factor board.
-	Screw the SAE fittings into the meter inlet and outlet.
-	Install the inlet and outlet pipes.
-	Cable tie the communications cable to avoid pulling or damage to it.
-	Load the meter ID into the K-Factor board
-	Pressurise the meter and check for leaks.
-	Calibrate the meter in accordance with the instructions in the dispenser service manual.

![image](15.9.7_CNG_KG100.png)

<BR>

# 9.19 Refuelling Hose Replacement

To remove the refuelling hose:
-	De-gas the dispenser.
-	Undo the JIC hose connection at the dispenser's outlet block.
-	Undo the connection between the hose and the nozzle assembly.<BR>

To install the new refuelling hose:
-	Attach the nozzle assembly to the new hose.
-	Attach the new hose to the dispenser at the outlet block. 
-	Re-gas the dispenser and push the Start button to fill the new hose assembly with gas.
-	Check all hose connections for leaks by applying soapy water mixture and looking for bubbles.

# 9.20 Power Supply Fuse Replacement

**NOTE:** There are three fuses used in the C5000 Flame proof box.<BR>
Before you start, make sure you have the following fuses with these ratings:<BR>
- F1 = 1.6 A<BR>
- F2,F3 = 0.5 A<BR>
- OR Compac fuse kit F-C5PWR-FKE<BR>

Fuse locations are displayed on the C5000 terminal board in the flameproof box.<BR>
**NOTE:** Every new dispenser is supplied with one spare F1, F2 and F3 fuse, located on the inside of the flameproof box lid.

![image](15.9.8_CNG_fuses.png)

To remove the C5000 terminal board fuse(s):
-	Degas the dispenser.
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Remove the flameproof box lid.
-	Remove the blown fuse and discard.

**CAUTION:** Take basic anti-static precautions by wearing a wristband with an earth strap. 
To install the new C5000 terminal board fuse(s):
-	Replace the blown fuse element with a new one of equal type and rating.

**CAUTION:** You must use the correct rating when replacing a fuse. The correct ratings are printed next to each fuse on the printed circuit board. Using the incorrect fuse rating may compromise the intrinsic safety of the dispenser.

-	Replace the flameproof box lid, ensuring that the O-ring in the lid engages in its associated groove. 
-	Turn on the power to the dispenser.

**DANGER:** Do not power up the dispenser with the flameproof box lid removed.

**NOTE:** *Before replacing the lid on the flameproof box, make sure that the O-ring is not damaged and is seated properly in its groove.<BR>
If the O-ring is damaged and needs replacing, replace it with an O-ring of the same size and specification (176 N70).*

<BR>

# 9.21 Power Supply Replacement
Before you start, obtain the following replacement parts 
-	Replacement Power Supply part number F-CP-C5K-PS
To remove the C5000 Power Supply:
-	De-gas the dispenser.
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Remove the flameproof box lid to gain access to the C5000 power supply board.

**CAUTION:** Take basic anti-static precautions by wearing a wristband with an earth strap. 

-	Undo the screws that hold the earth bar in the Flameproof box, taking care not to lose any of the spacers or other mounting hardware
-	Undo the screws that hold the terminal board in the flame proof box and remove the terminal board.
-	Undo the screws that hold any coms or GPIO board into the C5000 processor board.
-	Undo the screws that hold the C5000 processor board in the flameproof box and remove the C5000 processor board.
-	Undo the screws that hold the C5000 power supply board in the flame proof box 
-	Carefully slide out the C5000 power supply board to gain access to the plugs on the Com bus Cable that connects into the bottom PCB, and unplug this.

Completely remove the C5000 power supply board.

 
To install the new C5000 power supply:
-	To install the new C5000 power supply, reverse the procedure above.

**DANGER:** Before replacing the lid on the flameproof box, make sure that the O-ring is not damaged, and is seated properly in its groove. If the O-ring is damaged and needs replacing, replace it with an O-ring of the same size and specification (176 N70). 

**NOTE:** It should not be necessary to recalibrate the dispenser. However, in some locations, this may be legally required as per the Calibrate the Meter section.

# 9.22 Processor Board Replacement

Before you start, obtain the following replacement parts 
-	Replacement C5000 Processor part number **F-CP-C5K-PROCES**

To remove the C5000 processor board:
-	De-gas the dispenser.
-	If possible, record all the set-up data by accessing the **Parameter** switch and the **K-Factor** switch. The Software Set-Up and Upgrade section contains details on obtaining this information. 
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser.<BR>
Failure to turn off the power could result in an electric shock.

-	Remove the flameproof box lid to gain access to the C5000 Processor board.

**CAUTION:** Take basic anti-static precautions by wearing a wristband with an earth strap. 

-	Undo the screws that hold any coms or GPIO board into the C5000 processor board.
-	Undo the screws that hold the C5000 processor board in the flameproof box and remove the C5000 processor board.

To install the new C5000 processor board:
-	Put the new C5000 board in place of the old one, 
-	Do up the screws that hold the C5000 processor board in the flameproof box.
-	Do up the screws for any coms or GPIO board into the C5000 processor board.
-	Reinstalled the lid on the flameproof box

**DANGER:** Before replacing the lid on the flameproof box, make sure that the O-ring is not damaged, and is seated properly in its groove. If the O-ring is damaged and needs replacing, replace it with an O-ring of the same size and specification (176 N70). 

-	Switch on the power supply to the dispenser.
-	Press the K-factor button on the K-Factor board to sync the settings in the K-Factor board with the C5000 processor board 
-	Check dispenser operation

**NOTE:** It necessary to recalibrate the dispenser.

# 9.23 Temperature Pressure Board Replacement 

Before you start, obtain the following replacement parts<BR>

Replacement Temperature and Pressure board part number: **F-CP-C5K-CNG-TP**

To remove the temperature pressure board:
-	De-gas the dispenser.
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Access the temperature pressure board. 

**CAUTION:** Take basic anti-static precautions by wearing a wristband with an earth strap.

Unplug all wiring from the temperature pressure board and remove the board from its position.
To install the new temperature pressure board:
-	Put the new board in place of the old one and plug all the wiring back in the same order as before. 
-	Make sure the Dip switches are the same as the board that was taken out
-	Turn the power to the dispenser back on.
-	Check Dispenser operation. Checking Dispenser Operation.  

**NOTE:** It should not be necessary to re-calibrate the dispenser unless a pressure transducer or temperature probe needs to be replaced.

# 9.24 Dispenser Software Upgrade or Replacement
You can upgrade the dispenser software via USB Stick. Make sure the USB stick is formatted as FAT32 and has the new dispenser software loaded on it.

**CAUTION:** Before working on the dispenser electronics, take basic anti-static precautions by wearing a wristband with an earth strap.<BR>

To record set-up data and tote information:
-	Access the K-Factor board by opening the cover behind the main display. 
-	Record all the set-up data by accessing the Parameter switch and the K-Factor switch. Refer to Parameter Switch Settings and K-Factor Switch Settings to obtain this information.

The following data is required from the Parameter switch :
	Dispenser pump price.
	Dispenser pump number.
	Dispenser Setting
	Software Program number, if you are upgrading to a new version. 

The following data is required from the K-Factor switch:
	The K-Factor. There is a value for side A and side B in dual hose dispensers.
	Configuration Code C.
	The Density Factor.

-	Record the tote information by pressing the nozzle switch or start button quickly five times
 
To install the new C5000 software
-	Switch off the power supply to the dispenser.

**DANGER:** Never remove any electrical components without first switching off the power to the dispenser. Failure to turn off the power could result in an electric shock.

-	Remove the flameproof box lid to gain access to the C5000 Processor board.
-	Install the USB stick for the software that you want to install. If there is a coms or GPIO card installed on the C5000 processor board, you might have to remove it.
-	Reinstalled the lid on the flameproof box

**DANGER:** Before replacing the lid on the flameproof box, make sure that the O-ring is not damaged, and is seated properly in its groove. If the O-ring is damaged and needs replacing, replace it with an O-ring of the same size and specification (**176 N70**). 

-	Switch on the power supply to the dispenser.
-	The Display will display hold. The display will change from hold to calib, this mean that the software has been upgraded.
-	Press the K-Factor board button on the K-Factor board to clear the caib from the display and sync the K-Factor board settings will the C5000 processor board.
-	Check the dispenser operation Checking Dispenser Operation.
 
<BR>

# 10.0 Dispenser Calibration

# 10.1 Meter Calibration

Calibrating the meter involves:<BR>

- Comparing the dispensers stated amount dispensed to actual amount dispensed.<BR> 
- Adjusting the K-Factor if accuracy is not within the required tolerance.  

**NOTE:** *The K-Factor for each new dispenser is factory set but the Dispenser must be calibrated on site.*<BR> 

To test the meter accuracy:<BR>
Record the dispenser’s current density factor and set it to read out in kg Density Factor (d5F).<BR>

- Test the meter accuracy using either Calibration Test Fill Procedure Method 1 or Calibration Test Fill Procedure Method 2.<BR>

To calculate the meter K-Factor:
- Make sure that the dispenser is idle.
- Press and release the **K-Factor** button on the K-Factor board until the K-Factor is displayed

Calculate the new K-Factor with the following formula:<BR>

New K Factor=existing K Factor×(Dispensed quantity)/(Displayed quantity)<BR>

Example:<BR>

Existing K Factor=0.98 <BR>
Displayed quantity=5.80<BR>
Dispensed quantity=6.00kg<BR>
New K Factor=0.98×(6.00/5.80) =1.0138 (4dp)

To input dispenser settings:
- Input the new meter K-factor.
- Set the density factor back to its original value. (dSF).

**Calibration Test Fill Procedure Method 1**

Method 1 of checking calibration involves filling a gas bottle and comparing the read-out scale reading with the dispenser display reading.

Before you start, make sure you have:<BR>

-	Certified weighing scales with a read-out accuracy of +/- 20 g or better and a range of  0 – 120 kg
-	A CNG cylinder with a fill and release valve

To carry out the Calibration Test Fill Procedure Method 1:

-	Put the CNG cylinder on the scales.
-	Empty the CNG cylinder by venting it to the atmosphere.

**DANGER:** Always vent cylinders in a safe manner and safe location.

-	Zero the TARE read-out on the scales. 
-	Fill the CNG cylinder from the Dispenser. 
-	Compare the read-out weight (Dispensed Quantity) on the scales with the dispenser display (Displayed Quantity).

If the results are not within 0.5% of each other, you will need to change the calibration, as per the Calculate and Set the New K-Factor section above.

**Calibration Test Fill Procedure Method 2**
 
Method 2 of checking calibration involves filling a vessel and comparing a Master Meter reading with the dispenser display readings.<BR>
This method assumes that the master meter is sufficiently accurate and reliable enough to be considered a good reference.<BR>
Before you start, make sure you have a Master Meter<BR>

To carry out the Calibration Test Fill Procedure Method 2:
-	Plug the dispenser refuelling probe into the Master Meter, and then plug the master meter refuelling probe into a vehicle to fill.
-	Turn on the Master Meter valve, if applicable, and reset to zero.
-	Fill the vehicle from the dispenser. 
-	Turn off the dispenser refuelling valve and Master Meter valve, if applicable. 
-	Compare the Master Meter read-out (Dispensed Quantity) with the dispenser display (Displayed Quantity).

If the results are not within 0.5% of each other, you will need to change the calibration, as per the Calculate and Set the New K-Factor section above.

# 10.2 Pressure Transducer Calibration 

Calibrating the dispenser pressure transducers is done by setting the Pressure probe calibration points.<BR>
The following procedure is how to set these points.

**NOTE:** *The pressure transducers are calibrated at the factory and usually do not require recalibration.*

To set pressure probe calibration points:<BR>

-	Degas the dispenser and close all outlet isolation valves
-	Turn on the gas to the dispenser. 
-	Remove the nozzle from its holster or press the start button, allowing gas to pass through the dispenser.
-	Slowly open the outlet isolation valve and watch as the pressure gauge begins to rise. Shut the valve when the reading is approximately 10 bar.
-	Hang up the nozzle or press the stop button.
-	Set the uA1L (low pressure probe 1 calibration point)to 10. If there are 2 pressure transducers per side set uA2L (low pressure probe 2 calibration point) as well
-	Remove the nozzle from its holster again or press the start button.
-	Increase the gauge pressure to approximately 200 bar.
-	Hang up the nozzle or press the STOP button.
-	Set the uA1h (high pressure probe 1 calibration point) to 200. If there are 2 pressure transducers per side set Ua2h (high pressure probe 2 calibration point) as well
-	Check current calibrated pressure is the same as the Pressure gauge 

# 10.3 Ambient Temperature Sensor Calibration

Calibrating the Ambient Temperature Sensor involves:
-	Comparing the dispensers stated temperature to the actual temperature. 
-	Adjusting the ambient temperature reading if it is found to be incorrect.

To test the sensor accuracy:<BR>

Using a calibrated temperature meter, determine the temperature of the body of the dispenser Ambient temperature sensor.<BR>
Access the current dispenser ambient temperature reading.
To adjust the dispenser reading:

Adjust the dispenser’s ambient temperature reading to match that of the calibrated temperature meter.














# MODBUS

MODBUS Registers

|Register|Type|Access|Designation|Operational|Notes
|-|-|-|-|-|-
0100|	U16|	RO|	Operation Flags|	YES	
0101|	U16|	RO|	Unit Pric	YES	
0102|	U32|	RO|	Current Quantity|	YES|	3dp implied
0104|	U32|	RO|	Current Amount|	YES|	2dp implied
0106|	BCD12|	RO|	Hose Quantity|	YES|	00+ 5 BYTES BCD
0109|	BCD12|	RO|	Hose Amount|	YES|	00+ 5 BYTES BCD
0112|	U16|	RO|	Pressure|	YES|	Live, Transducer
0113|	U16|	RO|	Flow rate|	YES|	Live, kg/min 2dp (3dp is available with native I32)
0114|	U16|	RO|	Error Flags|	YES|	
0115|	I16|	RO|	Ambient Temperature|		YES|	Live from onboard T/P Board sensor
0116|	I16|	RO|	Gas Temperature|	YES|	Live from MODBUS meter 
0117|	BCD8|	RO|	Hose Quantity per electronic tote|	YES|	2dp implied
0124|	U16|	RO|	End of sale indicator| 	YES|	Last end of delivery
0125|	U32|	RO|	Quantity|	YES|	Last end of delivery, 3dp
0127|	U32|	RO|	Amount| 	YES|	Last end of delivery, 3dp
0129|	I16|	RO|	Gas Temperature|	YES|	Last end of delivery, 1dp
0130|	U16|	RO|	Pressure|	YES|	Start of last delivery, 0dp
0131|	U16|	RO|	Pressure|	YES|	End of last delivery, 0dp
0200|	U16|	RW|	Dispenser lock|	YES|	0 = free; 1 = locked. Acts as a nozzle up reason to prevent fill or stop fill. These things to right are no longer in use ->Setting the C4000 B code to 1xxx will continue to apply the lock status after dispenser re-power, else the dispenser will re-power in stand-alone mode
0201|	U16|	RW|	Unit Price|	YES|	0.00->655.35, 2dp implied. Size limited by U16 register. Stored as U32, 3dp.
0202|	U16|	RW|	Target Fill Pressure|	YES|	0-350, bar 0dp
0203|	U16|	RW|	Max fill pressure|	YES|	0-350.0, bar 1dp. Internally sets overpressure cutoff (Max pressure setting is now redundant
0204|	U16|	RW|	Sequence rate Low to Med bank|	YES|	0,1,2 (fast, med, slow). internally does not exist, sets global bank switch over rate! Only Side 1 changes. Side 2 is ignored to stop toggling of shared global setting. Backwards compatible with existing tool if 10,20,30 (10,2.0,3.0) etc is sent, sets the closest setting (1.0kg slow, 3.0kg med, 5.0kg fast)
0205|	U16|	RW|	Sequence rate Med to High bank|	NO|	Register is not linked to config. Use 204 to change sequencing speed.
0206|	U32|	RW|	Density Factor (NEW)|	YES|	Density factor, 4dp (10000 -> 1.0000)
0208|	U16|	RW|	Virtual switch||		0 (0b00) no switch pressed. 1 (0b01) start. 2 (0b10) stop. 3 (0b11) Start & stop.

# Compac MODBUS timing diagram

The following Compac MODBUS timing diagram specifies the Start Interval Time  










