
![image](logos.png)


<font size="5">

# KG100 Standalone Meter Display Manual  

Updated 6 May 2026


**Conditions of Use**  

<font size="3">

Please read this manual completely before working on, or making adjustments to Compac equipment

Compac Industries Limited accepts no liability for personal injury or property damage resulting from working on or adjusting the equipment incorrectly or without authorization.

Along with any warnings, instructions, and procedures in this manual, you should also observe any other common sense procedures that are generally applicable to equipment of this type.

Failure to comply with any warnings, instructions, procedures, or any other common sense procedures may result in injury, equipment damage, property damage, or poor performance of the Compac equipment

The major hazard involved with operating the Compac C5000 is electrical shock. This hazard can be avoided if you adhere to the procedures in this manual and exercise all due care.

Compac Industries Limited accepts no liability for direct, indirect, incidental, special, or consequential damages resulting from failure to follow any warnings, instructions, and procedures in this manual, or any other common sense procedures generally applicable to equipment of this type. The foregoing limitation extends to damages to person or property caused by the Compac C5000 processor, or damages resulting from the inability to use the Compac C5K processor, including loss of profits, loss of products, loss of power supply, the cost of arranging an alternative power supply, and loss of time, whether incurred by the user or their employees, the installer, the commissioner, a service technician, or any third party.

Compac Industries Limited reserves the right to change the specifications of its products or the information in this manual without necessarily notifying its users.

Variations in installation and operating conditions may affect the Compac C5000 processor's performance. Compac Industries Limited has no control over each installation's unique operating environment. Hence, Compac Industries Limited makes no representations or warranties concerning the performance of the Compac C5000 processor under the actual operating conditions prevailing at the installation. A technical expert of your choosing should validate all operating parameters for each application.

Compac Industries Limited has made every effort to explain all servicing procedures, warnings, and safety precautions as clearly and completely as possible. However, due to the range of operating environments, it is not possible to anticipate every issue that may arise. This manual is intended to provide general guidance. For specific guidance and technical support, contact your authorised Compac supplier, using the contact details in the Product Identification section.

Only parts supplied by or approved by Compac may be used and no unauthorised modifications to the hardware of software may be made. The use of non-approved parts or modifications will void all warranties and approvals. The use of non-approved parts or modifications may also constitute a safety hazard.

Information in this manual shall not be deemed a warranty, representation, or guarantee. For warranty provisions applicable to the Compac C5000 processor, please refer to the warranty provided by the supplier.

Unless otherwise noted, references to brand names, product names, or trademarks constitute the intellectual property of the owner thereof. Subject to your right to use the Compac C5K processor, Compac does not convey any right, title, or interest in its intellectual property, including and without limitation, its patents, copyrights, and know-how.

Every effort has been made to ensure the accuracy of this document. However, it may contain technical inaccuracies or typographical errors. Compac Industries Limited assumes no responsibility for and disclaims all liability of such inaccuracies, errors, or omissions in this publication.

## Table of Contents

<font size ="5">

[**1.0 Safety**](#10-safety)

<font size ="3">

<font size ="5">

[**2.0 Introduction**](#20-introduction)

<font size ="3">

<font size ="5">

[**3.0 Operation**](#30-operation)

[3.1 Zeroing the Meter](#31-zeroing-the-meter)

<font size ="3">

<font size ="5">

[**4.0 Drawings**](#40-drawings)

<font size ="3">


<font size ="5">

[**5.0 Mechanical assembly**](#50-mechanical-assembly)

<font size ="3">

<font size ="5">

[**6.0 Electrical connections**](#60-electrical-connections)

<font size ="3">

[6.1 Power Requirements](#61-power-requirements)

[6.2 Power connection](#62-power-connection) 

[6.3 RS485 MODBUS connection](#63-rs485-modbus-connection)

[6.4 Fuses](#64-fuses)

<font size ="5">

[**7.0 Calibration**](#70-calibration)

<font size ="3">

[7.1 Calibration Method 1](#72-calibration-method-2)

[7.2 Calibration Method 2](#72-calibration-method-2)

[7.3 Changing the K-factor of the KG100 Standalone Meter](#73-changing-the-k-factor-of-the-kg100-standalone-meter)

<font size ="5">

[**8.0 MODBUS Registers**](#80-modbus-registers)

<font size ="3">

<font size ="5">

[**9.0 Approvals**](#90-approvals)

<font size ="3">

[9.1 Electrical Certification](#91-electrical-certification)



<BR>

# 1.0 Safety

**DANGER PRECAUTIONS**<BR>

Please adhere to the following safety precautions at all times when working on Compac equipment.<BR>
Failure to observe these safety precautions could result in damage to the Meter, injury, or death.<BR>
Make sure that you read and understand all safety precautions before operating Compac equipment<BR>
Failure to take adequate safety precautions could result in explosion, injury and loss of life.

# 1.1 System Design
Ensure the system design does not allow the gas pressure to exceed its rating.<BR>
The KG100 Meter does not include any safeties to protect against excessive inlet pressure.<BR>
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

- Always turn off the power to the KG100 Standalone Meter before removing the box lid. Never touch wiring or components with power on.
- Never power up the CKG100 Standalone Meter with the flameproof box lid removed.
- Always turn off the power to the KG100 Standalone Meter upgrading or replacing components.
- Always take basic anti-static precautions when working on the electronics, i.e., wearing a wristband with an earth strap. 

# 2.0 Introduction

The Compac KG100 Standalone Meter.<BR>

![image](16.0_KG100_Standalone_Meter.png)

The KG100 Coriolis meter is an example of innovative Compac technology, designed and manufactured in our New Zealand facility using automated production methods to ensure precision measurement.

It exceeds OIML standards for accuracy and is rated for inlet pressures up to 350 bar.

**Benefits:**

- High speed processor and intelligent software guarantees accuracy and reliability

- Laser precision bends and computer controlled automated assembly provides unrivalled precision

- Heat treatment ensures zero point stability and prevents calibration drift

- SAE parallel thread fittings with o-rings prevent leaks<BR>

The Standalone version of the Compac KG100 Coriolis meter with a built-in display has been developed for metering CNG / Biogas in both Dispensing and applications other than vehicle filling.

Typical applications:<BR>
- Metering CNG / Biogas in a gas supply line with a non-resettable totaliser
- Master Meter for calibrating CNG dispensers with batch filling reset function

**Features:**

- Integrated 3-inch display which includes a non-resettable totalised and Batch fill function reset button

- Integrated Ex-rated junction box and power converter, allowing for either AC mains or a general purpose 12VDC power supply 

- Easy integration into existing systems with common Modbus RTU communication protocol

- Ultra low maintenance throughout the lifespan of the flow meter

|Specifications||
|-----|-----
|Nominal Flow Rate|0-100kg/min|
|Maximum inlet pressure|350bar|
|Temperature Range|-55C to +80C|
|Weight|Approx 4.1kgs|
|Accuracy|As per International Standard OIML R139 
|Material|All wetted parts Stainless Steel

<BR>

# 3.0 Operation

# 3.1 Zeroing the Meter

The KG100 Meter must be zeroed before every fill.
This is done remotely from the PLC using MODBUS (Compac to provide full details of the Register to use later) 

The Meter has two modes
- Zeroing Mode
- Normal Mode

You can see which mode the Meter is in by viewing the Display<BR>

The top line will display either<BR>
0 = The Meter is zeroing<BR>
kg/min = The Meter is in normal mode



# 4.0 Drawings

![image](MAD0116PRO_KG100_Standalone_Meter_Assembly_Page_1.png)

![image](MAD0116PRO_KG100_Standalone_Meter_Assembly_Page_2.png)

# 5.0 Mechanical assembly 

Assemble the Standalone Meter Power Supply on the Meter as per the MAD116PRO drawings in section 4  


# 6.0 Electrical connections 

All Electrical connections are made in the KG100 Display enclosure

The KG100 Display Enclosure consists of two sections


**Front IS section** 
This section is Intrinsically Safe.<BR>
It houses the LCD Dipslay and IS electronics<BR>

The lid is fixed to the housing with bolts which can be secured with a tamperproof wire calibration seal

Removing the lid gives access to the Dispatch/Idle Button switch which is used to change the K-factor of the Meter is case re-calibration of the KG100 Meter is required.  

The orientation of the Display can also changed by rotating it to suit the installation. 

**Back NON-IS section**
This section is NON-IS and allows access to the Mains, 12V and RS485 connections on the CI540 Power Module

Once the KG100 Standalone Meter has been commisioned, it should not be necessary to remove the NON-IS back cover during normal service.<BR>

**DANGER** *Do not operate the KG100 Meter without the NON-IS cover in place*<BR>

<BR>

# 6.1 Power Requirements

The KG100 Standalone Meter can be powered from either 230V Mains or 12VDC, depending on which is available.<BR>

Both connections are provided on the CI540 Power Module<BR>

**NOTE** There is no provision for powering the Standalone Meter from the C5000 Power Card.<BR>
In most applications for the Standalone Meter, there is no C5000 anyway as the Standalone Meter connects to other equipment

It is intended that an off the shelf, locally available 12VDC would be installed out of the zone and wired back to the Standalone Meter CI540 module

To connect the Power and RS485 MODBUS, remove the NON-IS back cover and wire as follows:

<BR>

# 6.2 Power connection 

**12VDC operation:** Connect to 12VDC to the terminals marked **+12V and E**<BR>

or

**230V mains operation:** Connect incoming 230VAC mains to the terminals marked **MAINS**

<BR>

# 6.3 RS485 MODBUS connection

Connect the RS485 cable from the PLC to **RS495 A and B**  

<BR>

**NOTE** Use appropriately rated glands to gland power and RS485 cables into the Display Enclosure

<BR>

![image](16.1.1_KG100SA_connections.png)

# 6.4 Fuses

The Fuses are located on the CI540 Power Module

# 7.0 Calibration

There are two Calibration methods

# 7.1 Calibration Method 1

**Method 1 – Calibrate with SA (Standalone) Module Installed<BR>**

Connect the SA module to the meter and use the SA display reading as the register value for calibration.<BR>

(This method may require a customised meter mount to be fitted on the test rig.)<BR>

- Connect the assembled SA meter to the test rig in the default orientation.<BR>
- Perform a gas test of the SA meter assembly on the test rig.<BR>
- Record all fill results on the KG100 Meter Test Sheet.<BR>
- Upon completion of calibration, generate and print the calibration test certificate.<BR>

# 7.2 Calibration Method 2

**Method 2 – Pre-test Meter on the C5K meter test rig before SA (Standalone) Module Installation**<BR>

Pre-test the meter on the test rig before connecting the SA module, then configure the K-factor.<BR>

- Prior to connecting the SA module, perform a gas test of the KG meter on the test rig.<BR>
- (Use the supplied C5K dispenser cable “BW-KG100-CI545”.)<BR>
- Record all fill results on the KG100 Meter Test Sheet.<BR>
- Upon completion of calibration, generate and print the calibration test certificate.<BR>
- After connecting the SA module to the meter, power on the unit and configure the K-factor.<BR>

# 7.3 Changing the K-factor of the KG100 Standalone Meter

- The lid of the Display Enclosure has provision for a tamper-proof wire seal
- To change the K-Factor, it is necesary to first cut the Calibration seal wire 
- Remove the Display enclosure lid
- Press the Dispatch/Idle button on the PCB.<BR>
- The first digit will flash
- Hold the button down while the first digit scrolls though. Release when the correct number appears<BR>
- Allow to reset
- Hold the Dispatch/Idle button down to move to the next digit.

Repeat the above until the K-Factor is set correctly

**NOTE** You can verify the K-Factor in the Meter by momentarily pressing the Dispatch/Idle button.<BR>
The K-Factor will be displayed.
Check the K-Factor and allow the Display to reset


# 8.0 MODBUS Registers

**Electrical interface** 

Communication is via 5V TTL RS485.  

**Communication protocol** 

The communication protocol is standard Modbus RTU with the following packet structure:  

|Start|Address|Function|Data|CRC|End| 
|---|---|---|---|---|---|
|>3.5 char|8 bits|8 bits|N * 8 bits|16 bits|>3.5 char| 


**Common Modbus registers**<BR>

Table 1 below contains commonly used registers when integrating the KG100 Meter (Integrable Meter) into a dispenser/controller system.<BR> The complete list of registers is available upon request.

Register|Type|Access|Designation 
-------|-----|-----|-----
0001|U16|RO|Processor Software Major 
0002|U16|RO|Processor Software Minor 
0003|U16|RO|Processor Software day | Software month 
0004|U16|RO|Processor Software year|
0005|U16|R/W|Modbus address 
0006|U16|RO|Secondary Processor Software Major 
0007|U16|RO|Secondary Processor Software Minor 
0008-0009|U16|RO|Unique ID 
0010|U16|RO|Runtime seconds 
0065|INT16|R/W|wStatus 
0066|INT16|RO|rStatus 
0070-0071|FLOAT|RO|VOL_FLOW 
0072-0073|FLOAT|RO|VOL_BATCH 
0074|U16|RO|Density 
0075|U16|RO|TEMPERATURE 
0076|U16|RO|cSTATUS 
0080-0081|FLOAT|RO|KG_FLOW 
0082-0083|FLOAT|RO|KG_BATCH 
0084|U16|RO|cDensity 
0085|INT16|RO|cTemperature
0129|U16|R/W|Pair ID 1 
0130|U16|R/W|Pair ID 2 
0132|U16|R/W|REQ Address 
0136|U32|R/W|K Factor (flow calibration factor) 
0138|INT16|R/W|Density offset 
0139|INT16|R/W|Temperature offset 
0142|U16|R/O|OWID EXT A 
0143|U16|R/O|OWID EXT B 
0144|U16|R/O|OWID EXT C 
0145|U16|R/O|OWID EXT D 
0146|U16|R/O|OWID INT A 
0147|U16|R/O|OWID INT B 
0148|U16|R/O|OWID INT C 
0149|U16|R/O|OWID INT D 
0176|FLOAT|R/W|Flow cutoff 

**Table 1 - Commonly used meter registers** 

Further registers to be added later including the register to zero the Meter

# 9.0 Approvals

# 9.1 Electrical Certification

The KG100 Standalone Meter Power Supply has the following Electrical Certification<BR>

IECEX Certificate of Conformity - IECEx ExTC 26.0002X Issue 0

This approval document is available to download from the Compac Website www.compac.co.nz
