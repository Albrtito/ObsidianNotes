---

kanban-plugin: basic

---

## Requirements

- [ ] GE2-P2-FR-02: Identify with ID and provide credit card number. Info in JSON. Create code. (not needed to record the code)
- [ ] GE-P2-FR-02-I1: Path to JSON.
- [ ] G2-P2-FR-02-P1: Verify stored and OrderID matches the data. Not manipulated
- [ ] G2-P2-FR-02-P1.1: Verify existence of localizer in reservation file. Data matches
- [ ] G2-P2-FR-02-P1.2: If verified.Create instance of HotelStay.
- [ ] G2-P2-FR-02-P2: All data stored (of correctly processed things)
- [ ] G2-P2-FR-02-O1: SHA-256 string with an hex key if correct data.
- [ ] G2-P2-FR-02-O2: File with the processed stays
- [ ] G2-P2-FR-02-O3: EXCEPTIONS (HotelManagementException)<br>- Data file cannot be found<br>- The file is not in JSON format<br>- The JSON does not have the expeected structure<br>- the JSON data does not have valid values<br>- The locator does not correspond to the the stored data<br>- The arrival date does not correspond to the reservation date<br>- Internal processing error while obtaining the key


## TestsCases



## To-Do



## Developing

- [ ] Read all documentation
- [ ] Create Pylint 5 rules


## Done





%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%