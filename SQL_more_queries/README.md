      <div class="panel panel-default" id="project-description">

  <div class="panel-body">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/1tuxYhEv__bmrwkAicbjpA" title="How To Create a New User and Grant Permissions in MySQL" target="_blank">How To Create a New User and Grant Permissions in MySQL</a> </li>
<li><a href="/rltoken/PMozNP0LI2zJ-ycA-L6xoA" title="How To Use MySQL GRANT Statement To Grant Privileges To a User" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a> </li>
<li><a href="/rltoken/AHI2a6vFyr8h4LeI6xK96w" title="MySQL constraints" target="_blank">MySQL constraints</a> </li>
<li><a href="/rltoken/UvrRJYwhKKL-WcqdfR4ZTg" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/vZviDvoYzQSi5asDz-ZsqA" title="Basic query operation: the join" target="_blank">Basic query operation: the join</a> </li>
<li><a href="/rltoken/vjcpTEMrRJUOXIWBdzzlMg" title="SQL technique: multiple joins and the distinct keyword" target="_blank">SQL technique: multiple joins and the distinct keyword</a> </li>
<li><a href="/rltoken/s0sG5NqFN4nw4-k0KJNBbg" title="SQL technique: join types" target="_blank">SQL technique: join types</a> </li>
<li><a href="/rltoken/tv7XqDq1naSlqSz042VBjA" title="SQL technique: union and minus" target="_blank">SQL technique: union and minus</a> </li>
<li><a href="/rltoken/Qp6hXj5D3Cdeqi5Z-30sAw" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/o6faV44f8S34zW3FiO5Mgg" title="The Seven Types of SQL Joins" target="_blank">The Seven Types of SQL Joins</a> </li>
<li><a href="/rltoken/T3VjE1yBfwJcd1hDD4tItw" title="MySQL Tutorial" target="_blank">MySQL Tutorial</a> </li>
<li><a href="/rltoken/0NaQZjOUvQuWy0xGPhTkVw" title="SQL Style Guide" target="_blank">SQL Style Guide</a> </li>
<li><a href="/rltoken/R5KAnzO4iwYo2LgD3eKL8A" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a> </li>
</ul>

<p>Extra resources around relational database model design:</p>

<ul>
<li><a href="/rltoken/A81_Vk2TV-f_f5wG0HK6Zw" title="Design" target="_blank">Design</a></li>
<li><a href="/rltoken/cwgE_DVy7l3ap6lCVJsPZQ" title="Normalization" target="_blank">Normalization</a></li>
<li><a href="/rltoken/1JFNpSloiEAI7aLW2rnyKw" title="ER Modeling" target="_blank">ER Modeling</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/SXrjP8A_no4j3TMHUC4NBw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a new MySQL user</li>
<li>How to manage privileges for a user to a database or table</li>
<li>What&rsquo;s a <code>PRIMARY KEY</code></li>
<li>What&rsquo;s a <code>FOREIGN KEY</code></li>
<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
<li>How to retrieve datas from multiple tables in one request</li>
<li>What are subqueries</li>
<li>What are <code>JOIN</code> and <code>UNION</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code> (version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>

<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>

<p>Connect to your MySQL server:</p>

<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &#39;help;&#39; or &#39;\h&#39; for help. Type &#39;\c&#39; to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>

<h3>Use the sandbox to run MySQL</h3>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<ul>
<li>Ask for container <code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p
Enter password: 
$ curl &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo &quot;SELECT * FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221107T143318Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed518b0f498d8071022c8a4e0966f2e2248b7148ce26ea0f6be0685825514560" alt="" loading='lazy' style="" /></p>

  </div>
</div>
