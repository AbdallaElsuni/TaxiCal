# TaxiCal  

TaxiCal is an open-source **federal tax calculator** that calculates taxes based on income and marital status with **high accuracy** using the latest IRS tax brackets.  

## Features  

### **✅ Accurate Federal Tax Calculation**  
- Uses **IRS tax brackets** for precise tax estimates.  
- Supports **automatic updates** via `FederalVariables.json`.  
- The app will detect, verify, and load the latest tax data if `FederalVariables.json` is placed in the same directory.  

### **🔐 Account System**  
- Users can create accounts with **auto-generated 16-digit IDs** and **8-digit passcodes**.  
- Credentials are stored in a **secure JSON-based database**.  
- The **Account Manager** (found under **Account Actions** in the top-left menu) allows users to:  
  - Change their passcode.  
  - Delete their account.  

### **🌍 State Tax Support (Upcoming)**  
- The **Classes.py** module already includes an algorithm for **state tax calculations**.  
- California's tax brackets are preconfigured as an example.  
- Users can add other states by following the same pattern.  
- For states **without income tax**, set:  
  - One bracket from **0 to infinity** with a **0% rate**.  
  - `"StateBiggestSealOrder"` to `1`.  
- **State tax GUI will be added in the 6.0 update.**  

## Installation  
1. **Download** the latest release from [Releases](https://github.com/AbdallaElsuni/TaxiCal/releases).  
2. Place `FederalVariables.json` in the same directory (rename it to Variables.json if for 5.0 version and older) for **updated IRS tax brackets**.  
3. Run:  
   - **Windows**: `TaxiCal.exe`  
   - **Linux/Mac**: `python TaxiCal.py`  

## License  
TaxiCal is released under the **MIT License**.  

## Contributing & Issues  
- Feel free to contribute by adding state tax data!  
- Report issues in the [Issues](https://github.com/AbdallaElsuni/TaxiCal/issues) section.  

📌 **GitHub Repository:** [TaxiCal](https://github.com/AbdallaElsuni/TaxiCal)  
