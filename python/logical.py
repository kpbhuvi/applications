#if applicant has high income and good score
#Eligible for loan

has_high_income = False
has_good_score = True
has_criminal_record = True

if has_high_income and has_good_score:
    print("eligible for loan")

print("not eligible for loan")

if has_high_income or has_good_score:
    print("eligible for loan")

#print("not eligible for loan")

#If applicant has good credit and doesnt have criminal record then eligible for criminal record

if has_good_score and not has_criminal_record :
    print("eligible for loan")

print("Not eligible for loan")