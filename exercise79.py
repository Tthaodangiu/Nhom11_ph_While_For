import random
m_value = random.randint(1, 100)
update_count = 0
print(m_value)
for i in range(99):
    new_num = random.randint(1, 100)
    print(new_num)
    if new_num > m_value:
        m_value = new_num
        update_count += 1
        print(m_value,"<== Update")
print("The maximum value found was :",m_value)
print("The maximum value was updated",update_count,"times.")
