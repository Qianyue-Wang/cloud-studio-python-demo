import pandas as pd

# 读取Excel表格
df = pd.read_excel('salary.xlsx')

# 计算考勤扣除金额
def calculate_attendance_deduction(late_count):
    if late_count <= 3:
        return 0
    else:
        return (late_count - 3) * 100

# 计算个税
def calculate_income_tax(income):
    if income <= 3000:
        return income * 0.03
    elif 3000 < income <= 12000:
        return income * 0.1
    elif 12000 < income <= 25000:
        return income * 0.2
    elif 25000 < income <= 35000:
        return income * 0.25
    elif 35000 < income <= 55000:
        return income * 0.3
    elif 55000 < income <= 80000:
        return income * 0.25
    else:
        return income * 0.45

# 对每一行数据进行计算
df['考勤扣除金额'] = df['迟到次数'].apply(calculate_attendance_deduction)
df['税前工资'] = df['工资基数'] - df['五险一金扣除'] - df['考勤扣除金额']
df['个税扣除'] = df['税前工资'].apply(calculate_income_tax)
df['实发工资'] = df['税前工资'] - df['个税扣除']

# 更新Excel表格中的相关列
with pd.ExcelWriter('salary.xlsx') as writer:
    df.to_excel(writer, index=False)

# 打印整体数据
print(df)