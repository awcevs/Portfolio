<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="../js/jquery-3.7.0.js"></script>
</head>
<body>
	<style>
	.userlogin_form
	{
    	width: 400px;
	    margin: auto; 
	    padding: 0 20px;
	    margin-bottom: 20px;
	}
	.userlogin_form b
	{
	    display: block; 
	    margin-bottom: 5px;
	}
	/*
	.userlogin_form.fild
	{
		margin:5px 0;
	}
	*/
	
	.userlogin_form input:not(input[type=test])
	{
	    border: 1px solid #dadada;
	    padding: 15px;
	    width: 100%;
	    margin-bottom: 5px;
	}
	.userjoin
	{
		width:33%; 
		float:left;
		text-align: center;
	}
	.userip
	{
		width:33%; 
		float:right;
		text-align: center;
	}
	.joinok
	{
		width:33%; 
		float:left;
		/*border: 1px solid gold; 
		float: left; 
		width: 33%;"
		*/
	}
	.joincansel
	{
		width:33%;
		float: right;
		/*
		border: 1px solid gold; 
		float: left; 
		width: 33%;
		*/
	}
	.userloginok
	{
		width:33%; 
		float:left;
	}
	.userlogincansel
	{
		width:33%; 
		float:right;
	}
	</style>
	<script>
		window.onload = function()
		{
			$("#userid").focus();
			
			$("#loginFrm").submit(function(){
				
				if($("#userid").val() == "")
				{
					alert("아이디를 입력하세요");
					$("#userid").focus();
					return false;
				}
				if($("#userpw").val() == "")
				{
					alert("비밀번호를 입력하세요");
					$("#userpw").focus();
					return false;
				}			
				return true;
			});
		}
	</script>
	<center><a href="../main/index.jsp"><img src="../images/logo2.png"></a></center>
	<form id="loginFrm" name="loginFrm" method="post" action="userloginok.jsp">
		<div class="userlogin_form">
			<div class="fild">
				<b>아이디</b>
				<input class="userid" type="text" id="userid" name="userid" placeholder="아이디를 입력해주세요.">
			</div>
			<div class="fild">
				<b>비밀번호</b>
				<input class="userpw" type="password" id="userpw" name="userpw" placeholder="비밀번호를 입력해주세요.">
			</div>
			<div class=userjoin>
			<a href="./userjoin.jsp"><b>회원가입</b></a>
			</div>
			<div class=userip>
				<a href="./userip.jsp"><b>아이디 /비밀번호 찾기</b></a>
			</div>
			<br>
			<br>
			<br>
			<div class="userloginok">
				<input class="joinok" type="submit" value="로그인">
			</div>
			<div class="userlogincansel">
				<a href="../main/index.jsp"><input class="joincansel" type="button" value="취소"></a>
			</div>
		</div>
	</form>
</body>
</html>