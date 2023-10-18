<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
UserVO user = new UserVO();

request.setCharacterEncoding("utf-8");

//아이디/비밀번호를 login.jsp로부터 받는다.
user.setId(request.getParameter("userid"));
user.setPw(request.getParameter("userpw"));

//아이디 또는 비밀번호가 null 인지 검사한다.
if( user.getId() == null || user.getPw() == null)
{
	response.sendRedirect("userlogin.jsp");
	return;
}
//DTO를 이용해서 로그인 처리한다.
UserDTO dto = new UserDTO();
if( dto.Login(user.getId(), user.getPw()) == false)
{
	//아이디나 비번틀림.
	%>
	<script>
		alert("아이디 또는 비밀번호가 일치하지 않습니다.");
		document.location= "userlogin.jsp";
	</script>
	<%	
}else
{
	//로그인 사용자 정보를 읽는다.
	user = dto.Read(user.getId());
	
	session.setAttribute("login",user);
	response.sendRedirect("../main/index.jsp");
}

%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<style>
	.loginfrom
	{
    	width: 400px;
	    margin: auto; 
	    padding: 0 20px;
	    margin-bottom: 20px;
	}
	.text
	{
	    display: block; 
	    margin-bottom: 5px;
	    width:33%; 
		text-align:center;
		margin: 0 auto;
		height: auto;
	}
	.loginfrom input:not(input[type=test]),.userjoin_form select
	{
	    border: 1px solid #dadada;
	    padding: 15px;
	    width: 100%;
	    margin-bottom: 5px;
	}
	.loginok
	{
		width:33%; 
		/*float:left;
		/*border: 1px solid gold; 
		float: left; 
		width: 33%;"
		*/
		text-align:center;
		margin: 0 auto;
		height: auto;
	}
	</style>
	<center><img src="../images/logo2.png"></center>
	<b class=text>로그인이 완료되었습니다.</b>
	<br>
	<br>
	<div class=loginfrom>
		<div class=loginok>
			<a href="../index.jsp"><input class="loginok" type="submit" value="메인 화면"></a>
		</div>
	</div>
</body>
</html>