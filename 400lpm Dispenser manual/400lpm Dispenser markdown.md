
![image](Compac_front_page.png)

<font size ="6">

# Compac Master and Laser 400 lpm Liquid Fuel Dispensers <BR>

<font size ="8">

Installation manual

<font size ="3">

Updated 21 October, 2026

<font size ="65">
Laser 

![image](Laser.png)

Master

![image](Master.png)

<font size ="3">

**Conditions of Use**

- Please read this manual completely before working on, or making adjustments to, Compac equipment<BR>
- Compac Industries Limited accepts no liability for personal injury or property damage resulting from working on or adjusting the equipment incorrectly or without authorization.<BR> 
- Along with any warnings, instructions, and procedures in this manual, you should also observe any other common sense procedures that are generally applicable to equipment of this type.<BR>
- Failure to comply with any warnings, instructions, procedures, or any other common sense procedures may result in injury, equipment damage, property damage, or poor performance of the Compac equipment<BR>
- The major hazard involved with operating the Compac C5K processor is electrical shock. This hazard can be avoided if you adhere to the procedures in this manual and exercise all due care.<BR>
- Compac Industries Limited accepts no liability for direct, indirect, incidental, special, or consequential damages resulting from failure to follow any warnings, instructions, and procedures in this manual, or any other common sense procedures generally applicable to equipment of this type. The foregoing limitation extends to damages to person or property caused by the Compac C5K processor, or damages resulting from the inability to use the Compac C5K processor, including loss of profits, loss of products, loss of power supply, the cost of arranging an alternative power supply, and loss of time, whether incurred by the user or their employees, the installer, the commissioner, a service technician, or any third party.<BR> 
- Compac Industries Limited reserves the right to change the specifications of its products or the information in this manual without necessarily notifying its users.<BR>
- Variations in installation and operating conditions may affect the Compac C5K processor's performance. Compac Industries Limited has no control over each installation's unique operating environment. Hence, Compac Industries Limited makes no representations or warranties concerning the performance of the Compac C5K processor under the actual operating conditions prevailing at the installation. A technical expert of your choosing should validate all operating parameters for each application.<BR>
- Compac Industries Limited has made every effort to explain all servicing procedures, warnings, and safety precautions as clearly and completely as possible. However, due to the range of operating environments, it is not possible to anticipate every issue that may arise. This manual is intended to provide general guidance. For specific guidance and technical support, contact your authorised Compac supplier, using the contact details in the Product Identification section.
- Only parts supplied by or approved by Compac may be used and no unauthorised modifications to the hardware of software may be made. The use of non-approved parts or modifications will void all warranties and approvals. The use of non-approved parts or modifications may also constitute a safety hazard.
- Information in this manual shall not be deemed a warranty, representation, or guarantee. For warranty provisions applicable to the Compac C5000 processor, please refer to the warranty provided by the supplier.
- Unless otherwise noted, references to brand names, product names, or trademarks constitute the intellectual property of the owner thereof. Subject to your right to use the Compac C5K processor, Compac does not convey any right, title, or interest in its intellectual property, including and without limitation, its patents, copyrights, and know-how. 
- Every effort has been made to ensure the accuracy of this document. However, it may contain technical inaccuracies or typographical errors. Compac Industries Limited assumes no responsibility for and disclaims all liability of such inaccuracies, errors, or omissions in this publication.

<font size ="5">

**Validity**
<font size ="3">

This manual cover the following Compac products

**LASER and MASTER 400lpm Liquid Fuel Dispensers (excluding LPG)** 

**Notes:**

1. For 400lpm Dispensers that include 40-160lpm hoses, please also refer to the 40-160lpm Dispenser Manual for specific information 

Compac Industries Limited reserves the right to revise or change product specifications at any time.<BR>
This publication describes the state of the product at the time of publication and may not reflect the product at all times in the past or in the future.

**Manufactured by:**<BR>
Compac Laser and Master Dispensers are designed and manufactured by Compac Industries Limited<BR>
52 Walls Road, Penrose, Auckland 1061, New Zealand<BR>
P.O. Box 12-417, Penrose, Auckland 1641, New Zealand<BR>
Phone: + 64 9 579 2094<BR>
Fax: + 64 9 579 0635<BR>
Email: techsupport@compac.co.nz<BR>
www.compac.co.nz<BR>
Copyright ©2015 Compac Industries Limited, All Rights Reserved
<BR>

## Table of Contents

<font size ="5">

[**Dispenser Installation overview**](#dispenser-installation-overview)

<font size ="3">

<font size ="5">

[**Product Identification**](#product-identification)

<font size ="3">

<font size ="5">

[**Footprints**](#footprints)

[**Installation**](#installation)

<font size ="3">

[Static Electricity Precautions](#static-electricity-precautions)

[Pre-installation Check](#pre-installation-check)

[Procedures](#procedures) 

[Dispensing Hoses and Nozzles](#dispensing-hoses-and-nozzles)

[Breakaways](#breakaways)

[**Typical Wiring for a Dispenser**](#typical-wiring-for-a-dispenser)

<font size ="3">

[Incoming Mains](#incoming-mains)

[External Submersible or Transfer Pump connections](#external-submersible-or-transfer-pump-connections)

[Comms connections](#comms-connections)

[K-Factor Board](#k-factor-board)
 
[**Terminal Board connections**](#terminal-board-connections)

[MR400S, L400S](#mr400s-l400s)

[MMR400S (x2 C5K MR400S)](#mmr400s-x2-c5k-mr400s)

[MMR400-80S](#mmr400-80s)

[MMR400-160S](#mmr400-160s)

[MMR400S – with Estop switch fitted](#mmr400s--with-estop-switch-fitted)

[MMR400-160S – Aviation (2x C5K)](#mmr400-160s--aviation-2x-c5k)

<font size ="5">

[**Setting up the C5000**](#setting-up-the-c5000)

<font size ="3">

[**K-Factor Settings**](#k-factor-settings)

[Changing the K factor FA and Fb](#changing-the-k-factor-fa-and-fb)

[Changing the Solenoid Delay](#changing-the-solenoid-delay)

[**Parameter Switch Settings**](#parameter-switch-settings)

[Changing the Pump Number](#changing-the-pump-number)

[Changing the Price](#changing-the-price)

[Standalone Mode](#standalone-mode)

<font size ="5">

[**Notes**](#notes)

<font size ="3">

[Pump Controller](#pump-controller)

[Spare Fuses](#spare-fuses)

<font size ="5">

[**Error Messages and End of Sale Indicators**](#error-messages-and-end-of-sale-indicators)

<font size ="3">

<BR>

# Dispenser Installation overview

These are the basic steps to installing and commissioning a Compac dispenser<BR>
For more detailed information, please refer to the C5000 Master Manual.


1. Identify the model that you are installing. This is stamped on the side of the unit.
2. Download the correct footprint from the Compac Website. These can be found in the PRODUCTS section
3. Check the External Pump connections for your model from the table further down
4. Calibrate the Dispenser and adust the K Factor if required
5. Set the Solenoid Delay time
6. Set the Pump Number
7. Set the Price. **Important**: If connected to Controller, ensure that the correct price is being sent down to the Dispenser
8. If connected to a Controller, set the Standalone b setting as required.

<BR>

# Product Identification
Ensure you are using the correct installation instructions and footprint drawing before commencing site work or installation.<BR>
The identification plate is fastened to the bottom of the right-hand side panel when facing the front of the dispenser.<BR>
The model number is on the first line of the identification plate. The following example is for the Master Pump or Dispenser<BR>


![image](9.1.2_Model_Identification_Plate.png)

Understanding the model number:
The model number for dispensers is split into: Chassis style, hose configuration, pump or dispenser and specific application.
Use the table below to help identify the unit.

The same format applies to both Laser and Master models<BR>

MASTER pumps Dispensers model start with MR (single hose) or MMR (dual hose)<BR> 
LASER pumps Dispensers model start with L (single hose) or LL (dual hose) 

The following example is for the MASTER Pump or Dispenser<BR>

|Style|L/min oer hose|Pump style|Options
|-----|-----|-----|-----|
MR=single hose|MR40 = one hose @ 40l/min|P = Pump|Blank = standard|
MMR=multi hose|MMR40=two hoses @ 40 l/min|S = Dispenser|Avi = Aviation|
| |MMR80-40 = side A 80 lpm, side B = 40 lpm||Marine = Marine|

For example: **MMR 80-40S Marine** is a two-hose unit.<BR>
Hose side A is 80 l/min, side B is 40 l/min with external pumps.<BR>
As a marine model, it has stainless steel pipework and stainless-steel chassis for marine conditions.

The following example is for the LASER Pump or Dispenser<BR>
|Style|L/min oer hose|Pump style|Options
|-----|-----|-----|-----|
L=single hose|L40 = one hose @ 40l/min|P = Pump|Blank = standard|
LL=multi hose|LL40=two hoses @ 40 l/min|S = Dispenser|Avi = Aviation|
| |LL80-40 = side A 80 lpm, side B = 40 lpm||Marine = Marine|


<BR>

# Footprints

The following 400lpm Footprints are available for downloading from the Products / Master / Documentation section on the Compac Website<BR>
**NOTE:** There may be more than one footprint for a particular model due to customer/market variations and customisations<BR>

|Model number|Footprint number|Special Notes|
|------------|----------------|-----|  
|MR400S|MAD0132G-01-D||  
|MMR400-160S|MAD0138G-01-C||
|MMR400-80S|MAD0139D-01-C||
|MR400S|MAD0140C-01-B|Aviation|
|MMR400S|MAD0152C-01-B|2x sets of C5K electronics - one for each hose| 
|MMR400-160S|MAD0183A-01-A|Aviation model with no filter on the 160 lpm side| 
|MMR400-160S|MAD0274A|Aviation model with 2x C5K electronics|

<BR>

<font size ="5">

# Installation

<font size ="3">

# Static Electricity Precautions
Electronic components used are sensitive to static. Please take anti-static precautions.
An anti-static wrist strap should be worn and connected correctly when working on any electronic equipment. If an anti-static wrist strap is unavailable, or in an emergency, hold onto an earthed part of the pump/dispenser frame whilst working on the equipment. This is not a recommended alternative to wearing an anti-static wrist strap.<BR>

**NOTE:** Compac Industries Limited reserves the right to refuse to accept any circuit boards returned, if proper anti-static precautions have not been taken.

# Pre-installation Check
Once the pump is received on site, check that no damage has occurred while in transit – in particular, damage to electronics due to vibration or jarring.<BR>
All terminals and plugs should be checked, including IC chips, to ensure they are securely in place.

# Procedures
Installation should be in accordance with local regulations.<BR>
The dispensing equipment shall be installed to prevent the delivery hose from contacting the ground when not in use.<BR>
Where local regulations require a sump to be fitted:<BR>
a.	Sumps must be provided at all dispenser installations with secondary containment pipework and at all new installations.<BR>
b.	At all sites with sumps, dispensers must be installed with a liquid level detection device fitted in the sump that will raise an alarm if liquid is detected in the base of the sump.<BR>
c.	All Compac Master dispensers at automotive sites must have a safe break device installed in the delivery hose.<BR>
d.	External pump systems required to have an automatic emergency shut-off device installed at the base of each dispenser and it must be activated if the dispenser is knocked over or pulled from its mount.<BR>

# Dispensing Hoses and Nozzles

The unit may or may not be supplied with dispensing hose and nozzle assemblies.<BR> 
If customer supplied hose assemblies, pylons, reels, safe breaks and nozzles are used they must comply with the requirements outlined in AS/NZS 2229.<BR>
All dispenser nozzles must trip shut when returned to the nozzle holder. 

# Breakaways

For all dispensers fitted with breakaways, ensure the breakaway is installed between the nozzle and the high-mast or pylon (if fitted).<BR>
Any breakaways that have been subject to a break-away situation should be inspected and refitted or replaced in accordance with the original manufacturer’s instructions.


<BR>

# Typical Wiring for a Dispenser

The instructions below refer to basic installation wiring.<BR>
Prior to pump installation ensure that there is at least a two-metre tail on both the incoming underground mains supply cable and
comms cable (if comms enabled).<BR>
These cables are terminated at the C5000 power supply, which is housed in the flameproof enclosure located in the bottom of the pump, behind the door.<BR>
Mains power wiring should be rated for a maximum current draw of 10 A rms at 220-240 V ac.
Refer to AS/NZS 60079.14 for appropriate cabling.<BR>

**NOTE:** All cables entering the power supply must be glanded with certified 20mm flameproof
glands.<BR>
**NOTE:** Output to submersible pump(s) is 230 V ac, 300 mA max. It is wired to the pump
contactor/relay at the switchboard and not directly to the pump.<BR>
**NOTE:** Before any additional switch or replacement switch (e.g. remote nozzle or sump switch) is
connected to the K-Factor board (J11-J14 or JJ21-J24), the switch circuit must be tested to
ensure that with the two switch wires connected together there is at least 500Vac (700Vdc)
isolation between the switch and earth.<BR>
**NOTE:** Comms cable is not intrinsically safe.<BR>
**NOTE:** Pump comms connects to pump controller such as a ComfillV2, PT1 or 3rd Party Controller etc. (optional).<BR>
When replacing the lid of the flameproof enclosure, ensure the sealing O ring is in place

![image](2.1.1_Power_Supply_in_FPbox.png)

# Incoming Mains
Incoming mains connections should be brought in to the terminal board.<BR>
<BR>
If an emergency stop button was ordered with the dispenser, it will be factory wired into the
terminal board, shown below.<BR>
This will be in place of the normal loop between the triac and
main phases.<BR>
If there is an Overfill Protection System (either Compac or Third Party), it should be wired as an Emergency Stop Switch would be between the Triac Phase and Mains Phase<BR>
If there is both an Emergency Stop Switch and an Overfill Protection System, they should be wired in series so that either can interrupt the Triac Phase in cas of an emergency 



Wires have standard colours which are shown. In case these colours are unclear, they are as
follows:<BR>
▪ Incoming mains phase: Brown<BR>
▪ Incoming mains neutral: Blue<BR>
▪ Incoming mains earth: Green/Yellow<BR>

![image](1.1.1_Mains_connections.png)

<BR>

# External Submersible or Transfer Pump connections

**Single hose 400lpm Dispensers**<BR>
Connect the cable from the External Submersible or Transfer Pump Contactor to **Side A-MTR RELAY (LOW) - T1**

**Dual Hose 400lpm Dispensers**<BR>
Connect the cable from the External Submersible or Transfer Pump Contactor for side A to **Side A-MTR RELAY (LOW) - T1**<BR>
Connect the cable from the External Submersible or Transfer Pump Contactor for side B to **Side B-MTR RELAY (LOW) - T4**<BR>


**Notes:**
1. C5000 External pump triac outputs have a maximum rating of 300mA so must be connected via a contactor, not directly to Pump Motor<BR>
2. If both sides of a dual hose Dispenser are to connect to the same External Submersible or Transfer Pump, then T1 and T4 may be linked together and a single cable taken to the Contactor  

<BR>

# Connecting an Overfill Protection System

The Overfill Protection system (Either a Compac Overfill Protection built in to the Dispenser, or an external system) connects between the MAINS PHASE and the TRIAC PHASE (refer to the EMERGENCY Connection on the drawing above)

This controls power to the 230V Triac outputs for the Solenoid and Motor output.

If it is a Compac Overfill Protection system, there will be Permissve (Green) and Red (non-permissive) lights on the Dispenser
The Permissive (green) light must be on for the Dispenser to fill.  

In the event of an overfill situation or a non-permissive vehicle /probe, power will be interrupted to triacs
The Solenoid Valve will close and the Motor output will go off.
The Fill will stop immediately and the Dispenser electronics wil time out on no flow

<BR>

# Comms connections

The comms I/O is controlled by the connections to the CI501 Comms board which is piggy backed on the Power Supply inside the flame-proof enclosure.<BR>

Refer to the following diagram for connecting RS485, RS232, Compac or Gilbarco pumps. The shown switch should be set to the desired setting. <BR>

**NOTE** Ensure that SW200 (Switch 1) is set the required protocol

<BR>

![image](2.1.5_CI501-Comms_board.png)

Switches 300, 302, and 303 are for RS485/RS232 Terminator application.
Use the following table to configure these switches. Switch 300 is for channel 1, and switches 302 and 303 are for channel 2.

![image](9.3.1_CI501_Dip_Switches.png)

<BR>

# K-Factor Board

Both the Parameter switch and K-Factor switch are found on the K-Factor board. Meters and air switches are also connected to this board. See below for the location of these.

![image](2.1.3_Kfactor_board.png)

<BR>

<font size ="6">

# Terminal Board connections

<BR>

<font size ="3">

# MR400S, L400S

NOTE: If an ACV valve is used instead of the ‘Large Single Stage Solenoid, the 400S pre-set solenoid will only need to be wired to the SFS terminal.<BR>

![image](1.6.1_Terminals_MR400S,L400S.png)

<BR>

# MMR400S (x2 C5K MR400S)

Two C5000 Flame Proof Box assembly will be connected in a MMR400S.<BR>
Therefore, two Terminal boards will be wired separately. It will be differentiated by Side A1 and A2.<BR>
• Wire the solenoids and Terminal Board from Side A1 together.<BR>
• Same goes for wiring the Side A2 assembly.

![image](1.6.2_Terminals_MMR400S_2x_C5K_MR400S.png)

**NOTE:**If an ACV valve is used instead of the ‘Large Single Stage Solenoid, the 400S pre-set solenoid will only need to be wired to the SFS terminal.

<BR>

# MMR400-80S

![image](1.6.3_Terminals_MMR400-80S.png)

NOTE: If an ACV valve is used instead of the ‘Large Single Stage Solenoid, the 400S pre-set solenoid will only need to be wired to the SFS terminal.

<BR>

# MMR400-160S

![image](1.6.4_Terminals_MMR400_160S.png)

**Important note:**<BR>

As the side B MTR RELAY (LOW) motor output is used for the 160lpm side solenoids, there is only one Motor output that is common to both the 400 and 160 hoses.<BR>
Therefore, either hose will start the same pump.<BR>
If a separate Motor output is required for each hose, then the Dispenser should be order with 2x sets of C5K electronics.BR>
<BR>

**NOTE:** If an ACV valve is used instead of the ‘Large Single Stage Solenoid, the 400S pre-set solenoid will only need to be wired to the SFS terminal.<BR>

For the Side B MTR RELAY terminal, the primary and secondary core ends are twisted together with use a ferrule crimp.

<BR>

# MMR400S – with Estop switch fitted

The MMR400S has of 2x sets of C5K electronics with a 5 core and a 3 core OLEX Cable loop between them.<BR> 
Mains and Triac Phases are looped together through a 5 Core OLEX cable.<BR>
There is a separate “External Pump” connection labelled MTR RELAY(LOW) for each C5000<BR>
If both hoses need to switch one “External Pump”, there is an unused core in the 5 Core OLEX loop cable for the installer to loop both “External Pump” connections together.
 
Comms are looped together between the 2 sets of electronics with a 3 core Olex Cable

![image](1.6.5_Terminals_MMR400S_with_Estop.png)

<BR>

# MMR400-160S – Aviation (2x C5K)

The MMR400-160S Aviation Dispenser has of 2x sets of C5K electronics with a 5 core and a 3 core OLEX Cable loop between them<BR> 
Mains and Triac Phases are looped together through a 5 Core OLEX cable.<BR>
There is a separate “External Pump” connection labelled MTR RELAY(LOW) for each C5000<BR>
If both hoses need to switch one “External Pump”, there is an unused core in the 5 Core OLEX loop cable for the installer to loop both “External Pump” connections together.<BR>

![image](1.6.6_Terminals_MMR400_160S_Avi_2x_C5K.png)

<BR>

# Setting up the C5000

# K-Factor Settings
The settings that can be accessed from the K-Factor switch are shown below. Not all of these will need to be changed during installation, therefore information on the following pages refers only to the settings that must be changed. Once the Dispenser has been installed, if further customisation of the unit is required, refer to the C5000 Master Manual.



| Setting               | Price Display       | Litres Display|Important notes  |
|-----------------------|---------------------|---------------|-----------------|
| Dispenser settings    | **c-A** or **c-B**  |  *******  | These are set in the factory and should not be changed|
| Maximum flow          |                     | **9A****** or **9b** ****                  |
| K-Factor              | **FA** or **Fb**    | **\*\*\*.\*\*\***                                 |
| Configuration code    | **c**               | **\*\*\*\*\*\*\***  | This is set in the factory and should not be changed|                                |
| Solenoid delay        |                     | **SdA** *** or **Sdb** ***                    |
| Preset cutoff         |                     | **PcA***.** or **Pcb***.** |This is available if a secondary solenoid is wired in
| Preset rounding       |                     | **PrLA***.** or **PrLb***.** **PrHA***.** or **PrHb***.**|
| Flow time out         |                     | **n-A** *** or **n-b** ***                    |

<BR>

# Changing the K factor FA and Fb

The K-Factor is used to calibrate product flow. It is a ratio of litres dispensed per revolution of the meter. The K-Factor may need to be calibrated after periods of time. 
To calibrate the pump, dispense fuel into a certified measuring container and compare the display value with the one dispensed.
Example:
The Display shows 10.00 litres but the True volume is actually 20.00 Litres

To calculate the correct K-Factor from the information above; firstly record the existing K-Factor and use this formula to calculate the new K Factor.

**New K Factor=Existing K Factor x (Dispensed Amount)/(Displayed Amount)**

=Existing K Factor x 20/10

=Existing K Factor x 2

See Using the Dispenser Menus to edit these settings. Use the procedure for both side A and B.

![image](3.1.6_Kfactor_Kfactor_FA.png)

<BR>

# Changing the Solenoid Delay

This is the time delay from when the submersible pump starts to when the solenoids in the dispenser open to allow time for the leak detector to reset.<BR>

This is factory set by Compac at 005 (five seconds).<BR>

If problems are experienced with the leak detector tripping, firstly check that the solenoid delay is still set and then, if necessary, make it longer as follows.<BR>

To change the solenoid delay, depress the K-Factor switch repeatedly until the following display is shown. To increment a digit, press and hold the parameter switch when the desired digit is flashing. Repeat this procedure for side B if applicable.

![image](3.1.10_Kfactor_Solenoid_Delay_SdA.png)

<BR>

# Parameter Switch Settings

The settings that can be accessed from the parameter switch are shown below.<BR>
Not all of these will need to be changed during installation, therefore information on the following pages refers only to the settings that must be changed.<BR>
Once the pump has been installed, if further customisation of the unit is required, refer to the C5000 Master Manual.

|Setting             |Price Display 	  |Litres Display       |
|--------------------|------------------|---------------------| 
|Software Version    |P**.**. **  	    |P**.**. **           |
|Pump Number  	     |                  |PnA *** or PnB ***   |
|Price               |                  |PA**.*** or Pb**.*** |
|Pump Settings       |	                |ba **** or bb ****   |
|High Preset cut off |                  |HCA** or HCb**       |
|High-flow cut off	 |                  |HFA***               |
|Low-flow cut off    |                  |LFA***               |
|b Setting           |                  |b****                |
|Slave display       |                  |d5 ****              |
|Custom display      |                  |dc ****              |
|Last Sale           |**.**             |A***.* or b***.*     |
|Electronic Totes    |LA **** or dA**** |L****.**             |
|                    |Lb **** or db****	|d****.**             |

<BR>

# Changing the Pump Number

If the parameter switch is continually depressed, the following menu to change the pump number will appear.<BR>
Each side must be numbered between 1-99. Entering a pump number 0 will disable the pump.<BR><BR>
To change the pump number, depress the parameter switch repeatedly until the following display is shown.<BR>
To increment a digit, press and hold the parameter switch when the desired digit is flashing. Repeat this procedure for side B if applicable.

![image](4.1.2_Parameter_pump_number_PnA.png)

<BR>

# Changing the Price

The price must be set before the dispenser can be used, otherwise an error will be returned. Set the price in dollars per litre.<BR>

To change the price, depress the parameter switch repeatedly until the following display is shown. To increment a digit, press and hold the parameter switch when the desired digit is flashing. Repeat this procedure for side B if applicable.

![image](4.1.3_Parameter_price_PA.png)

<BR>

# Standalone Mode
In standalone operation, the dispenser will continue working when not connected to a controller. When in Standalone mode no authorisation of fills is required and so fills are simply initiated by removing the refuelling assembly from its holder. If standalone operation is inhibited, the dispenser will not work in standalone mode, regardless of whether the dispenser is ONLINE to a controller or not.<BR> <BR>
The dispenser ceases to work in standalone mode if connected to a controller, regardless of the position of standalone setting.<BR><BR> 
Generally, on retail forecourts the dispenser should be set-up for standalone operation.  Hence, if the forecourt controller breaks down the dispensers can be set to work in standalone mode simply by turning them off then on again. <BR><BR>
For unattended refuelling sites, the dispensers should not be able to work in standalone mode in the event of a controller failure. Therefore, the dispenser should be set-up to inhibit standalone operation. <BR><BR>
This is set in the b code on the K factor switch. The b code to run Standalone without Dispenser Controller is 1000.  The b code to inhibit Standalone is 0000.

![image](4.1.13_Parameter_Preset_bA.png)

<BR>

# Notes

# C5000 External Pump Triac Outputs 

External pump outputs have a maximum rating of 300mA so must be connected via a contactor, not directly to the Pump Motor.
<BR>


<BR>

# Pump Controller
If the Dispenser is connected to a Point of Sale (POS) or a Compac Controller such as a PT1, check that pump data and transaction information is being correctly uploaded to it.<BR>
Ensure that the Contoller is sending the correct price to the Dispenser<BR>
Refer to the Controller manual for specific instructions regarding connection and setup.

<BR>

# Spare Fuses
In the event of a fuse blowing on the C5000 Power supply a bag of 3 is included in each flameproof box. Any fuses used from this bag should be replaced.<BR>
NOTE: There are three different ratings used. If replacing a fuse, ensure that the correct value is used. 

<BR>

# Precautions if Using Generator Power
The power output from onsite generators can cause power spikes that may damage electrical components within the cabinet. When connecting to sites powered by generators, please take the following precautions:
1.	Install a power conditioner. Although generators are fitted with power regulators, most are not filtered sufficiently for powering sensitive electrical components. We recommend installing a commercial power conditioner and/or UPS between the generator and the unit.
2.	Before starting a generator, make sure the power to the unit is turned off. Start the generator, let the generator reach stable operating speed and wait 30 seconds before reconnecting the power to the unit.
3.	For units where the generator starts and stops on demand, install a delay timer or PLC to automatically isolate the unit until the operating speed and consistent power output is achieved.
4.	Isolate the unit before shutting down the generator.

<BR>

# Error Messages and End of Sale Indicators

These are all the Error codes available in the C5000.<BR>
Some are product specific so will not be found in all applications.

|Error Code      | Fuel specific | Possible causes                                | Suggested action  
-----------------| --------------| -----------------------------------------------| ---------------- 
**Er 3 or Err 3**   |No             |Price or Pump number not set in the Dispenser         |(a) If the Dispenser is connected to a Site Controller, the price on the Dispenser should be set to 0.00 and the pricing should be sent from the Controller.(b)If the Dispenser is not connected to a Site Controler (ie. it is operating in standalone mode), then the price must be set in the Dispenser. (c) Set the hose number in the dispenser
**Er 8 or Err 8**   |No             |Excessive reverse flow                          |Check that product is not flowing back into the tank once the delivery has finished. This can occur if the non-return valves on site are leaking
**Er 9 or Err 9**   |No             |The Flow Meter is in an illegal state           |(a)Re-power the Dispenser (b) Check Meter cable for loose wires or bad connections (c) Replace the Meter or the Encoder board on the Meter   
**Err91**           |No             |Meter sequence error                            |If 3rd party Meter, check the wiring
**Er 10 or Err 10** |No             |Memory Error. Configuration data lost or corrupted|Re-configure Dispenser. If problem persists, replace Memory or Processor Board             
**Er 12 or Err 12** |No             |Display error                                   |Replace Display
**Err 13**          |No             |Slave board has restarted                       |Power or Hardware failure
**Err 14**          |No             |K Factor board offline                          |Check the Bus Connections and C5K Power Supply
**Err 15**          |No             |K Factor board has restarted                    |Power or Hardware failure
**Err 16**          |No             |K Factor board is not talking to the LCD Display|(a) Check wiring (b) Replace the K factor board or LCD Display       
**Err 31**          |No             |Transaction has ended but fuel is still flowing |The Solenoid is leaking. Repair or replace solenoid
**Er 41 or Err 41** |No             | Pump not communicating with Controller          |If only one pump on the site is not communicating with the Controller, then the fault is likely to be in the pump.(a) Check the comms wire connection on the comms board  (b) Check the diagnostic LEDs on the comms board in the Dispenser to diagnose cause (c) Check the configuration and setup in the Dispenser.
|   |   |   |If all pumps are not communicating, check the comms wire connections on the comms board (a) Check comms cables between the Dispenser and the Controller (b) check setup and operation of the Controller
**Er 50**           |NO               |Meter not communicating with Dispenser electronics|(a) Check Meter connections (b) Check Dispenser configuration (c) Check that the Meter ID setup in the configuration matches the Meter ID
**Er 52**            | No             | Meter error | If the problem persists after repowering the unit, replace the meter.
**Er 53**            | LPG / Adblue / DEF / CNG |Meter stopped ibrating | Repower the unit. This error might display when the dispenser is powered up. In this case it is normal. If the problem persists, replace the meter
**Er 54**            | No           | Temperature sensor failure | Repower the unit. If the problem persists, replace the meter
**Er 55**            | CNG          | Meter not ready.  | Wait for meter to calibrate itself. The KG100 meter is in startup mode. If the problem persists, repower the unit.
**Er 61**            | LPG / Adblue / DEF / CNG | Error 61 happens because the Meter was not able to zero |(a) This can be due to a leak in the line or crystals accumulated in the Meter. (b) Check for leaks / crystallization. Purge the line. (c) If that does not reset the Error 61, pull the Meter out and pour hot water on it to dissolve any crystals inside the Meter. (d) If the problem persists, replace the Meter.
**Er 62**            |LPG / Adblue / DEF / CNG | Meter could not reset the batch (Could not zero the transaction values when nozzle was lifted to start a new transaction)                                                                                                 | Try restarting the Meter. If the problem persists, Replace the meter.
**Er 71**            |LPG / Adblue / DEF | V50 meter is set but variant is not selected  | Configure Device to either AdBlue / DEF or LPG
**Abd**              |No             |Display offline / Display Fault |(a) Check the connections to all displays.(b) Check the configuration of the  slave boards (If slave displays are connected) (c)Check and/or replace the display
**hoLd**             |No             |There are two types of HOLD error. There is a “Soft” HOLD err or that resets after the unit is re-powered and a “Hard” HOLD error that does not reset after the unit is re-powered. Display may also show Error 14 on display     | Re-power the unit. Does the HOLD error reset? (a) If the HOLD error resets but the problem persists, then the SD card may be corrupt and require replacement. Refer to the SD replacement procedure document.(b) If the HOLD error did not reset, then there is a possible hardware fault in the Power Supply PCB / Processor PCB board / K factor PCB board / other PCB board or Bus cable.          
**Calib c**          |No             | K-Factor data integrity failure, or the processor board has been replaced                       |  To reset, break the K factor switch seal and momentarily press
**Calib p**          |No             |The K-Factor board has been swapped/replaced   |  To reset, break the K factor switch seal and momentarily press
**Calib**            |No             |The unit needs calibration, usually due to a hardware change   | Check the K-Factor, temperature and density calibration
**Calib f**          |No             |K-Factor is not set or is 00.0000     | Calibrate the unit and set the K factor
**Air**              |No             |1. Air is in the system. 2. Density out of range 3. Coil amplitude too low while meter is operating, displayed until next sale is started | Make sure pump is running. Check tank and pipework for leaks. Purge system. Increase the Solenoid delay on the K-Factor switch
**Orun**             |No             |Preset amount Overrun – flow above preset  | Check that solenoid is closing. Increase the preset cutoff
**5ump**             |No             |Sump error – liquid detected in the sump   | Empty the sump. Check the dispenser for leaks. Check for water etc getting into the sump.
**Ga5**              |LPG            |For LPG, the density being returned from the meter is too low  | Calibrate meter density using the K-Factor switch
**ABDL**             |No             |Display LCD error | There is a problem with the K Factor Board talking to the LCD. Check cables, plugs etc. If problem persists, replace K Factor board / LCD Display
**Er FLO**           |No             |Excess Flow        | Maximum flow rate exceeded, Increase Maximum flow rate setting or restrict flow
**ErPrSt**           |No             |The preset entered is below the MMQ   | Enter a preset above (or equal to) the MMQ
**Er dEn**           |LPG            |Density or Temperature out of Range | Calibrate meter density using the K-Factor switch  Calibrate meter temperature using the K-Factor switch

# END OF SALE Indicators

The purpose of the END OF SALE Indicator to give the reason why the last fill ended.

This is useful if it is not apparent why the last fill stopped

The EOS number will appear on the Dispenser Display at the end of the fill.
If there is a PINPad keypad / Display fitted, an EOS error code will be displayed on it

Some END OF SALE Indicators are a result of a fault in the system.

Other END OF SALE Indicators are normal operation

Note: This is a complete list of all the available END OF SALE Indicators and covers all Compac products. Some END OF SALE Indicators are Product / Fuel type specific



|Keypad Display (if fitted)   | Dispenser Display  | Description                                                              |  
|-----------------------------|--------------------|--------------------------------------------------------------------------|
**NOZ**                          | 1                  | The nozzle was hung up This is normal operation                          
**PRESET**                       | 2                  | The fill ended when it reached the preset amount or quantity          
**DISP**                         | 3                  | Normal fill                                                              
**OFFLINE**                      | 4                  | Comms not connected between Dispenser and Controller. Check comms connections and setup in the Dispenser and Controller.
**MAX**                          | 5                  | The fill reached either the maximum dollars or litres amount allowed     
**AIR**                          | 6                  | Air was detected in the fuel so the air switch cut out. Check for air in the fuel.
**ERROR**                        | 7                  | There was an error with the encoder in the flow meter. Check the Flow Meter   
**SUMP**                         | 9                  | Sump switch cut out because there was either water or fuel in the sump   
**TO ATH**                       | 12                 | Pre-auth from the Controller or Payment Terminal timed out. The customer may have taken too long to start the fill after it was authorised
**POR**                          | 13                 | The unit was repowered 
**STP SW**                       | 14                 | The Stop Switch was activated 
**PRST ERR**                     | 15                 | An Invalid preset value was entered
|                             | 17                 | There is a Display offline 
|                             | 18                 | The Displays are not paired 
|                             | 30                 | Controller initiated stop 
**DENSITY**                      | 35                 | The Density was out of range 













































