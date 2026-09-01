import matplotlib.pyplot as plt

# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# visitors = [120, 150, 180, 200, 170, 220, 250]

# plt.plot(days, visitors,marker='o',color='blue', linestyle=':', linewidth=2)
# plt.title("Website Visitors Over a Week")
# plt.xlabel("Days")
# plt.ylabel("Number of Visitors")
# plt.show()


# products = ["Phone", "Laptop", "Tablet", "Headphones"]
# sales = [50, 30, 20, 40]

# plt.bar(products, sales)
# plt.title("Product Sales")
# plt.xlabel("Products")
# plt.ylabel("Units Sold")
# plt.grid(True)
# plt.show()

# hours = [1,2,3,4,5,6,7,8]
# marks = [50,55,60,65,70,75,80,85]

# plt.scatter(hours, marks)
# plt.title("Hours vs Marks")
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.show()


# ages = [18,19,20,21,18,22,23,19,20,21,22,18]

# plt.hist(ages, bins=5)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

labels = ["Rent","Food","Travel","Entertainment"]
amounts = [40, 25, 20, 15]

plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()
