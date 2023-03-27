import pyodbc
import decimal


login = 'alex_chon1'
pw = 'MIS4322student'
cn_str = (
    'Driver={SQL Server Native Client 11.0};'
    'Server=MIS-SQLJB;'
    'Database=School;'
    'UID='+login+';'
    'PWD='+pw+';'
)
#connect to server
cn = pyodbc.connect(cn_str)
cursor = cn.cursor()











'''
1)
Calculate the new budget for each department. Every department will be getting a 10% increase in their budget except for 
the Information Systems (IS) and Computer Science (CS) departments. The IS department gets a 20% increase and the 
CS department gets a 15 % increase. Create a well formatted report that shows each department name, their 
current budget, their new budget and the amount increased.
'''

'''
Dept Name				Original Budget		New Budget		Increse in Budget
Engineering				$350,000.00			$385,000.00		$35,000.00
English					$120,000.00			$132,000.00		$12,000.00
Economics				$200,000.00			$220,000.00		$20,000.00
Mathematics				$250,000.00			$275,000.00		$25,000.00
Information Systems		$375,000.00			$450,000.00		$75,000.00
Computer Science		$310,500.00			$357,075.00		$46,575.00
'''


cursor.execute ('SELECT DepartmentID, Name, Budget, StartDate, Administrator FROM dbo.Department')
# for row in cursor.fetchall():
#     print(row)
dept_budgets = cursor.fetchall()

# Define a dictionary to store the budget increase percentages for each department
budget_increase_perc = {
    'Information Systems': 0.2,
    'Computer Science': 0.15,
    'Engineering': 0.1,
    'English': 0.1,
    'Economics': 0.1,
    'Mathematics': 0.1
}

# Define an empty list to store the results
results = []

# Loop through the query results and calculate the new budget for each department
for row in dept_budgets:
    dept_name = row[1]
    original_budget = decimal.Decimal(row[2])
    increase_perc = decimal.Decimal(budget_increase_perc[dept_name])
    new_budget = original_budget * (1 + increase_perc)
    increase = new_budget - original_budget
    results.append((dept_name, original_budget, new_budget, increase))

# Print the results in a well-formatted table
print('{:<25}{:<20}{:<20}{}'.format('Dept Name', 'Original Budget', 'New Budget', 'Increase in Budget'))
for row in results:
    print('{:<25}${:<19.2f}${:<19.2f}${:<.2f}'.format(row[0], row[1], row[2], row[3]))

# Close the cursor and connection





'''

2)
Display First Name, Last Name and corresponding personal and work email
for STUDENTS ONLY using Person and Contact_Info tables as shown below (only first row shown):


firstname	lastname	Personal Email					Work Email
Gytis		Barzdukas	josephine_darakjy@darakjy.org	ezekiel@chui.com
Peggy		Justice		art@venere.org					wkusko@yahoo.com
Yan			Li			lpaprocki@hotmail.com			bfigeroa@aol.com
Laura		Norman		donette.foller@cox.net			ammie@corrio.com
Nino		Olivotto	simona@morasca.com				francine_vocelka@vocelka.com
'''

# cursor.execute('select name, budget from school.dbo.department')
# data1 = cursor.fetchall()
# for x in data1:
#     print(x)






'''
3)
Display First Name, Last Name and corresponding home,cell and work phone numbers
for instructors only using Person and Contact_Info tables as shown below (only first 2 rows shown):

FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone
Kim			Abercrombie		(504) 621-8927	(410) 621-8927	(313) 621-8927
Fadi		Fakhouri		(810) 292-9388	(215) 292-9388	(815) 292-9388

'''



