# SKARAB Firmware Analysis and Integration Time Study for BINGO Radio Telescope

This repository contains the data analysis and firmware evaluation work related to SKARAB FPGA firmwares used in the BINGO Radio Telescope project at UFCG.

### Project Overview

The **BINGO** (BArios INterferometer for Galactic Observations) Radio Telescope, located in Aguiar, Paraíba, Brazil, is an instrument designed for radio spectrometry and cosmological studies.

This project focuses on analyzing and optimizing SKARAB FPGA firmwares within the telescope’s signal processing pipeline. Using tools like Simulink, MATLAB, Vivado, and the CASPER toolflow, the work investigates the impact of the accumulation vector size (acc_len) and other parameters on integration time and firmware performance.

### Key Objectives

* Evaluate integration time and processing performance across multiple SKARAB firmware versions

* Analyze metrics such as average integration time and standard deviation over varying accumulation vector sizes

* Identify anomalies, synchronization issues, and firmware behaviors affecting stability and accuracy

* Utilize Python scripts for data extraction, statistical filtering, and visualization

### Tools and Technologies

* SKARAB FPGA platform for radio astronomy digital signal processing

* CASPER toolflow for FPGA design and deployment

* Simulink and MATLAB for modeling and simulation

* Vivado for FPGA synthesis and implementation

* Python (pandas, matplotlib) for data analysis and visualization
