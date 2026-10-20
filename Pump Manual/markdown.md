
![image](Compac_front_page.png)

<font size ="6">

# Compac Master and Laser Liquid Fuel Pumps 40 to 160lpm <BR>

<font size ="8">

Installation manual

<font size ="3">

Updated 20 October, 2026

<font size ="65">
Laser 

![image](Laser.png)

Master

![image](Master.png)

<font size ="3">

**Conditions of Use**
<font size ="3">

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

LASER and MASTER 40 to 160lpm Liquid Fuel Pumps (excluding LPG)

**Notes:**

1. For 40 to 160 lpm Pumps that include Adblue hoses, please also refer to the Adblue Manual for Adblue specific information

2. For 40 to 160 lpm Pumps that include High Flow diesel hoses (eg 400lpm) hoses, please also refer to the 400lpm High Flow Manual for specific information
Compac Industries Limited reserves the right to revise or change product specifications at any time.<BR>
This publication describes the state of the product at the time of publication and may not reflect the product at all times in the past or in the future.


**Manufactured by:**<BR>
Compac Laser and Master Pumps are designed and manufactured by Compac Industries Limited<BR>
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

[**Pump installation overview**](#pump-installation-overview)

<font size ="3">

<font size ="5">

[**Product Identification**](#product-identification)

<font size ="3">

<font size ="5">

[**Installation**](#installation)

<font size ="3">

[Footprints](#footprints)

[Inlet connections](#inlet-connections) 

[Optional Inlet Flexi Coupling](#optional-inlet-flexi-coupling)

[Static Electricity Precautions](#static-electricity-precautions)

[Pre-installation Check](#pre-installation-check)

[**Below Ground Tank Installations**](#below-ground-tank-installations)

[**Above Ground Tank Installations**](#above-ground-tank-installations)

[Procedures](#procedures) 

[Dispensing Hoses and Nozzles](#dispensing-hoses-and-nozzles)

[Breakaways](#breakaways)

<font size ="5">

[**Typical Wiring for a Pump**](#typical-wiring-for-a-pump)

<font size ="3">

[Incoming Mains](#incoming-mains)

[Comms connections](#comms-connections)

[K-Factor Board](#k-factor-board)

[**Terminal Board connections**](#terminal-board-connections)

[MR40P, MR80P, L40P, L80P](#mr40p-mr80p-l40p-l80p)

[MR160P, L160P](#mr160p-l160p)

[MMR40P, MMR80P, LL40P, LL80P, L40PD](#mmr40p-mmr80p-ll40p-ll80p-l40pd)

[MMR80-40P,LL80-40P](#mmr80-40pll80-40p)

<font size ="5">

[**Setting up the C5000**](#setting-up-the-c5000)

<font size ="3">

[**K-Factor Settings**](#k-factor-settings)

[Changing the K factor FA and Fb](#changing-the-k-factor-fa-and-fb)

[**Parameter Switch Settings**](#parameter-switch-settings)

[Changing the Pump Number](#changing-the-pump-number)

[Changing the Price](#changing-the-price)

[Standalone Mode](#standalone-mode)

[Pump Controller](#pump-controller)

[Spare Fuses](#spare-fuses)

[Precautions if using Generator Power](#precautions-if-using-generator-power) 

<font size ="5">

[**Error Messages and End of Sale Indicators**](#error-messages-and-end-of-sale-indicators)

<font size ="3">

# Pump installation overview

These are the basic steps to installing and commissioning a Compac Pump<BR>
For more detailed information, please refer to the C5000 Master Manual.

1. Identify the model that you are installing. This is stamped on the side of the unit.
2. Download the correct footprint from the Compac Website. These can be found in the PRODUCTS section
3. Calibrate the Pump and adust the K Factor if required
5. Set the Pump Number
7. Set the Price. **Important**: If connected to Controller, ensure that the correct price is being sent down to the Pump
8. If connected to a Controller, set the Standalone b setting as required.

<BR> 

# Product Identification

The identification plate is fastened to the bottom of the right-hand side panel when facing the front of the dispenser.<BR>
The model number is on the first line of the identification plate. The following example is for the Master Pump or Dispenser<BR>


![image](9.1.2_Model_Identification_Plate.png)

Understanding the model number:
The model number for dispensers is split into: Chassis style, hose configuration, pump or dispenser and specific application.
Use the table below to help identify the unit.

The same format applies to both Laser and Master models<BR>

MASTER Pump models start with MR (single hose) or MMR (dual hose)<BR> 
LASER Pump models start with L (single hose) or LL (dual hose) 

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

**Pumps that include AdBlue**

Some Laser and Master Pumps have Adblue in addtion to Petrol or Diesel (40 to 160lpm)
Please refer to the Adblue manual for Adblue specific installation information 
This can be found in the Products section of the Compac Website

# Installation

# Footprints

Footprints for Compac Laser and Master Pumps can be downloaded from the Compac Website PRODUCTS section

# Inlet connections 

All outlets are approximately 680mm above the base: Outlet sizes are as follows:
	40 l/min - ¾” female BSP socket
	80 l/min - 1” female BSP socket
	160 l/min - 1 ¼” female BSP socket

Inlet pipework can be connected to the pump flange(s). <BR>
An optional flexible coupling is offered by Compac. There must be no fuel pressure in the pump line when pump is not operating.

# Optional Inlet Flexi Coupling

![image](10.1.1_Pump_Flange.png)

![image](10.1.2_Pump_Inlet_Flexy.png)


# Static Electricity Precautions
Electronic components used are sensitive to static. Please take anti-static precautions.
An anti-static wrist strap should be worn and connected correctly when working on any electronic equipment. If an anti-static wrist strap is unavailable, or in an emergency, hold onto an earthed part of the pump/dispenser frame whilst working on the equipment. This is not a recommended alternative to wearing an anti-static wrist strap.<BR>

**NOTE:** Compac Industries Limited reserves the right to refuse to accept any circuit boards returned, if proper anti-static precautions have not been taken.

# Pre-installation Check
Once the pump is received on site, check that no damage has occurred while in transit – in particular, damage to electronics due to vibration or jarring.<BR>
All terminals and plugs should be checked, including IC chips, to ensure they are securely in place.

# Below Ground Tank Installations
1.	Pumps must not be subject to any head pressure. Design your installation to eliminate any possibility of this occurring.
2.	Total length of horizontal piping between tank and pump should be no longer than 18 metres.<BR>
Use galvanised steel or approved non-metallic pipe and fittings.
3.	If the unit contains two pumps. It is recommended that each pump is supplied by a separate pipe. The common sizes used are.<BR>

•	40 l/min pumps, use a separate1½” pipe for each pump<BR>
•	80 l/min pumps, use a separate 2” pipe for each pump<BR>
•	160 l/min, single hose pumps, use either a separate 2” pipe for each pump, or, a single 3” pipe.<BR>

<font size ="4">

**Important Note:**  Do not feed two pumps from a single 2” pipe. This will result in the Pumps cavitating     

<font size ="3">

4.	Check valves must also be installed below each pump inlet.<BR>

5.	On 160lpm units, if a single 3" Suction line is used, Check valves must be fitted to the inlets of both pumps to prevent one pump drawing product back through the other. <BR>

<font size ="4">

**Important Note:**
Ensure that you remove the bung from the pump inlet before connecting the pipe.<BR>
If the bung is not removed, there wil be no product flow. <BR>

<font size ="3">

6.	Pipe must slope up from the tank to the pump (approximately 15 mm per metre). Pipe should be straight and supported along its length.
7.	All horizontal piping must be buried at least 450mm below ground level.
8.	The area under the pumping unit(s) must be filled with sand or dirt as far up the suction line as possible. Use water to pack the sand or dirt when put in place.
9.	Avoid asphalt drive surfaces covering the piping. Asphalt increases heat absorption causing vapour lock.
10.	Static lift must not exceed 3 metres (vertical distance from the product level in the tank to the centre of the pump unit).
11.	To absorb ground movement from settling of the tank, frost heaving of the ground or pump island settling, a swing joint must be used in the supply line at the tank and directly underneath the dispenser. Three additional directional changes using elbows are permitted. 
12.	Piping must hold a 3.4 Bar (50PSI) pressure test for a minimum of 10 minutes.
13.	It is recommended that a vertical, in-line check valve be installed underneath the pump.
14.	The dispensing equipment shall be installed to prevent the delivery hose from contacting the ground when not in use.
15.	A check valve must be installed at the tank end of the suction pipe in a serviceable location. Many clients install an extra check valve at the inlet to the pump. It is important neither of the check valves interfere with the flow of fuel. They must be adequately sized.

Refer to the footprint drawings for pump installation details.

![image](10.1.3_Underground_Tank.png)

<BR>
<BR>

# Above Ground Tank Installations

If a regulator valve is not installed correctly, product will pour out of the pump breather. If this happens do not plug the breather.<BR>
Review the installation and ensure that all the following requirements have been met. <BR>

The regulator valve must be mounted in the vertical position and directly underneath the pump. Do not mount alongside the pump as no pipework between the regulator valve and the pump is allowed to be below the regulator valve itself.<BR>

Do not plug the vent on the regulator valve. Pipe the vent back to the top of the tank or vent to atmosphere.<BR>

Maximum working pressure of fuel system = 50 psi / 3.4 bar<BR>

The installation must include a thermal expansion relief valve. Thermal expansion can cause pressures in the system greater than 50 psi / 3.4 bar and can result in failure of the valve and loss of product to the environment.<BR>
 
The installation must also include a solenoid valve positioned adjacent to the shut off valve at the tank. Its purpose is to prevent loss due to failure of the downstream piping or the system. The recommended solenoid is the Parker 2" type E321G4010 (available from Compac) <BR>

The Shear section of the regulator valve should be located level with the bottom of the cabinet base.<BR>

The installation must include a shutoff or gate valve to close the system and prevent loss when the equipment utilized in the fuelling system downstream from the above ground storage tank is being serviced or replaced.

![image](10.1.4_Above_Ground_Tank.png)

<BR>

# Dispensing Hoses and Nozzles

The unit may or may not be supplied with dispensing hose and nozzle assemblies.<BR> 
If customer supplied hose assemblies, pylons, reels, safe breaks and nozzles are used they must comply with the requirements outlined in AS/NZS 2229.<BR>
All Pump nozzles must trip shut when returned to the nozzle holder. 

# Breakaways

For all pumps that are fitted with breakaways, ensure that the breakaway is installed between the nozzle and the high-mast or pylon (if fitted).<BR>
Any breakaways that have been subject to a break-away situation should be inspected and refitted or replaced in accordance with the original manufacturer’s instructions.


# Typical Wiring for a Pump

The instructions below refer to basic installation wiring. Prior to pump installation ensure that there is at least a two-metre tail on both the incoming underground mains supply cable and comms cable (if comms enabled). These cables are terminated at the C5000 power supply, which is housed in the flameproof enclosure located in the bottom of the pump, behind the door.<BR>

Mains power wiring should be rated for a maximum current draw of 10 A rms at 220-240 V ac.<BR>

The incoming cables are terminated as shown in the following picture.<BR>

Refer to AS/NZS 60079.14 for appropriate cabling.<BR>

**NOTES:** 

- All cables entering the power supply must be glanded with certified 20mm flameproof glands.<BR>

- Comms cable is not intrinsically safe.<BR>

- Pump comms connects to pump controller such as a PT1, Comfill V2 or thord Party Controller etc. (option).
When replacing the lid of the flameproof enclosure, ensure the sealing O ring is in place.


![image](2.1.1_Power_Supply_in_FPbox.png)

# Incoming Mains
Incoming mains connections should be brought in to the terminal board.<BR>
<BR>
If an emergency stop button was ordered with the pump, it will be factory wired into the
terminal board, shown below.<BR>
This will be in place of the normal loop between the triac and
main phases.<BR>
If there is an Overfill Protection System (either Compac or Third Party), it should be wired as an Emergency Stop Switch would be between the Triac Phase and Mains Phase<BR>
If there is both an Emergency Stop Switch and an Overfill Protection System, they should be wired in series so that either can interupt the Triac Phase in cas of an emergency 



Wires have standard colours which are shown. In case these colours are unclear, they are as
follows:<BR>
▪ Incoming mains phase: Brown<BR>
▪ Incoming mains neutral: Blue<BR>
▪ Incoming mains earth: Green/Yellow<BR>

![image](1.1.1_Mains_connections.png)

<BR>

# Comms connections
The comms I/O is controlled by the connections to the CI501 Comms board which is piggy backed on the Power Supply inside the flame-proof enclosure.<BR>

Refer to the following diagram for connecting RS485, RS232, Compac or Gilbarco pumps. The shown switch should be set to the desired setting.
<BR>
**NOTE** Ensure that SW200 (Switch 1) is set the required protocol

![image](2.1.5_CI501-Comms_board.png)

Switches 300, 302, and 303 are for RS485/RS232 Terminator application.
Use the following table to configure these switches. Switch 300 is for channel 1, and switches 302 and 303 are for channel 2.

![image](9.3.1_CI501_Dip_Switches.png)

# K-Factor Board

Both the Parameter switch and K-Factor switch are found on the K-Factor board. Meters and air switches are also connected to this board. See below for the location of these.

![image](2.1.3_Kfactor_board.png)

<font size ="6">

# Terminal Board connections

STANDARD WIRING OF C5000 PUMPS<BR>

<font size ="3">

• Wire the triac(s) to the terminal board to the correct terminals using 0.75𝑚𝑚2 coloured wires.<BR>
**NOTE:** triac Gate terminal is the narrower spade.<BR>

• Use these diagrams to wire the pump motors and solenoids.

<BR>

# MR40P, MR80P, L40P, L80P

![image](1.7.1_Terminals_MR40P,MR80P,L40P,L80P.png)

<BR>

# MR160P, L160P

![image](1.7.2_Terminals_MR160P,L160P.png)

**NOTE:** Motor furthest from the dispenser outlet (usually side B) has the modified pump control valve and this motor is wired to ‘TB6’ on the terminal board.
 
<BR>

# MMR40P, MMR80P, LL40P, LL80P, L40PD

![image](1.7.3_Terminals_MMR40P,MMR80P,LL40P,LL80P,L40PD.png)

NOTE: A ‘Laser L40PD’ has two Motor Triacs, but only has one Motor (Motor Side A). Motor Output terminals are looped 'TB6' & 'TB7' with 0.75mm2 White appliance wire;<BR>
Connect the Motor & 'Loop' Wire to 'TB7' using a ferrule.

<BR>

# MMR80-40P,LL80-40P

![image](1.7.4_Terminals_MMR80-40P,LL80-40P.png)

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
| Preset cutoff         |                     | **PcA***.** or **Pcb***.** |This is available if a secondary solenoid is wired in
| Preset rounding       |                     | **PrLA***.** or **PrLb***.** **PrHA***.** or **PrHb***.**|
| Flow time out         |                     | **n-A** *** or **n-b** ***                    |


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

# Changing the Pump Number
If the parameter switch is continually depressed, the following menu to change the pump number will appear.<BR>
Each side must be numbered between 1-99. Entering a pump number 0 will disable the pump.<BR><BR>
To change the pump number, depress the parameter switch repeatedly until the following display is shown.<BR>
To increment a digit, press and hold the parameter switch when the desired digit is flashing. Repeat this procedure for side B if applicable.

![image](4.1.2_Parameter_pump_number_PnA.png)

# Changing the Price
The price must be set before the dispenser can be used, otherwise an error will be returned. Set the price in dollars per litre.<BR>

To change the price, depress the parameter switch repeatedly until the following display is shown. To increment a digit, press and hold the parameter switch when the desired digit is flashing. Repeat this procedure for side B if applicable.

![image](4.1.3_Parameter_price_PA.png)

# Standalone Mode
In standalone operation, the dispenser will continue working when not connected to a controller. When in Standalone mode no authorisation of fills is required and so fills are simply initiated by removing the refuelling assembly from its holder. If standalone operation is inhibited, the dispenser will not work in standalone mode, regardless of whether the dispenser is ONLINE to a controller or not.<BR> <BR>
The dispenser ceases to work in standalone mode if connected to a controller, regardless of the position of standalone setting.<BR><BR> 
Generally, on retail forecourts the dispenser should be set-up for standalone operation.  Hence, if the forecourt controller breaks down the dispensers can be set to work in standalone mode simply by turning them off then on again. <BR><BR>
For unattended refuelling sites, the dispensers should not be able to work in standalone mode in the event of a controller failure. Therefore, the dispenser should be set-up to inhibit standalone operation. <BR><BR>
This is set in the b code on the K factor switch. The b code to run Standalone without Dispenser Controller is 1000.  The b code to inhibit Standalone is 0000.

![image](4.1.13_Parameter_Preset_bA.png)

# Notes

# Pump Controller
If the pump is connected to a Point of Sale (POS) or a Compac Controller such as a PT1, check that pump data and transaction information is being correctly uploaded to it.<BR>
Ensure that the Contoller is sending the correct price to the Dispenser<BR>
Refer to the controller manual for specific instructions regarding connection and setup.

# Spare Fuses
In the event of a fuse blowing on the C5000 Power supply a bag of 3 is included in each flameproof box.<BR>
Any fuses used from this bag should be replaced.<BR>
NOTE: There are three different ratings used. If replacing a fuse, ensure that the correct value is used. 

# Precautions if using Generator Power
The power output from onsite generators can cause power spikes that may damage electrical components within the cabinet. When connecting to sites powered by generators, please take the following precautions:
1.	Install a power conditioner. Although generators are fitted with power regulators, most are not filtered sufficiently for powering sensitive electrical components. We recommend installing a commercial power conditioner and/or UPS between the generator and the unit.
2.	Before starting a generator, make sure the power to the unit is turned off. Start the generator, let the generator reach stable operating speed and wait 30 seconds before reconnecting the power to the unit.
3.	For units where the generator starts and stops on demand, install a delay timer or PLC to automatically isolate the unit until the operating speed and consistent power output is achieved.
4.	Isolate the unit before shutting down the generator.

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
