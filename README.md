# MVC-web--frame 
*自制的 MVC web 框架*
 


- 直接使用底层的 **Socket** 代码编写Web Server功能，具备网络请求和响应的收发和监听功能，在架构中负责：转发请求数据到 Web 框架和发送返回的响应至指定客户端

- 采用的MVC设计中，**Control** 部分由自制的Web 框架实现，实现了解释HTTP请求为易用实例、注册路由与路由函数映射、HTTP 响应数据组装接口、HTML 模板渲染、错误页面和重定向接口等功能，可以处理静态资源、表单、Ajax请求，在架构负责：解释请求，路由分发、生成响应返回

- **Modle** 部分通过**自制的ORM**实现，抽象了增删改查接口的基类，同时可以对不同类型的数据进行实例化形式的数据使用，封装了针对不同的数据操作函数

- **View**部分使用Jinja2模板语言，用于通过模板生成网页HTML代码


- 可以实现用户注册、登录功能，密码 Hash 加盐保护，微博留言与评论的 CRUD，用户管理功能


----------
![](https://github.com/Armrun/Flask--bbs1.1/blob/master/git图/web%20框架.gif)