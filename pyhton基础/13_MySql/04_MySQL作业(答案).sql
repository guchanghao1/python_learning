"""
表结构：员工表 (id, 名字, 部门, 薪资)
    CREATE TABLE 员工表 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    名字 VARCHAR(50) NOT NULL,
    部门 VARCHAR(50),
    薪资 INT
);

1、问题： 查询所有员工的姓名和工资
    SELECT name, salary FROM employees;

2、问题： 查询工资大于5000的员工信息
    SELECT * FROM employees WHERE salary > 5000;

3、问题： 按工资降序排列员工信息
    SELECT * FROM employees ORDER BY salary DESC;

4、问题： 查询工资最高的3名员工
    SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

5、问题： 计算所有员工的平均工资
    SELECT AVG(salary) as avg_salary FROM employees;

6、问题： 统计每个部门的员工数量和平均工资
    SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department;

7、问题： 查询姓名以'张'开头的员工
    SELECT * FROM employees WHERE name LIKE '张%';
"""


"""
表结构：students()
# CREATE TABLE students (student_id,name,age,gender,class,score)
#     student_id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     age INT,
#     gender ENUM('男', '女'),
#     class VARCHAR(50),
#     score DECIMAL(5,2)
# );

-- 插入测试数据
INSERT INTO students (name, age, gender, class, score) VALUES
('张三', 18, '男', '一班', 85.5),
('李四', 19, '男', '二班', 92.0),
('王五', 18, '女', '一班', 88.5),
('赵六', 20, '女', '三班', 76.0),
('钱七', 19, '男', '二班', 95.5),
('孙八', 18, '女', '一班', 82.0);

问题1：查询所有学生信息
SELECT * FROM students;

问题2：查询学生姓名和成绩
SELECT name, score FROM students;

问题3：查询成绩大于90分的学生
SELECT * FROM students WHERE score > 90;
问题4：查询一班的所有女生
SELECT * FROM students WHERE class = '一班' AND gender = '女';

问题5：按成绩从高到低排序
SELECT * FROM students ORDER BY score DESC;

问题6：查询成绩前三名的学生
SELECT * FROM students ORDER BY score DESC LIMIT 3;

问题7：按班级分组，按成绩降序排列
SELECT * FROM students ORDER BY class, score DESC;

问题8：统计学生总人数
SELECT COUNT(*) as total_students FROM students;

问题9：计算平均成绩
SELECT AVG(score) as avg_score FROM students;

问题10：查询最高分和最低分
SELECT MAX(score) as max_score, MIN(score) as min_score FROM students;

问题11：统计每个班级的学生人数
SELECT class, COUNT(*) as student_count
FROM students
GROUP BY class;

问题12：查询平均分超过85分的班级
SELECT class, AVG(score) as avg_score
FROM students
GROUP BY class
HAVING AVG(score) > 85;

问题13：查询姓'张'的学生
SELECT * FROM students WHERE name LIKE '张%';

问题14：将学生姓名转换为大写
SELECT UPPER(name) as upper_name, score FROM students;

问题15：查询姓名长度为2的学生
SELECT * FROM students WHERE LENGTH(name) = 2;
"""




