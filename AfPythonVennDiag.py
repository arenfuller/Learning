project_users={'Ron','Jess', 'Frank', 'Phil'}
	      
admin_users={'Frank', 'Jess', 'Jack'}
	      
#Number of Users
	      
print(len(project_users))

#All Users
	      
print(project_users.union(admin_users))

#Users who are in both groups
print(project_users.intersection(admin_users))

#Project users who are not admin
print(project_users.difference(admin_users))

#Admin users not working on the project
print (admin_users.difference(project_users)) 
