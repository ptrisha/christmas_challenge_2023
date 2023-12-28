# Pandas problem Day 26
# Problem description:
# https://leetcode.com/problems/students-and-examinations/

# A very unoptimized version.  I found the problem very 
# challenging.

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
   
    merge1 = students.merge(subjects, how="cross")

    merge2 = examinations.merge(students, how="left", on="student_id")
    group2= merge2.groupby(by=["student_id", "subject_name"], as_index=False).size()

    merge3 = merge1.merge(group2, how="left", on=["student_id", "subject_name"])
    merge3["size"]= merge3["size"].fillna(0)

    merge3.sort_values(by=["student_id", "subject_name"], inplace=True)
    merge3.rename(columns={"size": "attended_exams"}, inplace=True)
    merge3 = merge3[["student_id", "student_name", "subject_name", "attended_exams"]]

    return merge3
