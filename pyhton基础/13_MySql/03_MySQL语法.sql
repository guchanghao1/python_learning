-- 1、创建数据库
-- 2、创建空表 -- 设置它的字段和数据类型
-- 3、数据操作 -- 数据增删改查



一 -- 数据库操作
    1 -- 登录MySQL:     找到安装路径: D:\MySQL\mysql-8.0.23-winx64\bin --> 地址中: cmd
    mysql -u root -p
    2 -- 退出MySQL
    exit;

--     创建：CREATE DATABASE 数据库名字 CHARSET = utf8;
--     查询：SHOW DATABASES;
--     删除：DROP DATABASE 数据库名字;
--     使用：USE DATABASE;

    3 -- 新建数据库        charset=utf8： 写入中文
    创建    数据库   名字    字符
    CREATE DATABASE 数据库 CHARSET=utf8;
    CREATE DATABASE student charset=utf8;

    4 -- 使用数据库：use 数据库的名字
        使用数据库
        use  名字
        use student
    5 -- 查看所有数据库
    show DATABASES;

    6 -- 删除数据库：drop database 数据库名
    drop database 数据库名

    7 -- 总结：MySQL不区分字母大小写，不看格式，只认';',出现';'本行代码就结束


二 -- 数据表操作
--     删除每一行进行的是数据操作
--     删除每一列进行的是数据表操作

--     创建：CREATE TABLE 表名(字段名 数据类型 约束条件);

--     修改1：ALTER TABLE 表名 MODIFY 要修改字段名的 类型或者约束条件;
--     修改2：ALTER TABLE 表名 CHANGE 要修改的原字段名 新名字 类型和约束条件;

--     删除1：DROP TABLE 表名;
--     删除2：ALTER TABLE 表名 DROP 字段名;



    --查看当前数据库中所有表     字段结构: 字段名 数据类型 约束条件【可以省略】
    1 -- 常见表数据类型
        -- int  		 整型
        -- varchar()     字符串
        -- enum()      	 枚举
        -- date()        日期

 	2 -- 常见表约束条件
        -- auto_increment   自增
        -- not null         非空
        -- primary key      主键

 	3 -- 创建表：create table 表名(字段名 数据类型 约束条件)
        a -- 创建classes表(id、name)
        b -- 创建students表(id, name, age, height, gender)
        CREATE TABLE students
            (
            id   int   PRIMARY KEY auto_increment,
            name VARCHAR(50) ,
            age  INT,
            height int,
            gender enum('男','女')
            );

 	4 -- 修改表-新增字段--alter：table 表名 add 列名 类型及约束;
        a -- 添加birth字段到最后                最后--默认
        ALTER TABLE students add birth VARCHAR(50);
        b -- 添加score字段到第1列           首列--first
        --  ALTER TABLE students add addr2 VARCHAR(255) first;
        ALTER TABLE students ADD score3 VARCHAR(50) FIRST;
        c -- 添加phone字段到name的后面      name的后面 -- after name
        ALTER TABLE students add phone1 VARCHAR(50) AFTER name;

 	5 -- 修改表-修改字段：
         a -- 修改列类型及约束: alter table 表名 modify 列名 类型及约束;
         ALTER TABLE students modify age VARCHAR(50);
         b -- 修改列名: alter table 表名 change 原名 新名 类型及约束;
         ALTER TABLE students CHANGE age 年龄 VARCHAR(50);

 	6 -- 删除
        a -- 删除字段：alter table 表名 drop 列名;
        ALTER TABLE students DROP addr2;
        ALTER TABLE students DROP score3;
        ALTER TABLE students DROP phone1;
        ALTER TABLE students DROP birth;
        b -- 删除表：drop table 表名;
        DROP TABLE classes;


三 -- 数据操作

-- 数据操作部分：
-- 	插入：INSERT INTO 表名 VALUES();
--         插入的值要与表的字段数量一致（数据类型要一致）

-- 	修改：UPDATE  表名 SET 需要修改的字段;

-- 	删除: DELETE FROM 表名 WHERE 条件;

-- 	查询: SELECT  字段名  FROM 表名 WHERE 条件;
--         SELECT id,name FROM students;
--         不管进行了 求和 求平均数  不会在原表进行改变，只会出结果



1 -- 增 全字段插入
    a - insert into 表名 values (...);
		INSERT into students VALUES(1,'小明',18,180,'男');
		INSERT INTO students VALUES(0,'小丽',18,170,2);
		INSERT INTO students VALUES(4,'小红',20,175,2);

    b -- 多行插入

		INSERT INTO students VALUES
			(0, '小月月', 18, 180, 2),
			(0, '王语嫣', 29, 185, 1);
			(0, '李丽', 22, 165, 2),
			(0, '赵四', 30, 182, 1),
			(0, '周晓雯', 28, 168, 2),
			(0, '陈明', 35, 175, 1),
			(0, '林小玉', 19, 160, 2),
			(0, '孙建国', 45, 178, 1),
			(0, '杨紫琪', 26, 170, 2),
			(0, '吴浩', 31, 185, 1);

4 -- 查
    a -- 基本查询
        -- 查询所有学生信息   *： 所有字段
        查询   字段  在  表格
        SELECT * FROM students;

        -- 查询指定列 -- id, age, name
        SELECT id,年龄,name FROM students;

        -- 可以用as设置别名：select 字段1 as 别名1, 字段2 as 别名2 from 数据表名 where ...;
        SELECT name AS 姓名,height AS 身高 FROM students;

        -- 消除重复行： distinct
        SELECT DISTINCT 年龄 FROM students;

    b -- 条件查询
    1 -- 比较运算符:select ... from 表名 where ...
             -- 查询等于(=) 18岁的信息
             SELECT * FROM students WHERE 年龄 =18;
             SELECT id,name,年龄 FROM students WHERE 年龄 =18;
             -- 查询大于(>) 18岁的信息
             SELECT * FROM students WHERE 年龄 > 18;
             -- 查询小于30(<) 岁的信息
             SELECT * FROM students where 年龄 <30;
             -- 查询不等于18(!=) 岁的信息
             SELECT * FROM students WHERE 年龄 != 18;

    2 -- 逻辑运算符
             -- 18岁到28之间的所有学生信息 (and)
             SELECT * FROM students WHERE 18 <= 年龄 and 年龄 <= 28;
             -- 18岁以上的女生信息
             SELECT * FROM students WHERE 年龄 = 18 and gender = "女";
             -- 查看18岁以上 或者 身高大于170的男生 (or)
             SELECT * FROM students WHERE 年龄 > 20 or (height >170 AND gender = 1);
             SELECT * FROM students WHERE 年龄 > 20 or (height >170 AND gender = "男");
             -- 不在38岁以上的女生的信息 (not)
             SELECT * FROM students WHERE 年龄 <38 AND gender = 2;

c -- 范围查询
		1 -- in(1, 3, 8)表示在一个非连续的范围内  --离散
            -- 查询 年龄为18, 35, 45的同学信息
            SELECT * FROM students WHERE 年龄 in(18,35,45);


		2 -- not in 不连续的范围之内
            -- 查询 年龄不在18, 27, 34的同学信息
            SELECT * FROM students WHERE 年龄 not in(18,35,45);

		3 -- between ... and ... 表示在一个连续的范围内   -- 连续
            -- 查询 年龄是18~34之间的同学信息
            SELECT * FROM students WHERE 年龄 BETWEEN 18 and 34;
            SELECT * FROM students WHERE id BETWEEN 5 and 9;

		4 -- not between ... and ... 表示不在一个连续的范围内
            -- 查询 年龄不是18~34之间的同学信息
            SELECT * FROM students WHERE 年龄 not BETWEEN 18 and 34;



	e -- 聚合    聚合函数
			-- count 总数：查询有多少男生,多少女生
			SELECT count(*) FROM students WHERE gender = 1;
			SELECT count(*) FROM students WHERE gender ="女";

			-- count 总数：查询学生总数
			SELECT count(*) FROM students;

			-- max 最大值：查询最大的年龄
			SELECT max(年龄) FROM students;

			-- max 最大值：查询女生年龄最大的
			SELECT MAX(年龄) FROM students WHERE gender =2;

			-- min 最小值：查询最小的年龄
			SELECT min(年龄) FROM students;

			-- sum 求和：计算所有男生的年龄
			SELECT sum(年龄) FROM students WHERE gender =1;

			-- avg 平均值：计算男生平均年龄
			SELECT avg(年龄) FROM students WHERE gender =1;

			-- round(num, 2) 保留2位小数：计算女生平均年龄,保留2位小数
			SELECT round(avg(年龄),2) FROM students WHERE gender =2;
			SELECT round(avg(年龄),2) FROM students WHERE gender =1;

    g -- 分页: limit start[起始下标], count[个数] 限制查询出来数据的个数      下标从0开始
        -- 查询前5个数据
        SELECT * FROM students limit 0,5;

        -- 去获取 名字中紫的数据
        SELECT * FROM students WHERE name like "%丽";

    h -- 子查询   嵌套查询
        -- 查询出高于平均年龄的信息
        SELECT * FROM students
        WHERE age > (
        SELECT AVG(age) FROM students
        );

        -- 查询年龄最大的男生信息
        SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students WHERE gender = '女') and gender = '女' ;

    d -- 排序
        1 -- order by 单个字段（默认：从小到大排序, 省略了asc）  asc--从小到大  desc--从大到小
            -- 查询年龄在18~34之间的男性,年龄从小到大排序
            SELECT * FROM students WHERE age BETWEEN 18 AND 34 AND gender=1 ORDER BY age ASC;

            -- 查询年龄在18~34之间的女性,身高从大到小排序
            SELECT * FROM students WHERE age BETWEEN 18 AND 34 AND gender=2 ORDER BY age desc;

        2 -- order by 多个字段,用逗号隔开    -- 往后写就对了
            -- 查询年龄在18到34岁之间的女性,身高从大到小排序,如果身高相同情况下按照ID大小排序
            SELECT * FROM students WHERE age BETWEEN 18 AND 34 AND gender=2 ORDER BY height desc,id DESC;

            -- 按照年龄从小到大排序,身高从大到小排序
            SELECT * FROM students ORDER BY age asc, height DESC;


    f -- 分组
        1 -- group by
                -- 按照性别分组
                SELECT gender,count(*) AS 人数 FROM students GROUP BY gender;

                -- 计算男性的人数
                SELECT gender,count(*) AS 人数 FROM students WHERE gender =1 GROUP BY gender;

                -- 查询每种性别中最大的年龄
                SELECT gender, MAX(age) FROM students GROUP BY gender;


                -- 查询每种性别的平均年龄,并且保存2位小数
                SELECT gender, ROUND(avg(age),2) FROM students GROUP BY gender;


        2 -- group_concat(...)  把所需的字段 分成一个组
                -- 查询同种性别中的学生姓名
                SELECT gender,group_concat(name) FROM students GROUP BY gender;
        3 -- having
                -- 查询年龄人数超过2人得年龄,并显示其名字
                SELECT age, group_concat(name) FROM students GROUP BY age HAVING COUNT(age) > 1;


		-- 查询平均年龄超过30岁的性别,having avg(age)>30
		SELECT gender, avg(age)
		FROM students GROUP BY gender
		HAVING avg(age)>30;



2 -- 改: update 表名 set 列1=值1, 列2=值2, 列3=值3 ... where 条件判断;
    a -- 所有学生的身高修改成170

		UPDATE students SET height =170;
    b -- 将id为2的学生性别修改成男
		UPDATE students SET gender = 1 WHERE id = 2;

    c -- 将id为5的学生,名字修改成张三,性别修改成男
		UPDATE students SET name = '张三', gender = 1 WHERE id = 5;



3 -- 删:delete from 表名 where 条件;
     a -- 删除名字是张三的学生
		 DELETE FROM students WHERE name = "张三";

     b -- 删除id<4的学生
		 DELETE FROM students WHERE id < 7;

