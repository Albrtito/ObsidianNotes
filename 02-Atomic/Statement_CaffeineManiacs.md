**LEYENDA:**
+ <span style="background:#ff4d4f">RED: Non-Observed Explicit semantics</span>
+ <span style="background:#40a9ff">BLUE: Implicit semantics</span>
+ <span style="background:#d3f8b6">GREEN: No problem while implementation</span> 



The ecommerce company CaffeineManiacs TM Inc. needs a new database for recording and handling their data. In order to do this, they have made a specification about their services, providers and clients, as briefed in the following. 

The company has a

---
<span style="background:#d3f8b6">catalog of products, which are identified by their name (unique) and characterised by the coffea (that is, the species of coffee plant); the varietal (a variety of that coffea; there are many, such as Blue Mountain, Colombia, Bourbon, etc. ); the origin (the country where that coffee comes from); the roasting type, which can be ‘natural’, ‘high-roast’ (torrefacto), or ‘mixture’; whether it is decaf (decaffeinated) or not; </span>  : **creation of the product table**
**fields created: name(PK), coffea, varietal, origin, roastingtype, decaf(optional)**

---
<span style="background:#40a9ff">and the marketing formats available for each specific product: raw grain, roasted beans, ground, freeze-dried (soluble), in capsules, or prepared. Any product can be commercialized in several formats, and each format in turn can be packaged differing amounts (weight or volume, depending on the format).</span> : **formats are given in a table  and are referenced in the reference table, this was not implicitly told
formatTable(marketingFormat(PK), amount(PK))**

---
Any available <span style="background:#d3f8b6">reference is, therefore, an item identified by a bar-code, a packaging description (amount of product), and its retail prize. All references also have a certain number of available items for sale in our warehouses (stock)</span>. : **creation of the reference table: Fields created: (barcode(PK), retailPrice, stock,format(FK))**

<span style="background:#40a9ff">The packaging description is in the format table, then because each reference has a format it takes the packaging description from it</span>

--- 
<span style="background:#ff4d4f">Whenever a purchase is made, the available units of the involved references should be updated. When the available amount is less than a certain minimum threshold, a new replacement order will be automatically registered.</span>  : **this can be done manually but not automatically**


<span style="background:#d3f8b6">The minimum stock is, in general, different for each reference (by default, 5 units)</span>. : **part of the reference table, minimum stock is 5 by default: 
ReferenceTable: (barcode(PK), amount, retailPrice, stock, minStock(default:5))****

<span style="background:#ff4d4f">An automatic process is run daily (usually by night) for setting the existent ‘draft’ replacement orders, assigning them to a specific provider, recording the requested amount of units and order date, and finally updating the order date and time and setting the state to ‘placed’. </span> : **this can be done manually at nigh or with another program that works with the sql, however it cannot be set as a feature inside the sql code**
<span style="background:#40a9ff">:the only thing that is obtained from this is that the replacementOrder needs to have some status attribute</span>
**:replacementOrder:(status)

<span style="background:#fff88f">The requested units are calculated to attain a maximum threshold (that is, the maximum stock minus the current stock). </span> **: can this be done with a constraint?**

<span style="background:#ff4d4f">When the items of the replacement order are received, its row is updated with the correspondent receiving date, total (payment), and order state to ‘fulfilled’. </span> **: again something that cannot be updated in the sql**

<span style="background:#40a9ff"> however from this statement we get the implicit constraint  to know that for only one replacementOrder table, the payment and receivingDate must be optional</span>
**replacementOrder: (status, payment(optional), receivingDate(optional))**

<span style="background:#ff4d4f">There can be only one non-fulfilled (either draft or placed) replacement order per reference, and under no circumstances will more than one order be placed per day and reference. </span> : **this again cannot be checked with the sql, another external implementation would be needed** 
<span style="background:#40a9ff">:we now know that each order needs to have a reference that is being ordered</span>
**: replacementOrder(status, payment(optional),receivingDate(optional),reference)**

---
<span style="background:#affad1">When a new reference is inserted, the available stock is of course zero (unless the data operator who is inserting the row states explicitly something different).</span> **: the default value for stock in the reference table is 0: 
referenceTable(barcode(PK), amount, retailPrice, stock(default:0), minStock(default:5))**


<span style="background:#ff4d4f">Next time the automatic process is run, it will set the order for filling the stocks</span>**: this cannot be done, again same program that is in charge of updating the orders overnight should create new orders if needed.**

---
<span style="background:#d3f8b6">up to the maximum threshold (by default, 10 units higher than the minimum stock).</span> **: from this we can get that the maximumStock value for the reference table must have a default value of 10 more than the minimum stock.
<span style="background:#40a9ff">15 is the maximum default value</span>
ReferenceTable((barcode(PK), amount, retailPrice, stock(default:0), minStock(default:5)),maxStock(default:15)**

---
<span style="background:#ff4d4f">When placing each specific order, if at that moment there is no provider for that reference, the order will remain in ‘draft’ status. On the contrary, if there is more than one supplier for that reference, one will be chosen for that order. Specifically, the provider offering the lowest cost for the reference will be picked (if there are several tied offers, the supplier who has fulfilled their orders the fastest over the last year will be chosen; if they are still tied, the one with the fewest orders in the last year; if then still tied, anyone).</span> **:this is not something that can be done with sql as it is not a decision making software but a data managing one**

<span style="background:#40a9ff">**creation of an n to n relationship between provider and order. Each provider has n possible orders as well as an order canbe taken from n posible providers. Table name: provider_replacementOrder(provider(PK), replacementOrder(PK))**</span>

<span style="background:#40a9ff">now we know that each order needs a provider.</span>
**: replacementOrder(status, payment(optional),receivingDate(optional),reference, provider)**

---
<span style="background:#40a9ff">Draft orders can be deleted or updated (for increasing ‘quantity’). </span> **:this means draft orders have on delete do nothing? This does not make it so it is imposible to delete them**

<span style="background:#40a9ff">Already placed orders can’t be deleted, and shouldn’t be updated (except to set the delivery date and change its status).</span>
**:same thing as last implicit semantic, can this be done with an on delete condition?** #Duda 
<span style="background:#40a9ff">Fulfilled orders can’t be deleted or updated. </span>
**: same thing that last one. **

---
<span style="background:#d3f8b6">The suppliers (providers) have a unique name, CIF (tax id), salesperson’s full-name (cannot be repeated) and email (also univocal), phone number (unique) and commercial address (and, yes, it is unique as well).</span>
**:Creation of the provider table, an unique identifier CIF used as PK. 
provider(CIF(PK),salesperson(CK), email(CK),phoneNumber(CK), comercialAddress())**

---
<span style="background:#ff4d4f">If the provider is removed from the base, so will be all their supply lines (offers), but not the already fulfilled orders to them (which will be kept without a value for provider).</span>
**: this could be implemented as an on delete cascade but not with the difference in the state of the object.**

---
<span style="background:#d3f8b6">Besides, it is also needed to store the purchases placed by customers (our real business). An order is placed by a customer on a given date and set to a delivery address. </span>
 **: this creates a new table: purchase**
 **purchase(purchaseDate(PK), deliveryAddress(PK))**
 
<span style="background:#40a9ff"> The purchaseDate also holds time, so the primary key can be unique</span>
 
---
<span style="background:#40a9ff">They can set multiple purchases in the same day and to the same delivery address, but it will be processed as a single delivery (a delivery includes all orders of that day, and all items will be sent together).</span>
**: in order to use this part explicitly we would create a new table with the references and a connection to the purchase. However is better to have the reference in purchase
purchase(purchaseDate(PK), purchaseAddress(PK), delivery-PK))
delivery(PK)**

---
<span style="background:#d3f8b6">It is also important to record the billing data: type of payment (cash on delivery, bank transfer, credit card), payment date (charges to credit cards are always placed on the order’s date), and credit card data (in case).</span> 
**:This statement creates some new attributes inside the purchase table
purchase(purchaseDate(PK), deliveryAddress(PK), delivery-PK, billingType, billingDate, creditCardData)
This also states that we'll need a creditCardData table**

---
<span style="background:#d3f8b6">The delivery data is also essential: full address, and delivery date. </span>
**:this makes it so that we need to create a delivery table beforehand and now use the address and delivery date as PK. But to find all purchases going to a delivery an operation is still necessary. 
delivery(deliveryAddress(PK), deliveryDate(PK))**


---
<span style="background:#40a9ff">Finally, for each order there can be several items (one per purchased reference;</span>
**: This creates an N-N relation with the reference and purchase table**

---
<span style="background:#ff4d4f">in case that the customer buys more units of a certain product that had already purchased on the same day to the same shipping address, the new quantities will be added, keeping a single item line for that reference).</span>
**:this cannot be directly implemented with sql**

---
<span style="background:#d3f8b6">Apart from the reference, it is also required the quantity, unit retail price (in the order’s date)</span> and total price. 
**adding some attributes to the purchase table: 
purchase((purchaseDate(PK), deliveryAddress(PK), deliveryID, billingType, billingDate, creditCardData)**

---
<span style="background:#ff4d4f">If there is not enough stock of a given reference (when placing the item of an order), the quantity will be set to the maximum available, and a message will be generated to inform the user of such event. </span>
**:this cannot be directly implemented with sql**

---
<span style="background:#40a9ff">Our business distinguishes two types of clients: registered and non-registered clients.</span>
**:creation of a basic client table and a second table called resgisterdClient that holds more information
client()
registeredClient**

<span style="background:#d3f8b6">Registered clients have login data (unique username and password), </span> 
**: add to the registerdClient table some attributes
registeredClient(username(PK), password(PK))
REMARK: This should not be done if the data needs to be protected**

---
<span style="background:#d3f8b6">while non-registered clients can only be identified by their contact data (either the email or the phone, since both attributes are unique, and all purchasers will always provide at least one of them).</span>
**:create some attributes for the basic client table:
client(phone(PK)*,email(PK)*)
<span style="background:#40a9ff">The sql cannot check that we have either phone or mail</span>**

---
<span style="background:#d3f8b6">Regarding registered clients, apart from login data, we will keep their registration date and time; personal data (name and surname/s); contact information (phone and/or email); contact preference (email, phonecall, sms, whatsapp, facebook, wechat, qqmobile, snapchat, or telegram); their addresses</span><span style="background:#40a9ff"> (at least one address, and at most one address per client and town</span>);<span style="background:#d3f8b6"> their credit cards data; loyalty discounts; and, of course, all their purchases. </span>
**:this is just adding some other things to the registeredCient table
registeredCliente(username(PK),password(PK),registrationDateTime, name, surname, phone(FK),mail(FK), contactPreference,addresses,creditCardData)**

<span style="background:#40a9ff">The loyalty discounts and purchases have an attribute that identifies the client instead of there being an attribute in the client table. </span>


---
<span style="background:#40a9ff">Finally, non-registered users’ data or any data related thereto won't be kept, except that concerning legitimate interest: data related to the purchases, including the references and quantities, the buyer’s name and surname, shipping and billing addresses, payment data, credit card (in case), and relevant dates.</span>
**:All of this data is registered in the purchase, then if each purchase has an user it can be filtered from there.
adding an user attribute to the purchase table: 
purchase((purchaseDate(PK), deliveryAddress(PK), deliveryID, billingType, billingDate, creditCardData, billingAddress(FK), client(FK))
**



---
<span style="background:#ff4d4f">If a registered user wants to be deregistered, all their purchases will be converted (to anonymous buyer’s purchases) and then all data will be automatically deleted.</span>
**:this cannot be done directly. As it cannot be set to anonymous**

---
<span style="background:#d3f8b6">Data related to credit cards includes its cardholder, finance company, card number, and expiration date (only month and year); credit card numbers cannot be repeated, not even with different companies. </span>
**:direct creation of the creditCardData table
creditCardData(cardholder, financeCompany, cardNumber(PK),expirationDate)**

---
<span style="background:#d3f8b6">In another vein, any address has the thoroughfare’s type (street, square, circus, road…) and name, and may have gateway number, block number, stairs id, floor, and door. In addition, they always have ZIP code, town/city and country.</span>
**:direct creation of the address table
address(type, name, gateway*,block*,stairsID*,floor*,door*, ZIP,town, city, country)**

---
<span style="background:#d3f8b6">Loyalty discounts are generally calculated monthly and recorded as a ‘voucher’ including the percentage to be discounted (on each future purchase) and the date</span> 
<span style="background:#40a9ff">no need for the creation of the loyaltyDiscount table we directly add it into the registeredClient table as only registered clients can do this. </span>
**registeredClient(username(PK),password(PK),registrationDateTime, name, surname, phone(FK),mail(FK), contactPreference,addresses,creditCardData,discount, discountDate)**

---
<span style="background:#ff4d4f">(the voucher will only be valid for the following 30 days). That calculation follows a certain procedure (1% for every €10 purchased during the last 30 days, up to 10 times; plus the immediately previous discount divided by ten), and only current voucher is kept for each client.</span>
**This cannot be directly implemented**

---
<span style="background:#d3f8b6">Regarding the contact preference, it is set by default to sms (short message) if there is a phone number for that client,</span> <span style="background:#ff4d4f">and email otherwise. </span>
**: a default value for the contact preference can be set, however it cannot be done that else the mail should be taken:
registeredClient(username(PK),password(PK), registrationDateTime, name, surname, phone(FK),mail(FK), contactPreference(default = SMS) , addresses ,creditCardData)**



---
<span style="background:#d3f8b6">Last (but not least), users can post their opinions, ratings and comments on products and references (if the comment is set on a product, it is assumed to be valid for all formats; </span>
**:creation of the table comment: <span style="background:#40a9ff">By default it is over the product, but it can also me created over the reference so that the format is tracked</span>
comment(reference*, product)**


---

<span style="background:#40a9ff">otherwise, the format is specified). </span>
**The reference attribute is optional, if something is entered into the field it is valid for only that format.**

---
<span style="background:#d3f8b6">Comments have a score (a number from 1 to 5), a text, and can accumulate likes (supposed to be less than 1 billion, default zero)</span>.
**adding some attributes  to the comment table: 
comment(reference, format, likes(1billion to 0, default 0), text)**

registeredClient (username) is added to the comment table to identify who it is that posted the comment. 
**comment(reference* ,product, likes(1billion to 0, default 0), text, registeredClient(FK))**
<span style="background:#40a9ff">date and time of the comment are used as a primary key</span>
**comment(reference* ,product, likes(1billion to 0, default 0), text, registeredClient(FK)),dateTime)**

---
<span style="background:#d3f8b6">Comments can be tagged with an endorsement</span> <span style="background:#ff4d4f">if they come from a registered user who has consumed that product/reference previously. </span>
**: The creation of an endorsement as a bool value is possible, however the act of setting the endorsement to true or false cannot be done in sql**

---
<span style="background:#ff4d4f">If a user unsubscribes (is removed from the database) their comments remain, but anonymized (without link to any registered user). Unregistered customers cannot register any comments or ratings.</span>
**: a possible solution for this would be to create a default client called anonymous. However with the current implementation this cannot be done. **
